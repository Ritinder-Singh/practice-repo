# =============================================================================
# System Design — Interview Problems
# =============================================================================
# The 7 classic designs every SDE interview covers. Each has:
#   - Requirements clarification checklist
#   - Back-of-envelope estimation
#   - Core component breakdown
#   - Coding exercise (the implementable core)
#
# RADIO framework for each problem:
#   R — Requirements (functional + non-functional)
#   A — API design
#   D — Data model
#   I — Implementation (high-level architecture)
#   O — Optimise (scaling, bottlenecks, edge cases)
#
# Run: python 07_interview_problems.py
# Ref: https://github.com/donnemartin/system-design-primer
#      Alex Xu — "System Design Interview Vol. 1"
# =============================================================================

import hashlib
import time
import string
import random
from collections import defaultdict, deque
from dataclasses import dataclass, field
from typing import Optional


# =============================================================================
# DESIGN 1: URL Shortener (bit.ly)
# =============================================================================
# Requirements:
#   Functional:  shorten URL, redirect short URL, custom aliases optional
#   Non-functional: 100M URLs/day writes, 10:1 read:write, <10ms redirect p99
#
# Estimation:
#   writes/sec = 100M / 86400 ≈ 1,157/sec
#   reads/sec  = 1B   / 86400 ≈ 11,574/sec
#   Storage 5yr: 100M * 365 * 5 * 500 bytes ≈ 91 TB
#
# Key design choices:
#   - 7-char base62 code = 62^7 ≈ 3.5 trillion URLs
#   - Redirect: 301 (permanent, browser caches) vs 302 (temporary, server sees all)
#   - Storage: Postgres for URL mappings, Redis for hot URL cache
#
# TODO: Implement the core — generate + resolve short codes
#
# class URLShortener:
#     BASE62 = string.ascii_letters + string.digits  # 62 chars
#
#     def __init__(self):
#         self.url_to_code: dict[str, str] = {}
#         self.code_to_url: dict[str, str] = {}
#         self._counter = 1   # in production: distributed ID (Snowflake)
#
#     def _encode(self, n: int) -> str:
#         """Convert integer to base62 string."""
#         result = []
#         while n:
#             result.append(self.BASE62[n % 62])
#             n //= 62
#         return "".join(reversed(result)).zfill(7)
#
#     def shorten(self, long_url: str, custom_alias: Optional[str] = None) -> str:
#         if long_url in self.url_to_code:
#             return self.url_to_code[long_url]
#         code = custom_alias or self._encode(self._counter)
#         if code in self.code_to_url:
#             raise ValueError(f"Alias '{code}' already taken")
#         self._counter += 1
#         self.url_to_code[long_url] = code
#         self.code_to_url[code] = long_url
#         return code
#
#     def resolve(self, code: str) -> Optional[str]:
#         return self.code_to_url.get(code)
#
# shortener = URLShortener()
# code = shortener.shorten("https://www.example.com/very/long/url?with=params")
# print(f"Short code: {code}")
# print(f"Resolves to: {shortener.resolve(code)}")
#
# Interview follow-ups to answer:
#   1. How do you handle 10K QPS on resolve? (Redis cache, CDN for redirects)
#   2. What if the same long URL is submitted twice? (deduplicate in url_to_code)
#   3. How do you handle custom aliases that collide? (409 Conflict)
#   4. Analytics: how do you count clicks without slowing down redirects? (async Kafka)


# =============================================================================
# DESIGN 2: Rate Limiter
# =============================================================================
# Requirements:
#   Functional:  limit requests per user per time window, return 429 on exceed
#   Non-functional: <5ms overhead, distributed (multiple servers), precise
#
# Algorithms (know all 4):
#   Token Bucket:    allow bursts up to capacity, smooth refill — AWS, Stripe
#   Leaky Bucket:    queue requests, process at fixed rate — even output
#   Fixed Window:    count in current minute — simple but edge case at boundaries
#   Sliding Window:  most accurate — track timestamps of last N seconds
#
# Already implemented in 05_api_design.py. Here, focus on distributed rate limiting:
#
# Distributed rate limiter using Redis (the production approach):
#
# class DistributedRateLimiter:
#     """Uses Redis atomic INCR + EXPIRE for distributed rate limiting."""
#
#     def __init__(self, redis_client, limit: int, window_seconds: int):
#         self.redis = redis_client
#         self.limit = limit
#         self.window = window_seconds
#
#     def allow(self, user_id: str) -> tuple[bool, int]:
#         """Returns (allowed: bool, remaining: int)"""
#         window = int(time.time()) // self.window
#         key = f"rate:{user_id}:{window}"
#         pipe = self.redis.pipeline()
#         pipe.incr(key)
#         pipe.expire(key, self.window * 2)   # TTL buffer
#         count, _ = pipe.execute()
#         remaining = max(0, self.limit - count)
#         return count <= self.limit, remaining
#
# Interview follow-ups:
#   1. Race condition: two servers both see count=99, both increment to 100 — both allowed.
#      Fix: Lua script (atomic check-and-increment) or Redis INCR (already atomic)
#   2. What headers do you return? X-RateLimit-Limit, X-RateLimit-Remaining, Retry-After
#   3. Different limits for free vs paid users? (store tier in user metadata)


