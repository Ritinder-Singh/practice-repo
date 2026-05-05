# =============================================================================
# AI/ML — Audio Processing & Transcription
# =============================================================================
# Topics: Whisper API, batch transcription, chunking audio, diarization,
#         post-processing transcripts, downstream pipeline patterns.
# Run: python 03_audio_transcription.py
# Ref: Resume — "high-volume transcription system processing 500+ hours/month,
#      powering downstream Voice AI model training" (Genius365)
# =============================================================================

import os
import json
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

# pip install openai pydub


# =============================================================================
# 1. WHISPER TRANSCRIPTION (OpenAI API pattern)
# =============================================================================

@dataclass
class TranscriptSegment:
    start: float   # seconds
    end: float
    text: str
    speaker: Optional[str] = None  # after diarization
    confidence: Optional[float] = None


@dataclass
class Transcript:
    audio_file: str
    language: str
    duration_seconds: float
    segments: list[TranscriptSegment]
    full_text: str
    processing_time_ms: int

    def to_json(self) -> dict:
        return {
            "audio_file": self.audio_file,
            "language": self.language,
            "duration_seconds": self.duration_seconds,
            "full_text": self.full_text,
            "segments": [
                {"start": s.start, "end": s.end, "text": s.text, "speaker": s.speaker}
                for s in self.segments
            ],
        }


def transcribe_file_mock(file_path: str) -> Transcript:
    """
    Mock of Whisper transcription. In production:

        import openai
        client = openai.OpenAI()

        with open(file_path, "rb") as f:
            response = client.audio.transcriptions.create(
                model="whisper-1",
                file=f,
                response_format="verbose_json",  # includes segments + timestamps
                language="en",
            )

        segments = [
            TranscriptSegment(start=s.start, end=s.end, text=s.text)
            for s in response.segments
        ]
    """
    time.sleep(0.01)  # simulate API latency
    return Transcript(
        audio_file=file_path,
        language="en",
        duration_seconds=183.4,
        segments=[
            TranscriptSegment(0.0, 4.2, "Hi, this is Alex from TechSales.", speaker="Agent"),
            TranscriptSegment(4.5, 7.1, "Yes, who is this?", speaker="Customer"),
            TranscriptSegment(7.3, 15.0, "Alex from TechSales. We help companies reduce cloud spend.", speaker="Agent"),
        ],
        full_text="Hi, this is Alex from TechSales. Yes, who is this? Alex from TechSales...",
        processing_time_ms=1240,
    )


# =============================================================================
# 2. BATCH PROCESSING PIPELINE (the 500+ hours/month pattern)
# =============================================================================

class TranscriptionPipeline:
    """
    High-volume batch transcription with concurrency control.
    Mirrors the Genius365 audio processing system.
    """

    def __init__(self, max_workers: int = 10, output_dir: str = "transcripts"):
        self.max_workers = max_workers
        self.output_dir = Path(output_dir)
        self.stats = {"success": 0, "failed": 0, "total_duration": 0.0}

    def process_batch(self, audio_files: list[str]) -> list[Transcript]:
        results = []
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(self._process_one, f): f for f in audio_files}
            for future in as_completed(futures):
                file = futures[future]
                try:
                    transcript = future.result()
                    results.append(transcript)
                    self.stats["success"] += 1
                    self.stats["total_duration"] += transcript.duration_seconds
                except Exception as e:
                    print(f"Failed: {file} — {e}")
                    self.stats["failed"] += 1
        return results

    def _process_one(self, file_path: str) -> Transcript:
        transcript = transcribe_file_mock(file_path)
        self._save(transcript)
        return transcript

    def _save(self, transcript: Transcript):
        out = self.output_dir / f"{Path(transcript.audio_file).stem}.json"
        # In production: out.write_text(json.dumps(transcript.to_json(), indent=2))
        pass

    def throughput_stats(self) -> dict:
        hours = self.stats["total_duration"] / 3600
        return {
            "files_processed": self.stats["success"],
            "files_failed": self.stats["failed"],
            "total_audio_hours": round(hours, 2),
            "success_rate": f"{self.stats['success'] / max(1, self.stats['success'] + self.stats['failed']):.1%}",
        }


# =============================================================================
# 3. AUDIO CHUNKING (for files > 25MB Whisper limit)
# =============================================================================

