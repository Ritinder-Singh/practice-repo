# =============================================================================
# System Design — API Design
# =============================================================================
# Topics: REST principles, rate limiting (token bucket, sliding window),
#         pagination (cursor vs offset), idempotency, API versioning.
# Run: python 05_api_design.py
# Ref: https://cloud.google.com/apis/design  (Google API Design Guide)
#      https://github.com/microsoft/api-guidelines
# =============================================================================

import time
import threading
import hashlib
from collections import deque
from dataclasses import dataclass, field
from typing import Optional


# =============================================================================
# TODO 1: Token Bucket Rate Limiter
# =============================================================================
# Token bucket: refill at a steady rate, burst allowed up to bucket capacity.
# Used by: AWS API Gateway, Stripe, GitHub API.
#
# class TokenBucketRateLimiter:
#     def __init__(self, capacity: int, refill_rate: float):
#         """
#         capacity:    max burst size (tokens in bucket at full)
#         refill_rate: tokens added per second
#         """
#         self.capacity = capacity
#         self.refill_rate = refill_rate
#         self.tokens = float(capacity)
#         self.last_refill = time.time()
#         self._lock = threading.Lock()
#
#     def _refill(self) -> None:
#         now = time.time()
#         elapsed = now - self.last_refill
#         added = elapsed * self.refill_rate
#         self.tokens = min(self.capacity, self.tokens + added)
#         self.last_refill = now
#
#     def allow(self, tokens: int = 1) -> bool:
#         with self._lock:
#             self._refill()
#             if self.tokens >= tokens:
#                 self.tokens -= tokens
#                 return True
#             return False
#
# limiter = TokenBucketRateLimiter(capacity=10, refill_rate=2)  # 2 req/sec, burst 10
# allowed = sum(1 for _ in range(15) if limiter.allow())
# print(f"Allowed: {allowed}/15 (burst=10)")  # Should be 10 (full burst)


# =============================================================================
# TODO 2: Sliding Window Rate Limiter
# =============================================================================
# Sliding window: count requests in the last N seconds (more precise than fixed window).
# Fixed window flaw: 100 req at 0:59 + 100 req at 1:01 = 200 req in 2 seconds
# (both windows were < limit, but together violate the spirit of "100/min").
#
# class SlidingWindowRateLimiter:
#     def __init__(self, limit: int, window_seconds: int):
#         self.limit = limit
#         self.window = window_seconds
#         self._requests: dict[str, deque] = {}   # user_id → deque of timestamps
#         self._lock = threading.Lock()
#
#     def allow(self, user_id: str) -> bool:
#         now = time.time()
#         window_start = now - self.window
#         with self._lock:
#             if user_id not in self._requests:
#                 self._requests[user_id] = deque()
#             dq = self._requests[user_id]
#             # Remove timestamps outside the window
#             while dq and dq[0] < window_start:
#                 dq.popleft()
#             if len(dq) >= self.limit:
#                 return False
#             dq.append(now)
#             return True
#
# limiter = SlidingWindowRateLimiter(limit=5, window_seconds=10)
# for i in range(8):
#     result = limiter.allow("user:1")
#     print(f"Request {i+1}: {'✅ allowed' if result else '❌ rate limited'}")


# =============================================================================
# TODO 3: Idempotency Keys — safe retries
# =============================================================================
# Problem: client sends payment request, network times out, client retries.
# Without idempotency: payment charged TWICE.
# Solution: client sends a unique Idempotency-Key header.
# Server deduplicates: if same key seen before → return cached response.
#
# class IdempotencyStore:
#     def __init__(self, ttl_seconds: int = 86400):  # 24 hour TTL
#         self._store: dict[str, tuple] = {}   # key → (response, timestamp)
#         self.ttl = ttl_seconds
#
#     def get(self, key: str) -> Optional[dict]:
#         if key not in self._store:
#             return None
#         response, stored_at = self._store[key]
#         if time.time() - stored_at > self.ttl:
#             del self._store[key]
#             return None
#         return response
#
#     def store(self, key: str, response: dict) -> None:
#         self._store[key] = (response, time.time())
#
# idempotency = IdempotencyStore()
#
# def process_payment(idempotency_key: str, amount: float, user_id: int) -> dict:
#     cached = idempotency.get(idempotency_key)
#     if cached:
#         print("Returning cached response (duplicate request)")
#         return cached
#     # Actually charge the user
#     result = {"status": "charged", "amount": amount, "transaction_id": str(uuid.uuid4())}
#     idempotency.store(idempotency_key, result)
#     return result
#
# key = "pay_xyz_123"
# r1 = process_payment(key, 99.99, user_id=1)
# r2 = process_payment(key, 99.99, user_id=1)   # retry — same key
# assert r1["transaction_id"] == r2["transaction_id"]  # same response, no double charge