# =============================================================================
# DESIGN 3: Key-Value Store (like Redis)
# =============================================================================
# Requirements:
#   Functional:  get(key), put(key, value), delete(key), TTL support
#   Non-functional: <1ms latency, 10K QPS, survive restarts (persistence)
#
# Architecture:
#   - In-memory hash map for O(1) access
#   - WAL or snapshot for persistence (see 02_database_internals.py)
#   - Single-threaded event loop (Redis model) to avoid lock contention
#
# TODO: Build a minimal in-memory KV store with TTL
#
# class KVStore:
#     def __init__(self):
#         self._data:   dict[str, bytes] = {}
#         self._expiry: dict[str, float] = {}   # key → expiry timestamp
#
#     def get(self, key: str) -> Optional[bytes]:
#         if key in self._expiry and time.time() > self._expiry[key]:
#             del self._data[key]
#             del self._expiry[key]
#             return None
#         return self._data.get(key)
#
#     def set(self, key: str, value: bytes, ttl_seconds: Optional[int] = None) -> None:
#         self._data[key] = value
#         if ttl_seconds is not None:
#             self._expiry[key] = time.time() + ttl_seconds
#         elif key in self._expiry:
#             del self._expiry[key]
#
#     def delete(self, key: str) -> bool:
#         existed = key in self._data
#         self._data.pop(key, None)
#         self._expiry.pop(key, None)
#         return existed
#
#     def dbsize(self) -> int:
#         return len(self._data)


# =============================================================================
# DESIGN 4: Notification System
# =============================================================================
# Requirements:
#   Functional:  send push/SMS/email to users, support 10M notifications/day
#   Non-functional: soft real-time (< 5 seconds), at-least-once delivery
#
# Architecture:
#   API → Message Queue (Kafka) → Worker Pool → Provider (FCM, Twilio, SendGrid)
#   Retry logic with exponential backoff for failed sends.
#
# TODO: Implement the retry worker with exponential backoff
#
# @dataclass
# class Notification:
#     id: str
#     user_id: int
#     channel: str        # "push" | "sms" | "email"
#     content: str
#     attempts: int = 0
#     max_attempts: int = 3
#
# class NotificationWorker:
#     MAX_DELAY = 300   # 5 minutes max backoff
#
#     def _get_delay(self, attempt: int) -> float:
#         """Exponential backoff: 2^attempt seconds + jitter."""
#         return min(2 ** attempt + random.uniform(0, 1), self.MAX_DELAY)
#
#     def send(self, notif: Notification, provider) -> bool:
#         for attempt in range(notif.max_attempts):
#             try:
#                 provider.send(notif.channel, notif.user_id, notif.content)
#                 return True
#             except Exception as e:
#                 if attempt < notif.max_attempts - 1:
#                     delay = self._get_delay(attempt)
#                     print(f"Attempt {attempt+1} failed, retrying in {delay:.1f}s")
#                     time.sleep(delay)
#         print(f"Notification {notif.id} failed after {notif.max_attempts} attempts → DLQ")
#         return False


