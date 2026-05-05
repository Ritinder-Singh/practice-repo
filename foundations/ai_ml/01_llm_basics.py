# =============================================================================
# AI/ML — LLM Integration Basics
# =============================================================================
# Topics: OpenAI/Anthropic API calls, structured output (JSON mode),
#         prompt engineering, token counting, streaming, error handling.
# Run: python 01_llm_basics.py
# Ref: Resume — "LLM-based transcript analysis delivering structured JSON output
#      for call scoring and disposition classification" (Genius365)
# =============================================================================

import os
import json
from dataclasses import dataclass
from typing import Optional

# pip install anthropic openai
# from anthropic import Anthropic
# from openai import OpenAI


# =============================================================================
# 1. STRUCTURED OUTPUT — the exact pattern used at Genius365
# =============================================================================
# Goal: given a call transcript, return structured JSON for scoring/disposition

TRANSCRIPT_ANALYSIS_PROMPT = """
You are a call quality analyst. Given a sales call transcript, return a JSON object with:
- score: int (0-100) — overall call quality
- disposition: str — one of: "interested", "not_interested", "callback", "closed_won", "closed_lost"
- summary: str — 2-sentence summary
- red_flags: list[str] — any issues detected
- follow_up_required: bool

Respond ONLY with valid JSON. No markdown, no explanation.
""".strip()

SAMPLE_TRANSCRIPT = """
Agent: Hi, this is Alex from TechSales. Is this Sarah?
Customer: Yes, who's this again?
Agent: Alex from TechSales — we help companies reduce their cloud spend. Do you have 5 minutes?
Customer: I'm pretty busy actually...
Agent: I completely understand. Our clients typically save 30% on AWS costs. Would a quick 15-minute
       demo next Tuesday work better?
Customer: Maybe, send me an email first.
Agent: Absolutely. What's the best email?
Customer: sarah@company.com
Agent: Perfect, I'll send that over now. Thanks Sarah!
"""


def analyze_transcript_mock(transcript: str) -> dict:
    """Mock of the Genius365 LLM transcript analysis pipeline."""
    # In production: client.messages.create(model="claude-3-5-sonnet", ...)
    return {
        "score": 72,
        "disposition": "callback",
        "summary": "Agent successfully obtained customer email despite initial resistance. "
                   "Customer agreed to receive information but did not commit to a meeting.",
        "red_flags": ["Customer hesitant from the start", "No firm meeting booked"],
        "follow_up_required": True,
    }


# =============================================================================
# 2. PROMPT ENGINEERING PATTERNS
# =============================================================================

class PromptBuilder:
    """Chain-of-thought and few-shot prompt construction."""

    @staticmethod
    def few_shot(examples: list[dict], query: str) -> str:
        parts = []
        for ex in examples:
            parts.append(f"Input: {ex['input']}\nOutput: {ex['output']}")
        parts.append(f"Input: {query}\nOutput:")
        return "\n\n".join(parts)

    @staticmethod
    def chain_of_thought(task: str, reasoning_steps: list[str]) -> str:
        steps = "\n".join(f"{i+1}. {s}" for i, s in enumerate(reasoning_steps))
        return f"{task}\n\nThink step by step:\n{steps}\n\nNow answer:"

    @staticmethod
    def system_user(system: str, user: str) -> list[dict]:
        return [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ]


# =============================================================================
# 3. STREAMING RESPONSE HANDLER
# =============================================================================

def stream_handler_pattern():
    """
    Pattern for streaming LLM responses — used for real-time UIs.

    With Anthropic:
        with client.messages.stream(model=..., messages=...) as stream:
            for text in stream.text_stream:
                print(text, end="", flush=True)

    With OpenAI:
        for chunk in client.chat.completions.create(stream=True, ...):
            delta = chunk.choices[0].delta.content or ""
            print(delta, end="", flush=True)
    """
    print("Streaming pattern: iterate over chunks, flush each delta to stdout/websocket")


# =============================================================================
# 4. TOKEN COUNTING & COST ESTIMATION
# =============================================================================

def estimate_cost(input_tokens: int, output_tokens: int, model: str = "claude-3-5-sonnet") -> float:
    """Back-of-envelope cost calculation."""
    pricing = {
        "claude-3-5-sonnet": (3.00, 15.00),   # per million tokens (in, out)
        "claude-3-haiku":    (0.25, 1.25),
        "gpt-4o":            (5.00, 15.00),
        "gpt-4o-mini":       (0.15, 0.60),
    }
    in_price, out_price = pricing.get(model, (3.00, 15.00))
    return (input_tokens * in_price + output_tokens * out_price) / 1_000_000


# =============================================================================
# 5. RETRY + RATE LIMIT HANDLING
# =============================================================================

import time
import random

def llm_call_with_retry(fn, max_retries: int = 3):
    """Exponential backoff for rate limit errors."""
    for attempt in range(max_retries):
        try:
            return fn()
        except Exception as e:
            if "rate_limit" in str(e).lower() and attempt < max_retries - 1:
                wait = (2 ** attempt) + random.uniform(0, 1)
                print(f"Rate limited. Retrying in {wait:.1f}s...")
                time.sleep(wait)
            else:
                raise


# =============================================================================
# DEMO
# =============================================================================

if __name__ == "__main__":
    print("=== LLM Transcript Analysis (Genius365 Pattern) ===\n")
    result = analyze_transcript_mock(SAMPLE_TRANSCRIPT)
    print(json.dumps(result, indent=2))

    print("\n=== Cost Estimation ===")
    cost = estimate_cost(input_tokens=1500, output_tokens=200, model="claude-3-5-sonnet")
    print(f"500 calls/day @ ~1700 tokens each: ${cost * 500:.4f}/day")

    print("\n=== Few-Shot Prompt ===")
    prompt = PromptBuilder.few_shot(
        examples=[
            {"input": "Customer hung up immediately", "output": "not_interested"},
            {"input": "Customer asked for pricing sheet", "output": "interested"},
        ],
        query="Customer said 'let me think about it and call you back'",
    )
    print(prompt)

    # TODO: Wire up real Anthropic/OpenAI client
    # TODO: Add tool use / function calling
    # TODO: Add multi-turn conversation state management
