# =============================================================================
# Redis — Client Patterns in Python
# =============================================================================
# Topics: strings, hashes, lists, sets, sorted sets, pub/sub,
#         TTL/expiry, caching patterns, rate limiting, session storage.
# Run: python redis_client.py  (requires: pip install redis)
# Ref: Resume — Redis (Databases), caching in system_design/03_caching.py
# =============================================================================

import json
import time
import hashlib
from typing import Optional, Any
from functools import wraps

# import redis
# r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)


# =============================================================================
# MOCK CLIENT (runs without Redis installed)
# =============================================================================

class MockRedis:
    """Stand-in for redis.Redis — same interface, in-memory dict."""

    def __init__(self):
        self._store: dict = {}
        self._expiry: dict = {}
        self._lists: dict = {}
        self._sets: dict = {}
        self._zsets: dict = {}  # sorted sets: key → {member: score}

    def _is_expired(self, key: str) -> bool:
        exp = self._expiry.get(key)
        if exp and time.time() > exp:
            self._store.pop(key, None)
            self._expiry.pop(key, None)
            return True
        return False

    # Strings
    def set(self, key: str, value: Any, ex: Optional[int] = None) -> bool:
        self._store[key] = str(value)
        if ex:
            self._expiry[key] = time.time() + ex
        return True

    def get(self, key: str) -> Optional[str]:
        return None if self._is_expired(key) else self._store.get(key)

    def delete(self, *keys: str) -> int:
        return sum(1 for k in keys if self._store.pop(k, None) is not None)

    def exists(self, key: str) -> int:
        return 0 if self._is_expired(key) else (1 if key in self._store else 0)

    def incr(self, key: str, amount: int = 1) -> int:
        val = int(self._store.get(key, 0)) + amount
        self._store[key] = str(val)
        return val

    def expire(self, key: str, seconds: int) -> bool:
        self._expiry[key] = time.time() + seconds
        return True

    def ttl(self, key: str) -> int:
        exp = self._expiry.get(key)
        if not exp:
            return -1
        remaining = int(exp - time.time())
        return max(0, remaining)

    # Hashes
    def hset(self, name: str, mapping: dict) -> int:
        if name not in self._store:
            self._store[name] = {}
        self._store[name].update(mapping)
        return len(mapping)

    def hget(self, name: str, key: str) -> Optional[str]:
        return self._store.get(name, {}).get(key)

    def hgetall(self, name: str) -> dict:
        return dict(self._store.get(name, {}))

    # Lists
    def lpush(self, name: str, *values: Any) -> int:
        self._lists.setdefault(name, [])
        for v in values:
            self._lists[name].insert(0, str(v))
        return len(self._lists[name])

    def lrange(self, name: str, start: int, end: int) -> list:
        lst = self._lists.get(name, [])
        return lst[start: None if end == -1 else end + 1]

    def llen(self, name: str) -> int:
        return len(self._lists.get(name, []))

    # Sorted sets
    def zadd(self, name: str, mapping: dict) -> int:
        self._zsets.setdefault(name, {})
        self._zsets[name].update(mapping)
        return len(mapping)

    def zrange(self, name: str, start: int, end: int, withscores: bool = False, rev: bool = False):
        zset = self._zsets.get(name, {})
        sorted_members = sorted(zset.items(), key=lambda x: x[1], reverse=rev)
        sliced = sorted_members[start: None if end == -1 else end + 1]
        if withscores:
            return [(m, s) for m, s in sliced]
        return [m for m, _ in sliced]

    def zincrby(self, name: str, amount: float, value: str) -> float:
        self._zsets.setdefault(name, {})
        self._zsets[name][value] = self._zsets[name].get(value, 0) + amount
        return self._zsets[name][value]

    def pipeline(self):
        return MockPipeline(self)


class MockPipeline:
    def __init__(self, client: MockRedis):
        self._client = client
        self._commands: list = []

    def incr(self, key: str):
        self._commands.append(("incr", key))
        return self

    def expire(self, key: str, seconds: int):
        self._commands.append(("expire", key, seconds))
        return self

    def execute(self):
        results = []
        for cmd in self._commands:
            fn = getattr(self._client, cmd[0])
            results.append(fn(*cmd[1:]))
        return results


r = MockRedis()


# =============================================================================
# 1. CACHING PATTERN — Cache-Aside
# =============================================================================

def cache_aside(key: str, ttl: int, fetch_fn):
    """Read from cache; on miss, fetch and populate."""
    cached = r.get(key)
    if cached:
        print(f"  [CACHE HIT] {key}")
        return json.loads(cached)
    print(f"  [CACHE MISS] {key} — fetching from source")
    data = fetch_fn()
    r.set(key, json.dumps(data), ex=ttl)
    return data