# =============================================================================
# DESIGN 5: Design Twitter/X Timeline (the hard one)
# =============================================================================
# Requirements:
#   Functional:  post tweet, follow user, view home timeline (50 most recent tweets from following)
#   Non-functional: 300M users, 500M tweets/day, timeline <200ms
#
# Two approaches:
#
# Fan-out on write (push model):
#   When user A tweets → pre-compute and push to all followers' timeline caches
#   ✅ Timeline read is instant (pre-computed)
#   ❌ Celebrity with 50M followers → 50M cache writes per tweet
#
# Fan-out on read (pull model):
#   When user loads timeline → query all followed users' recent tweets and merge
#   ✅ Simple, works for celebrities
#   ❌ 200 following × DB query per load = slow
#
# Twitter's actual approach: HYBRID
#   Normal users (<10K followers): fan-out on write
#   Celebrities (>10K followers): fan-out on read, merged with cached timeline
#
# TODO: Implement a basic timeline with fan-out on write
#
# class TwitterTimeline:
#     def __init__(self):
#         self.tweets: dict[int, list[dict]] = defaultdict(list)      # user_id → their tweets
#         self.following: dict[int, set[int]] = defaultdict(set)       # user_id → set of followed user_ids
#         self.timelines: dict[int, deque] = defaultdict(lambda: deque(maxlen=800))  # user_id → cached timeline
#
#     def post_tweet(self, user_id: int, content: str) -> dict:
#         tweet = {"id": int(time.time() * 1000), "user_id": user_id,
#                  "content": content, "created_at": time.time()}
#         self.tweets[user_id].append(tweet)
#         # Fan-out: push to all followers' timeline caches
#         for follower_id in self._get_followers(user_id):
#             self.timelines[follower_id].appendleft(tweet)
#         return tweet
#
#     def follow(self, follower_id: int, followee_id: int) -> None:
#         self.following[follower_id].add(followee_id)
#
#     def get_timeline(self, user_id: int, limit: int = 20) -> list[dict]:
#         return list(self.timelines[user_id])[:limit]
#
#     def _get_followers(self, user_id: int) -> list[int]:
#         return [uid for uid, following in self.following.items() if user_id in following]


# =============================================================================
# DESIGN 6: Distributed Cache (like Memcached cluster)
# =============================================================================
# Already covered in 01_fundamentals.py (consistent hashing) and 03_caching.py.
# Interview angle: how do you ensure high availability?
#
# Replication: each cache node has a replica. Writes go to both, reads from primary.
# If primary goes down: replica promoted, consistent hash ring updated.
#
# Cache cluster (combine consistent hashing + LRU from earlier files):
# class CacheCluster:
#     def __init__(self, nodes: list[str], replicas_per_node: int = 150):
#         self.ring = ConsistentHashRing(replicas=replicas_per_node)
#         self.caches: dict[str, LRUCache] = {}
#         for node in nodes:
#             self.ring.add_server(node)
#             self.caches[node] = LRUCache(capacity=10_000)
#
#     def get(self, key: str) -> Optional[int]:
#         node = self.ring.get_server(key)
#         return self.caches[node].get(hash(key))
#
#     def set(self, key: str, value: int) -> None:
#         node = self.ring.get_server(key)
#         self.caches[node].put(hash(key), value)


# =============================================================================
# DESIGN 7: Design a Chat System (like WhatsApp/Slack)
# =============================================================================
# Requirements:
#   Functional:  1-on-1 messaging, group chats, online presence, message history
#   Non-functional: <100ms delivery, 50M DAU, messages stored 5 years
#
# Architecture decisions:
#   Transport: WebSocket (persistent connection) — not HTTP polling
#   Message ID: Snowflake ID (sortable, distributed)
#   Storage: Cassandra (write-heavy, wide rows for message history per chat)
#   Presence: Redis (user_id → last_seen timestamp, expire after 30s)
#
# TODO: Implement a Snowflake-like ID generator (timestamp + machine + sequence)
#
# class SnowflakeIDGenerator:
#     """41-bit timestamp | 10-bit machine ID | 12-bit sequence"""
#     EPOCH = 1700000000000   # custom epoch (ms) — Nov 2023
#
#     def __init__(self, machine_id: int):
#         assert 0 <= machine_id < 1024
#         self.machine_id = machine_id
#         self._sequence = 0
#         self._last_ts = -1
#         self._lock = threading.Lock()
#
#     def generate(self) -> int:
#         with self._lock:
#             ts = int(time.time() * 1000) - self.EPOCH
#             if ts == self._last_ts:
#                 self._sequence = (self._sequence + 1) & 0xFFF   # 12-bit wrap
#                 if self._sequence == 0:
#                     while ts <= self._last_ts:   # spin until next ms
#                         ts = int(time.time() * 1000) - self.EPOCH
#             else:
#                 self._sequence = 0
#             self._last_ts = ts
#             return (ts << 22) | (self.machine_id << 12) | self._sequence
#
# gen = SnowflakeIDGenerator(machine_id=1)
# ids = [gen.generate() for _ in range(5)]
# print("Snowflake IDs (sortable):", ids)
# assert ids == sorted(ids), "IDs must be monotonically increasing!"


if __name__ == "__main__":
    print("System Design Interview Problems — implement TODOs above")
    print("\nDesigns covered:")
    designs = [
        "1. URL Shortener",
        "2. Rate Limiter",
        "3. Key-Value Store",
        "4. Notification System",
        "5. Twitter Timeline (fan-out on write/read)",
        "6. Distributed Cache",
        "7. Chat System + Snowflake ID",
    ]
    for d in designs:
        print(f"   {d}")