def chunk_audio_plan(file_path: str, chunk_minutes: int = 10) -> list[dict]:
    """
    Plan for splitting audio into chunks before transcription.

    With pydub:
        from pydub import AudioSegment
        audio = AudioSegment.from_file(file_path)
        chunk_ms = chunk_minutes * 60 * 1000
        chunks = [audio[i:i+chunk_ms] for i in range(0, len(audio), chunk_ms)]
        for i, chunk in enumerate(chunks):
            chunk.export(f"chunk_{i}.mp3", format="mp3")
    """
    chunk_seconds = chunk_minutes * 60
    # Simulated 45-minute file
    total_seconds = 2700
    return [
        {"chunk_idx": i, "start_sec": i * chunk_seconds, "end_sec": min((i+1) * chunk_seconds, total_seconds)}
        for i in range(math.ceil(total_seconds / chunk_seconds))
    ]


# =============================================================================
# 4. POST-PROCESSING: TRANSCRIPT CLEANUP + SPEAKER DIARIZATION
# =============================================================================

import re

def clean_transcript(text: str) -> str:
    """Remove filler words, normalize spacing."""
    fillers = r'\b(um|uh|like|you know|sort of|kind of|basically)\b'
    text = re.sub(fillers, '', text, flags=re.IGNORECASE)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def assign_speakers(segments: list[TranscriptSegment], num_speakers: int = 2) -> list[TranscriptSegment]:
    """
    Placeholder for speaker diarization.
    In production use pyannote.audio or AssemblyAI diarization:
        assemblyai.TranscriptionConfig(speaker_labels=True)
    Naive assignment alternates speakers on long pauses.
    """
    speaker_map = {0: "Agent", 1: "Customer"}
    current_speaker = 0
    for i, seg in enumerate(segments):
        if i > 0 and (seg.start - segments[i-1].end) > 1.5:
            current_speaker = (current_speaker + 1) % num_speakers
        seg.speaker = speaker_map[current_speaker]
    return segments


# =============================================================================
# 5. DOWNSTREAM: STRUCTURED OUTPUT FOR VOICE AI TRAINING
# =============================================================================

def format_for_training(transcript: Transcript) -> list[dict]:
    """
    Convert transcript to training data format for fine-tuning Voice AI.
    Alternating agent/customer turns → instruction-response pairs.
    """
    pairs = []
    agent_segs = [s for s in transcript.segments if s.speaker == "Agent"]
    customer_segs = [s for s in transcript.segments if s.speaker == "Customer"]

    for i, agent_seg in enumerate(agent_segs):
        customer_response = customer_segs[i] if i < len(customer_segs) else None
        pairs.append({
            "instruction": agent_seg.text,
            "response": customer_response.text if customer_response else "",
            "timestamp": agent_seg.start,
        })
    return pairs


# =============================================================================
# DEMO
# =============================================================================

import math

if __name__ == "__main__":
    print("=== Single File Transcription ===")
    t = transcribe_file_mock("call_2024_01_15_alex.mp3")
    print(json.dumps(t.to_json(), indent=2))

    print("\n=== Batch Pipeline (simulating 500+ hrs/month) ===")
    pipeline = TranscriptionPipeline(max_workers=5)
    fake_files = [f"call_{i:04d}.mp3" for i in range(20)]
    transcripts = pipeline.process_batch(fake_files)
    print(json.dumps(pipeline.throughput_stats(), indent=2))

    print("\n=== Audio Chunk Plan (45-min file) ===")
    chunks = chunk_audio_plan("long_call.mp3", chunk_minutes=10)
    for c in chunks:
        print(f"  Chunk {c['chunk_idx']}: {c['start_sec']}s – {c['end_sec']}s")

    print("\n=== Speaker Diarization ===")
    segs = assign_speakers(t.segments)
    for s in segs:
        print(f"  [{s.speaker}] {s.start:.1f}s: {s.text}")

    print("\n=== Training Data Format ===")
    pairs = format_for_training(t)
    print(json.dumps(pairs, indent=2))

    # TODO: Integrate pyannote.audio for real diarization
    # TODO: Add confidence filtering (drop segments < 0.7 confidence)
    # TODO: Connect to database for transcript storage + retrieval
