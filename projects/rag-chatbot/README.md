# RAG Chatbot — Python + Streamlit + Qdrant

A teaching project covering RAG pipelines, embeddings, reranking, and LLM integration.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Streamlit App                          │
│   ┌─────────────────────┐   ┌───────────────────────────┐  │
│   │  Chat Page          │   │  Settings Page            │  │
│   │  main.py            │   │  pages/1_Settings.py      │  │
│   │  - message history  │   │  - LLM provider/model     │  │
│   │  - streaming output │   │  - temperature, max tokens│  │
│   │  - doc upload UI    │   │  - chunk size/overlap     │  │
│   └────────┬────────────┘   │  - top-k, threshold       │  │
│            │                │  - reranker toggle        │  │
└────────────┼────────────────┴───────────────────────────────┘
             │
             ▼
┌─────────────────────────────────────────────────────────────┐
│                     RAG Pipeline                            │
│                                                             │
│  INGESTION                                                  │
│  Loader → Chunker → Embedder ──────────────────┐           │
│                                                ▼           │
│  RETRIEVAL                              ┌─────────────┐    │
│  Query → Embedder → Vector Search ──►  │   Qdrant    │    │
│                          ▲             │  port 6333  │    │
│          (hybrid: dense + BM25)        └──────┬──────┘    │
│                                               │            │
│  RERANKING                                    │            │
│  Retrieved Docs → Cross-Encoder ──────────────┘            │
│                       │                                     │
│  GENERATION           ▼                                     │
│  PromptBuilder → LLMClient → streamed response              │
│                     ├── Groq API                            │
│                     └── Ollama (local)                      │
└─────────────────────────────────────────────────────────────┘
```

## Project Structure

```
rag-chatbot/
├── docker-compose.yml           # Streamlit app + Qdrant
├── Dockerfile                   # Streamlit app image
├── requirements.txt             # All Python dependencies
├── .env.example                 # GROQ_API_KEY, OLLAMA_BASE_URL, QDRANT_URL, etc.
├── README.md
│
└── app/
    ├── main.py                  # Streamlit chat page (entry point)
    ├── pages/
    │   └── 1_Settings.py        # Streamlit settings page (multi-page app)
    │
    ├── config/
    │   └── settings.py          # Pydantic BaseSettings — loads .env, holds all tuneable params
    │
    ├── rag/
    │   ├── pipeline.py          # Top-level orchestrator: routes ingestion and query calls
    │   │
    │   ├── ingestion/
    │   │   ├── loader.py        # Load documents: PDF (pypdf/PyMuPDF), TXT, web URL (BeautifulSoup)
    │   │   ├── chunker.py       # Splitting strategies: recursive char, fixed-size, sentence-aware
    │   │   └── embedder.py      # Produce vectors: sentence-transformers (local) or API-based
    │   │
    │   ├── retrieval/
    │   │   ├── vector_store.py  # Qdrant client wrapper: upsert, search, delete, list collections
    │   │   ├── retriever.py     # Dense search + hybrid (BM25 sparse + dense fusion)
    │   │   └── reranker.py      # Cross-encoder reranking (sentence-transformers), top-k selection
    │   │
    │   └── generation/
    │       ├── llm_client.py    # Provider abstraction: Groq API and Ollama behind one interface
    │       ├── prompt_builder.py # Assemble: system prompt + retrieved context + chat history
    │       └── chat_history.py  # Sliding window memory: stores last N turns in st.session_state
    │
    └── services/
        ├── chat_service.py      # End-to-end query flow: embed → retrieve → rerank → generate
        └── document_service.py  # Ingest new docs, list indexed docs, delete from Qdrant
```

## Setup

```bash
# Copy and fill in your keys
cp .env.example .env

# Run everything with Docker Compose
docker-compose up --build

# App:    http://localhost:8501
# Qdrant: http://localhost:6333  (dashboard: http://localhost:6333/dashboard)

