# =============================================================================
# AI/ML — RAG (Retrieval-Augmented Generation) Pipeline
# =============================================================================
# Topics: chunking, embedding, vector search (cosine similarity),
#         FAISS/pgvector patterns, retrieval, augmented prompting.
# Run: python 02_rag_pipeline.py
# Ref: Resume — "RAG knowledge base serving 10+ internal teams for Voice AI" (Genius365)
#               "SecondBrain — ingests URLs, files, GitHub repos, Obsidian vaults"
# =============================================================================

import math
import hashlib
from dataclasses import dataclass, field
from typing import Optional
import json

# pip install sentence-transformers faiss-cpu anthropic
# Real stack: sentence-transformers for embeddings, FAISS or pgvector for search


# =============================================================================
# 1. CHUNKING STRATEGIES
# =============================================================================

@dataclass
class Chunk:
    id: str
    text: str
    metadata: dict
    embedding: Optional[list[float]] = None


def chunk_fixed_size(text: str, chunk_size: int = 512, overlap: int = 64) -> list[str]:
    """Fixed-size character chunking with overlap."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks


def chunk_by_paragraph(text: str, max_chars: int = 1000) -> list[str]:
    """Split on double newlines, merge small paragraphs."""
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks, current = [], ""
    for p in paragraphs:
        if len(current) + len(p) > max_chars and current:
            chunks.append(current.strip())
            current = p
        else:
            current = f"{current}\n\n{p}" if current else p
    if current:
        chunks.append(current.strip())
    return chunks


def chunk_by_sentence(text: str, sentences_per_chunk: int = 5) -> list[str]:
    """Simple sentence-boundary chunking."""
    import re
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [
        " ".join(sentences[i:i + sentences_per_chunk])
        for i in range(0, len(sentences), sentences_per_chunk)
    ]


# =============================================================================
# 2. EMBEDDING (mock — replace with real model)
# =============================================================================

def embed_text_mock(text: str, dim: int = 384) -> list[float]:
    """
    Mock embedding. In production:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer('all-MiniLM-L6-v2')  # 384-dim, fast
        embedding = model.encode(text).tolist()

    Or via API:
        client.embeddings.create(model="text-embedding-3-small", input=text)
    """
    # Deterministic fake embedding based on text hash
    h = int(hashlib.md5(text.encode()).hexdigest(), 16)
    rng = [(h * (i + 1) % 997) / 997.0 for i in range(dim)]
    magnitude = math.sqrt(sum(x**2 for x in rng))
    return [x / magnitude for x in rng]  # L2 normalized


# =============================================================================
# 3. VECTOR STORE (in-memory — mirrors what FAISS / pgvector does)
# =============================================================================

class VectorStore:
    """
    Simplified flat vector store. Production alternatives:
    - FAISS (local, fast): faiss.IndexFlatIP for cosine on normalized vecs
    - pgvector: ALTER TABLE ... ADD COLUMN embedding vector(384);
                SELECT * FROM docs ORDER BY embedding <=> $1 LIMIT 5;
    - Qdrant, Pinecone, Weaviate for managed/distributed
    """

    def __init__(self):
        self.chunks: list[Chunk] = []

    def add(self, text: str, metadata: dict = {}) -> Chunk:
        chunk_id = hashlib.md5(text.encode()).hexdigest()[:8]
        embedding = embed_text_mock(text)
        chunk = Chunk(id=chunk_id, text=text, metadata=metadata, embedding=embedding)
        self.chunks.append(chunk)
        return chunk

    def search(self, query: str, top_k: int = 3) -> list[tuple[Chunk, float]]:
        query_emb = embed_text_mock(query)
        scored = [(chunk, self._cosine(query_emb, chunk.embedding)) for chunk in self.chunks]
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]

    @staticmethod
    def _cosine(a: list[float], b: list[float]) -> float:
        dot = sum(x * y for x, y in zip(a, b))
        mag_a = math.sqrt(sum(x**2 for x in a))
        mag_b = math.sqrt(sum(x**2 for x in b))
        return dot / (mag_a * mag_b + 1e-9)


# =============================================================================
# 4. FULL RAG PIPELINE
# =============================================================================

class RAGPipeline:
    """End-to-end RAG: ingest → retrieve → augment → generate."""

    def __init__(self):
        self.store = VectorStore()

    def ingest(self, text: str, source: str = "unknown") -> int:
        chunks = chunk_by_paragraph(text, max_chars=800)
        for i, chunk_text in enumerate(chunks):
            self.store.add(chunk_text, metadata={"source": source, "chunk_idx": i})
        return len(chunks)

    def retrieve(self, query: str, top_k: int = 3) -> list[Chunk]:
        results = self.store.search(query, top_k)
        return [chunk for chunk, score in results if score > 0.5]

    def build_context(self, chunks: list[Chunk]) -> str:
        parts = []
        for i, chunk in enumerate(chunks):
            src = chunk.metadata.get("source", "?")
            parts.append(f"[Source {i+1}: {src}]\n{chunk.text}")
        return "\n\n---\n\n".join(parts)

    def build_prompt(self, query: str, context: str) -> str:
        return f"""Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't have that information."

