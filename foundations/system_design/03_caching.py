# =============================================================================
# System Design — Caching & CDN
# =============================================================================
# Topics: LRU/LFU eviction, cache-aside/read-through/write-through,
#         TTL, cache stampede, Redis data structures, consistent hash sharding.
# Run: python 03_caching.py
# Ref: https://redis.io/docs/latest/
#      ByteByteGo — "A Crash Course in Caching"
# =============================================================================

import time
from collections import OrderedDict
from typing import Optional, Any


# =============================================================================
# TODO 1: LRU Cache (LeetCode #146 — must know cold)
# =============================================================================
# Least Recently Used — evict the item that was accessed longest ago.
# Constraint: O(1) get AND put.
# Classic solution: doubly linked list + hash map (Python: OrderedDict).
#
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache: OrderedDict[int, int] = OrderedDict()
#
#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
#         self.cache.move_to_end(key)   # mark as most recently used
#         return self.cache[key]
#
#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.cache.move_to_end(key)
#         self.cache[key] = value
#         if len(self.cache) > self.capacity:
#             self.cache.popitem(last=False)   # evict least recently used (front)
#
# cache = LRUCache(3)
# cache.put(1, 1); cache.put(2, 2); cache.put(3, 3)
# cache.get(1)          # access 1 → now most recent
# cache.put(4, 4)       # evicts 2 (least recently used)
# assert cache.get(2) == -1   # evicted
# assert cache.get(1) == 1    # still there


# =============================================================================
# TODO 2: LFU Cache — Least Frequently Used (harder)
# =============================================================================
# LFU evicts the item with the lowest access frequency.
# Tie-break: evict the least recently used among items with same frequency.
# Used by Redis when maxmemory-policy = allkeys-lfu.
#
# class LFUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.min_freq = 0
#         self.key_to_val:  dict[int, int] = {}
#         self.key_to_freq: dict[int, int] = {}
#         self.freq_to_keys: dict[int, OrderedDict] = defaultdict(OrderedDict)
#
#     def _update_freq(self, key: int) -> None:
#         freq = self.key_to_freq[key]
#         self.key_to_freq[key] = freq + 1
#         del self.freq_to_keys[freq][key]
#         if not self.freq_to_keys[freq] and self.min_freq == freq:
#             self.min_freq += 1
#         self.freq_to_keys[freq + 1][key] = None
#
#     def get(self, key: int) -> int:
#         if key not in self.key_to_val:
#             return -1
#         self._update_freq(key)
#         return self.key_to_val[key]
#
#     def put(self, key: int, value: int) -> None:
#         if self.capacity <= 0:
#             return
#         if key in self.key_to_val:
#             self.key_to_val[key] = value
#             self._update_freq(key)
#             return
#         if len(self.key_to_val) >= self.capacity:
#             evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
#             del self.key_to_val[evict_key]
#             del self.key_to_freq[evict_key]
#         self.key_to_val[key] = value
#         self.key_to_freq[key] = 1
#         self.freq_to_keys[1][key] = None
#         self.min_freq = 1


# =============================================================================
# TODO 3: TTL Cache — time-based expiry
# =============================================================================
# Keys expire after a TTL (time-to-live) in seconds.
# Used for: session tokens, API response caching, rate limit windows.
#
# class TTLCache:
#     def __init__(self, default_ttl: int = 60):
#         self.default_ttl = default_ttl
#         self._store: dict[str, tuple[Any, float]] = {}  # key → (value, expiry_ts)
#
#     def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
#         expiry = time.time() + (ttl or self.default_ttl)
#         self._store[key] = (value, expiry)
#
#     def get(self, key: str) -> Optional[Any]:
#         if key not in self._store:
#             return None
#         value, expiry = self._store[key]
#         if time.time() > expiry:
#             del self._store[key]
#             return None   # expired
#         return value
#
#     def delete(self, key: str) -> None:
#         self._store.pop(key, None)
#
# cache = TTLCache(default_ttl=2)
# cache.set("session:abc", {"user_id": 1})
# print(cache.get("session:abc"))   # {"user_id": 1}
# time.sleep(3)
# print(cache.get("session:abc"))   # None — expired