# Or run locally (Qdrant still via Docker)
docker-compose up qdrant -d
pip install -r requirements.txt
streamlit run app/main.py
```

## Environment Variables (`.env.example`)

```
GROQ_API_KEY=
OLLAMA_BASE_URL=http://localhost:11434
QDRANT_URL=http://qdrant:6333      # use http://localhost:6333 for local dev
QDRANT_COLLECTION=rag_docs
EMBEDDING_MODEL=all-MiniLM-L6-v2  # sentence-transformers model name
```

## Adjustable Settings (via Settings Page)

| Category | Parameters |
|----------|-----------|
| LLM | Provider (Groq / Ollama), model name, temperature, max output tokens |
| Retrieval | Top-k documents, similarity score threshold |
| Chunking | Strategy (recursive / fixed / sentence), chunk size, overlap |
| Embeddings | Model name (hot-swap without restarting) |
| Reranker | Enable/disable, top-k after reranking |

## What to Build

### Config (`app/config/settings.py`)
- [ ] `AppSettings(BaseSettings)` — reads all values from `.env`; fields: `groq_api_key`, `ollama_base_url`, `qdrant_url`, `qdrant_collection`, `embedding_model`, `llm_provider` (enum: groq/ollama), `llm_model`, `temperature`, `max_tokens`, `top_k`, `similarity_threshold`, `chunk_size`, `chunk_overlap`, `reranker_enabled`, `reranker_top_k`
- [ ] Singleton pattern so settings are loaded once and shared across modules

### Ingestion — `app/rag/ingestion/`
- [ ] `loader.py` — `load_pdf(path)`, `load_txt(path)`, `load_url(url)` → return list of raw text chunks with source metadata
- [ ] `chunker.py` — `chunk_recursive(text, size, overlap)`, `chunk_fixed(text, size)`, `chunk_sentences(text)` → `List[Document]` where `Document` has `text` + `metadata`
- [ ] `embedder.py` — `Embedder` class: loads sentence-transformers model on init, `embed(texts: List[str]) -> List[List[float]]`; swap model via settings

### Retrieval — `app/rag/retrieval/`
- [ ] `vector_store.py` — `VectorStore` wrapping `qdrant_client.QdrantClient`: `create_collection()`, `upsert(docs, vectors)`, `search(query_vector, top_k, threshold)`, `delete_by_source(source_id)`, `list_all()`
- [ ] `retriever.py` — `Retriever`: `dense_search(query, top_k)` using embedder + vector_store; `hybrid_search(query, top_k)` combining dense + BM25 sparse (via `qdrant_client` sparse vectors or `rank_bm25`)
- [ ] `reranker.py` — `Reranker`: loads `cross-encoder/ms-marco-MiniLM-L-6-v2` on init; `rerank(query, docs, top_k) -> List[Document]` — scores each query-doc pair, returns sorted top-k

### Generation — `app/rag/generation/`
- [ ] `llm_client.py` — `LLMClient` with `stream_response(prompt: str) -> Iterator[str]`; internally switches between `groq.Groq().chat.completions.create(stream=True)` and `requests.post(ollama_url/api/generate, stream=True)` based on `settings.llm_provider`
- [ ] `prompt_builder.py` — `build_prompt(query, context_docs, history) -> str`: formats retrieved docs as numbered context blocks, prepends system instruction, appends conversation history
- [ ] `chat_history.py` — `ChatHistory`: wraps `st.session_state`; `add(role, content)`, `get_last_n(n)`, `clear()`; enforces sliding window

### RAG Orchestrator (`app/rag/pipeline.py`)
- [ ] `RAGPipeline`: owns retriever, reranker, llm_client, prompt_builder, chat_history
- [ ] `ingest(file_or_url)` → loads → chunks → embeds → upserts to Qdrant
- [ ] `query(user_message) -> Iterator[str]` → embeds query → retrieves → (optionally) reranks → builds prompt → streams generation

### Services (`app/services/`)
- [ ] `chat_service.py` — thin wrapper: `ask(message) -> Iterator[str]` calling `pipeline.query()`; handles `st.write_stream()`
- [ ] `document_service.py` — `ingest_document(uploaded_file)`, `list_documents()`, `delete_document(source_id)` — used by the chat page sidebar

### Streamlit UI (`app/main.py` + `app/pages/1_Settings.py`)
- [ ] `main.py` — chat interface: `st.chat_input`, `st.chat_message` bubbles, `st.write_stream` for streamed output, sidebar with document upload (`st.file_uploader`) and indexed doc list
- [ ] `1_Settings.py` — settings page: `st.selectbox` for provider/model, `st.slider` for temperature/top-k/chunk-size, `st.toggle` for reranker, `st.button("Save")` writes back to `st.session_state` (overriding defaults)

### Infrastructure
- [ ] `Dockerfile` — `python:3.12-slim`, `COPY requirements.txt`, `pip install`, `COPY app/`, `CMD ["streamlit", "run", "app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]`
- [ ] `docker-compose.yml` — two services: `app` (builds from Dockerfile, port 8501, env_file .env) and `qdrant` (image: `qdrant/qdrant`, port 6333, volume for persistence)
- [ ] `requirements.txt` — `streamlit`, `qdrant-client`, `sentence-transformers`, `groq`, `rank-bm25`, `pypdf`, `beautifulsoup4`, `requests`, `pydantic-settings`

## Key Concepts Demonstrated

| Concept | Where |
|---------|-------|
| Chunking strategies | `ingestion/chunker.py` |
| Dense embeddings | `ingestion/embedder.py` |
| Vector similarity search | `retrieval/vector_store.py` + `retriever.py` |
| Hybrid search (dense + BM25) | `retrieval/retriever.py` |
| Cross-encoder reranking | `retrieval/reranker.py` |
| Prompt construction with context | `generation/prompt_builder.py` |
| Sliding window chat memory | `generation/chat_history.py` |
| LLM provider abstraction | `generation/llm_client.py` |
| Full pipeline orchestration | `rag/pipeline.py` |