Context:
{context}

Question: {query}

Answer:"""

    def query(self, question: str) -> dict:
        chunks = self.retrieve(question)
        if not chunks:
            return {"answer": "No relevant context found.", "sources": []}
        context = self.build_context(chunks)
        prompt = self.build_prompt(question, context)
        # In production: send prompt to LLM
        return {
            "answer": f"[LLM would answer based on {len(chunks)} retrieved chunks]",
            "prompt_preview": prompt[:300] + "...",
            "sources": [c.metadata.get("source") for c in chunks],
        }


# =============================================================================
# 5. PGVECTOR PATTERN (SQL — for SecondBrain / Genius365 PostgreSQL stack)
# =============================================================================

PGVECTOR_SETUP = """
-- Enable extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Table with embedding column
CREATE TABLE knowledge_chunks (
    id          SERIAL PRIMARY KEY,
    source      TEXT,
    chunk_idx   INT,
    content     TEXT,
    embedding   vector(384),
    created_at  TIMESTAMPTZ DEFAULT NOW()
);

-- IVFFlat index for approximate nearest-neighbor (fast at scale)
CREATE INDEX ON knowledge_chunks USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);

-- Retrieval query (cosine distance — lower is closer)
-- SELECT content, source, 1 - (embedding <=> $1::vector) AS similarity
-- FROM knowledge_chunks
-- ORDER BY embedding <=> $1::vector
-- LIMIT 5;
"""


# =============================================================================
# DEMO
# =============================================================================

SAMPLE_DOCS = [
    ("FastAPI supports async/await natively. Use async def for route handlers that do IO. "
     "Pydantic models handle request validation automatically.", "fastapi_docs"),

    ("PostgreSQL supports JSONB for semi-structured data. Use GIN indexes on JSONB columns "
     "for fast key/value lookups. JSONB is stored in binary format.", "postgres_docs"),

    ("Redis supports several data structures: strings, hashes, lists, sets, sorted sets. "
     "Use EXPIRE to set TTL on keys. ZADD for leaderboards with scores.", "redis_docs"),

    ("n8n is a workflow automation tool. Use HTTP Request nodes to call external APIs. "
     "Webhook nodes trigger workflows from external events.", "n8n_docs"),
]

if __name__ == "__main__":
    rag = RAGPipeline()

    print("=== Ingesting Documents ===")
    for text, source in SAMPLE_DOCS:
        n = rag.ingest(text, source=source)
        print(f"  {source}: {n} chunk(s)")

    print("\n=== Querying RAG Pipeline ===")
    queries = [
        "How do I set TTL on Redis keys?",
        "What is JSONB in PostgreSQL?",
        "How does n8n handle webhooks?",
    ]
    for q in queries:
        result = rag.query(q)
        print(f"\nQ: {q}")
        print(f"Sources: {result['sources']}")
        print(f"Preview: {result['prompt_preview'][:120]}...")

    print("\n=== Chunking Strategies ===")
    sample = "First sentence. Second sentence. Third sentence. Fourth sentence. Fifth sentence. Sixth one."
    print(f"By sentence (3/chunk): {chunk_by_sentence(sample, 3)}")

    # TODO: Wire up real sentence-transformers embeddings
    # TODO: Connect to pgvector / FAISS for production search
    # TODO: Add re-ranking step (cross-encoder) after retrieval
    # TODO: Add metadata filtering (filter by source, date, etc.)