# =============================================================================
# TODO 4: Cache stampede / thundering herd — prevention
# =============================================================================
# Problem: A popular cached item expires. 10,000 requests simultaneously
# get a cache miss and all hammer the database at once.
#
# Solution A — Locking (mutex per key):
# def get_with_lock(key: str) -> Any:
#     value = cache.get(key)
#     if value is not None:
#         return value
#     lock_key = f"lock:{key}"
#     with distributed_lock(lock_key, timeout=5):
#         # re-check after acquiring lock — another process may have set it
#         value = cache.get(key)
#         if value is None:
#             value = db.query(key)
#             cache.set(key, value, ttl=300)
#     return value
#
# Solution B — Probabilistic Early Expiration (XFetch):
# Better: stochastically refresh the cache before it expires — no lock needed.
# def get_xfetch(key: str, beta: float = 1.0) -> Any:
#     value, delta, expiry = cache.get_with_metadata(key)
#     # delta = time it took to compute the value last time
#     # Refresh early if: current_time >= expiry - delta * beta * log(random())
#     if time.time() >= expiry - delta * beta * (-math.log(random.random())):
#         value = db.query(key)
#         cache.set(key, value, ttl=300)
#     return value
#
# EXERCISE: Simulate a cache stampede:
#   1. Set a cache entry with TTL=1 second
#   2. Spin up 100 threads that all call get() simultaneously after TTL expires
#   3. Count how many threads hit the DB (should be 100 without fix)
#   4. Add a threading.Lock per key and repeat — should be 1 DB hit


# =============================================================================
# TODO 5: Caching strategies — know the trade-offs
# =============================================================================
# Cache-Aside (Lazy Loading):
#   Read: check cache → if miss, read DB, write to cache, return
#   Write: write to DB, then INVALIDATE the cache key (not update)
#   ✅ Only caches data that's actually requested
#   ❌ Cache miss penalty (3 round trips), possible stale data
#
# Read-Through:
#   Cache sits in front of DB — app only talks to cache.
#   On miss, cache itself fetches from DB and stores result.
#   ✅ Simpler application code
#   ❌ Cold start: first request always misses
#
# Write-Through:
#   Every write goes to cache AND DB synchronously.
#   ✅ Cache always consistent with DB
#   ❌ Write latency penalty, cache may fill with data never read
#
# Write-Behind (Write-Back):
#   Write to cache immediately, async write to DB later.
#   ✅ Lowest write latency
#   ❌ Data loss if cache goes down before DB write
#
# EXERCISE: For each use case, pick a strategy and justify:
#   1. User profile page (read-heavy, writes rare)
#   2. Shopping cart (frequent writes, low loss tolerance)
#   3. News feed (pre-computed, heavy reads)
#   4. Bank balance (every write must persist immediately)
#
# strategy_choices = {
#     "user_profile": {"strategy": "cache_aside", "reason": "..."},
#     ...
# }


# =============================================================================
# TODO 6: Redis data structures — pick the right one
# =============================================================================
# Implement each pattern (use redis-py or mentally trace the commands):
#
# import redis
# r = redis.Redis()
#
# 1. Session store (STRING):
#    r.setex(f"session:{token}", 3600, json.dumps(user_data))
#    data = json.loads(r.get(f"session:{token}"))
#
# 2. Rate limiter (STRING + INCR):
#    count = r.incr(f"rate:{user_id}:{window}")
#    if count == 1: r.expire(f"rate:{user_id}:{window}", 60)
#    if count > 100: raise RateLimitError()
#
# 3. Leaderboard (SORTED SET):
#    r.zadd("leaderboard", {"player:1": 1500, "player:2": 2300})
#    top10 = r.zrevrange("leaderboard", 0, 9, withscores=True)
#
# 4. Pub/Sub notification:
#    Publisher: r.publish("new-order", json.dumps(order))
#    Subscriber: pubsub = r.pubsub(); pubsub.subscribe("new-order")
#
# 5. Distributed lock (SET NX EX):
#    acquired = r.set(f"lock:{resource}", "1", nx=True, ex=30)
#    if not acquired: raise LockError("Resource locked")
#    try: do_work()
#    finally: r.delete(f"lock:{resource}")


if __name__ == "__main__":
    print("Caching & CDN — implement TODOs above")