def cache_result(ttl: int = 300):
    """Decorator: cache function return value in Redis."""
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            key = f"{fn.__name__}:{hashlib.md5(str(args).encode()).hexdigest()[:8]}"
            return cache_aside(key, ttl, lambda: fn(*args, **kwargs))
        return wrapper
    return decorator


@cache_result(ttl=60)
def get_user_profile(user_id: int) -> dict:
    """Simulates DB fetch."""
    return {"id": user_id, "name": "Ritinder", "role": "SDE"}


# =============================================================================
# 2. SESSION STORAGE (Hash per session)
# =============================================================================

class SessionStore:
    SESSION_TTL = 3600  # 1 hour

    @staticmethod
    def create(session_id: str, user_data: dict):
        r.hset(f"session:{session_id}", mapping=user_data)
        r.expire(f"session:{session_id}", SessionStore.SESSION_TTL)

    @staticmethod
    def get(session_id: str) -> dict:
        return r.hgetall(f"session:{session_id}")

    @staticmethod
    def destroy(session_id: str):
        r.delete(f"session:{session_id}")

    @staticmethod
    def refresh(session_id: str):
        r.expire(f"session:{session_id}", SessionStore.SESSION_TTL)


# =============================================================================
# 3. RATE LIMITING — Sliding Window Counter
# =============================================================================

def is_rate_limited(client_id: str, limit: int = 10, window_sec: int = 60) -> bool:
    """
    Fixed window rate limiter using INCR + EXPIRE.
    For sliding window, use ZADD with timestamps.
    """
    key = f"ratelimit:{client_id}:{int(time.time()) // window_sec}"
    pipe = r.pipeline()
    pipe.incr(key)
    pipe.expire(key, window_sec)
    count, _ = pipe.execute()
    return int(count) > limit


# =============================================================================
# 4. LEADERBOARD — Sorted Set
# =============================================================================

class Leaderboard:
    def __init__(self, name: str):
        self.key = f"leaderboard:{name}"

    def add_score(self, user: str, score: float):
        r.zadd(self.key, {user: score})

    def increment(self, user: str, delta: float):
        r.zincrby(self.key, delta, user)

    def top_n(self, n: int = 10) -> list[tuple[str, float]]:
        return r.zrange(self.key, 0, n - 1, withscores=True, rev=True)


# =============================================================================
# 5. JOB QUEUE — List as Queue (FIFO)
# =============================================================================

class JobQueue:
    """Simple FIFO queue using Redis lists. Production: use Celery + Redis broker."""

    def __init__(self, name: str):
        self.key = f"queue:{name}"

    def enqueue(self, job: dict):
        r.lpush(self.key, json.dumps(job))

    def peek(self, count: int = 5) -> list[dict]:
        return [json.loads(j) for j in r.lrange(self.key, 0, count - 1)]

    def size(self) -> int:
        return r.llen(self.key)


# =============================================================================
# DEMO
# =============================================================================

if __name__ == "__main__":
    print("=== Cache-Aside Pattern ===")
    profile = get_user_profile(42)
    print(f"  First call: {profile}")
    profile2 = get_user_profile(42)
    print(f"  Second call (cached): {profile2}")

    print("\n=== Session Storage ===")
    SessionStore.create("sess_abc123", {"user_id": "42", "role": "admin"})
    print(f"  Session: {SessionStore.get('sess_abc123')}")
    print(f"  TTL: {r.ttl('session:sess_abc123')}s")

    print("\n=== Rate Limiting ===")
    for i in range(12):
        limited = is_rate_limited("user_42", limit=10, window_sec=60)
        print(f"  Request {i+1}: {'BLOCKED' if limited else 'OK'}")

    print("\n=== Leaderboard ===")
    lb = Leaderboard("monthly_calls")
    lb.add_score("alice", 850)
    lb.add_score("bob", 920)
    lb.add_score("carol", 780)
    lb.increment("alice", 50)
    print(f"  Top 3: {lb.top_n(3)}")

    print("\n=== Job Queue ===")
    q = JobQueue("transcription")
    q.enqueue({"file": "call_001.mp3", "priority": "high"})
    q.enqueue({"file": "call_002.mp3", "priority": "normal"})
    print(f"  Queue size: {q.size()}")
    print(f"  Peek: {q.peek()}")

    # TODO: Replace MockRedis with real redis.Redis client
    # TODO: Add pub/sub pattern (notification system)
    # TODO: Add distributed lock (SET key value NX EX 30)
