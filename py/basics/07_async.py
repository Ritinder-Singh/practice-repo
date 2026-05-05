# =============================================================================
# Python — Async/Await & asyncio
# =============================================================================
# Topics: coroutines, event loop, asyncio.gather, asyncio.create_task,
#         asyncio.Queue, aiohttp basics, async context managers/iterators.
# Run: python 07_async.py
# Docs: https://docs.python.org/3/library/asyncio.html
# =============================================================================

import asyncio
import time
from typing import AsyncIterator

# TODO 1: Basic coroutine vs regular function
#   Write a coroutine fetch_data(url: str, delay: float) that simulates
#   an HTTP request by sleeping delay seconds then returning a mock response.
#   Show the difference: calling it returns a coroutine object, not a result.
#   Use asyncio.run() to execute it.
#
# async def fetch_data(url: str, delay: float) -> str:
#     await asyncio.sleep(delay)
#     return f"Data from {url}"

# TODO 2: asyncio.gather — concurrent execution
#   Fetch 5 URLs concurrently (each takes 1s) and show it completes in ~1s total.
#   Compare to sequential (would take ~5s).
#   Use time.perf_counter() to measure.
#
# async def main():
#     urls = [f"https://example.com/{i}" for i in range(5)]
#     results = await asyncio.gather(*[fetch_data(url, 1.0) for url in urls])
#     print(results)

# TODO 3: asyncio.create_task — fire and forget
#   Create tasks that run "in background" while main coroutine does other work.
#   tasks = [asyncio.create_task(fetch_data(url, 1)) for url in urls]
#   await asyncio.gather(*tasks)

# TODO 4: asyncio.Queue — producer/consumer pattern
#   Producer puts items into queue. Consumer processes them.
#   Run 1 producer and 3 consumers concurrently.
#
# async def producer(queue: asyncio.Queue, items: list) -> None:
#     for item in items:
#         await queue.put(item)
#         await asyncio.sleep(0.1)
#     await queue.put(None)  # sentinel
#
# async def consumer(queue: asyncio.Queue, name: str) -> None:
#     while True:
#         item = await queue.get()
#         if item is None:
#             await queue.put(None)  # pass sentinel to next consumer
#             break
#         print(f"{name} processed {item}")
#         queue.task_done()

# TODO 5: Async context manager
#   Implement AsyncTimer as an async context manager (__aenter__/__aexit__):
#
# class AsyncTimer:
#     async def __aenter__(self):
#         self._start = time.perf_counter()
#         return self
#
#     async def __aexit__(self, *args):
#         elapsed = time.perf_counter() - self._start
#         print(f"Elapsed: {elapsed:.3f}s")

# TODO 6: Async iterator / async generator
#   Write an async generator that yields chunks from a simulated stream:
#
# async def stream_data(n: int) -> AsyncIterator[str]:
#     for i in range(n):
#         await asyncio.sleep(0.1)  # simulate network delay per chunk
#         yield f"chunk_{i}"
#
# # Consume with: async for chunk in stream_data(5): ...

# TODO 7: asyncio.timeout (Python 3.11+) / asyncio.wait_for
#   Wrap a slow coroutine with a timeout. Catch asyncio.TimeoutError.
#
# async def slow_operation():
#     await asyncio.sleep(10)
#
# async def main():
#     try:
#         await asyncio.wait_for(slow_operation(), timeout=2.0)
#     except asyncio.TimeoutError:
#         print("Operation timed out!")