# =============================================================================
# TODO 4: Cursor-based pagination (production standard)
# =============================================================================
# Offset pagination (OFFSET 1000 LIMIT 10) is slow and inconsistent:
#   - OFFSET scans and discards 1000 rows every time
#   - New items inserted → pages shift → duplicate/missing items
#
# Cursor pagination: encode the last seen item as the cursor.
#   - O(log N) instead of O(N)  — no scan needed, uses index
#   - Stable: insertions don't shift pages
#
# class CursorPaginator:
#     def __init__(self, items: list[dict]):
#         self.items = sorted(items, key=lambda x: x["id"])
#
#     def _encode_cursor(self, item_id: int) -> str:
#         import base64
#         return base64.b64encode(f"id:{item_id}".encode()).decode()
#
#     def _decode_cursor(self, cursor: str) -> int:
#         import base64
#         decoded = base64.b64decode(cursor.encode()).decode()
#         return int(decoded.split(":")[1])
#
#     def paginate(self, cursor: Optional[str], limit: int = 10) -> dict:
#         start_id = self._decode_cursor(cursor) if cursor else 0
#         page = [i for i in self.items if i["id"] > start_id][:limit]
#         next_cursor = self._encode_cursor(page[-1]["id"]) if len(page) == limit else None
#         return {"data": page, "next_cursor": next_cursor, "has_more": next_cursor is not None}
#
# items = [{"id": i, "name": f"item_{i}"} for i in range(1, 101)]
# paginator = CursorPaginator(items)
# page1 = paginator.paginate(cursor=None, limit=10)
# page2 = paginator.paginate(cursor=page1["next_cursor"], limit=10)
# print(f"Page 1 IDs: {[i['id'] for i in page1['data']]}")  # 1–10
# print(f"Page 2 IDs: {[i['id'] for i in page2['data']]}")  # 11–20


# =============================================================================
# TODO 5: REST API Design — apply the conventions
# =============================================================================
# Design the URL structure and HTTP methods for a task management API.
# Apply these rules:
#   - Nouns for resources, not verbs: /tasks not /getTasks
#   - Plural collection names: /tasks not /task
#   - HTTP methods carry the action: GET (read), POST (create), PUT (replace), PATCH (update), DELETE
#   - Nested resources for relationships: /users/{id}/tasks
#   - Status codes: 200 OK, 201 Created, 204 No Content, 400 Bad Request, 401, 403, 404, 409, 422, 429, 500
#   - Idempotent: GET, PUT, DELETE (safe to retry). NOT idempotent: POST (creates new resource each time)
#
# Complete the design:
# API_DESIGN = {
#     "list tasks":     {"method": "GET",    "url": "/tasks",            "response": 200},
#     "get task":       {"method": "GET",    "url": "/tasks/{id}",       "response": 200},
#     "create task":    {"method": "POST",   "url": "/tasks",            "response": 201},
#     "update task":    {"method": "PATCH",  "url": "/tasks/{id}",       "response": 200},
#     "replace task":   {"method": "PUT",    "url": "/tasks/{id}",       "response": 200},
#     "delete task":    {"method": "DELETE", "url": "/tasks/{id}",       "response": 204},
#     "complete task":  {"method": "POST",   "url": "/tasks/{id}/complete", "response": 200},  # action as sub-resource
#     "user's tasks":   {"method": "GET",    "url": "/users/{id}/tasks", "response": 200},
# }
# Extend: add search (?q=keyword), filter (?status=done), sort (?sort=-created_at)


# =============================================================================
# TODO 6: API Versioning strategies
# =============================================================================
# Compare the 3 approaches and when to use each:
#
# 1. URI versioning (most common, explicit):
#    GET /v1/users     vs     GET /v2/users
#    ✅ Clear, easy to route, easy to document separately
#    ❌ Breaks REST purity (version is not a resource)
#
# 2. Header versioning:
#    GET /users  with  Accept: application/vnd.myapp.v2+json
#    ✅ Clean URLs, follows HTTP spec
#    ❌ Harder to test in browser, harder to cache (Vary header required)
#
# 3. Query param versioning:
#    GET /users?version=2
#    ✅ Easy to test in browser
#    ❌ Can get lost, pollutes query params
#
# EXERCISE: You're breaking a /users response (removing "phone" field, renaming "full_name" to "name").
#   1. Which strategy would you pick and why?
#   2. How long do you maintain v1 alongside v2?
#   3. How do you communicate the deprecation to clients?


if __name__ == "__main__":
    print("API Design — implement TODOs above")
