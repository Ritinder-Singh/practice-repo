# =============================================================================
# System Design — Fundamentals
# =============================================================================
# Topics: consistent hashing, horizontal vs vertical scaling, CAP theorem,
#         load balancing strategies, stateless services, back-of-envelope math.
# Run: python 01_fundamentals.py
# Ref: https://github.com/donnemartin/system-design-primer
#      ByteByteGo — System Design playlist
# =============================================================================

import hashlib
import bisect
from collections import defaultdict


# =============================================================================
# TODO 1: Consistent Hash Ring
# =============================================================================
# Problem: You have N cache servers. You want to distribute keys across them
# such that when a server is added/removed, only ~1/N keys need to be remapped
# (vs. naive modulo hashing which remaps ALL keys).
#
# Implementation:
#   - Place servers on a virtual ring of 2^32 positions
#   - Each server gets `replicas` virtual nodes (reduces hotspots)
#   - A key maps to the first server clockwise from its hash position
#
# class ConsistentHashRing:
#     def __init__(self, replicas: int = 150):
#         self.replicas = replicas
#         self.ring: dict[int, str] = {}      # position → server name
#         self.sorted_keys: list[int] = []
#
#     def _hash(self, key: str) -> int:
#         return int(hashlib.md5(key.encode()).hexdigest(), 16) % (2**32)
#
#     def add_server(self, server: str) -> None:
#         for i in range(self.replicas):
#             pos = self._hash(f"{server}:{i}")
#             self.ring[pos] = server
#             bisect.insort(self.sorted_keys, pos)
#
#     def remove_server(self, server: str) -> None:
#         for i in range(self.replicas):
#             pos = self._hash(f"{server}:{i}")
#             del self.ring[pos]
#             self.sorted_keys.remove(pos)
#
#     def get_server(self, key: str) -> str:
#         if not self.ring:
#             raise ValueError("No servers in ring")
#         pos = self._hash(key)
#         idx = bisect.bisect_right(self.sorted_keys, pos) % len(self.sorted_keys)
#         return self.ring[self.sorted_keys[idx]]
#
# After implementing:
# ring = ConsistentHashRing(replicas=150)
# for s in ["server-A", "server-B", "server-C"]:
#     ring.add_server(s)
#
# keys = [f"user:{i}" for i in range(1000)]
# distribution = defaultdict(int)
# for k in keys:
#     distribution[ring.get_server(k)] += 1
# print("Distribution before adding server-D:", dict(distribution))
#
# ring.add_server("server-D")
# remapped = sum(1 for k in keys if ring.get_server(k) != distribution_before[k])
# print(f"Keys remapped after adding server-D: {remapped}/1000")
# Goal: ~250 keys remapped (1/4), not all 1000


# =============================================================================
# TODO 2: Load Balancer Strategies
# =============================================================================
# Implement three load balancing algorithms and compare their key distributions.
#
# class RoundRobinBalancer:
#     def __init__(self, servers: list[str]):
#         self.servers = servers
#         self._idx = 0
#
#     def get_server(self) -> str:
#         server = self.servers[self._idx % len(self.servers)]
#         self._idx += 1
#         return server
#
# class WeightedRoundRobinBalancer:
#     """Higher weight = more requests routed to that server."""
#     def __init__(self, servers: dict[str, int]):  # {"server": weight}
#         self.pool = [s for s, w in servers.items() for _ in range(w)]
#         self._idx = 0
#
#     def get_server(self) -> str:
#         server = self.pool[self._idx % len(self.pool)]
#         self._idx += 1
#         return server
#
# class LeastConnectionsBalancer:
#     """Route to server with fewest active connections."""
#     def __init__(self, servers: list[str]):
#         self.connections: dict[str, int] = {s: 0 for s in servers}
#
#     def get_server(self) -> str:
#         return min(self.connections, key=self.connections.get)
#
#     def release(self, server: str) -> None:
#         self.connections[server] = max(0, self.connections[server] - 1)


# =============================================================================
# TODO 3: Back-of-Envelope Calculations
# =============================================================================
# Practice estimating system capacity. Know these numbers cold.
#
# LATENCY NUMBERS (approximate):
#   L1 cache reference:           0.5 ns
#   L2 cache reference:           7 ns
#   Main memory reference:        100 ns
#   SSD random read:              150 µs
#   Network round trip (same DC): 0.5 ms
#   HDD seek:                     10 ms
#   Network round trip (cross-DC):150 ms
#
# THROUGHPUT NUMBERS:
#   SSD sequential read:          500 MB/s
#   Network bandwidth (1Gbps):    125 MB/s
#   Postgres (simple reads):      ~10,000 QPS per instance
#   Redis:                        ~100,000 QPS
#
# EXERCISE: Design capacity for a URL shortener (like bit.ly)
#   Assumptions:
#     - 100M URLs created/day
#     - 10:1 read:write ratio → 1B reads/day
#     - Average URL length: 100 bytes
#     - 5-year retention
#
#   Calculate:
#   writes_per_second = 100_000_000 / 86_400   # ≈ 1,157 writes/sec
#   reads_per_second  = 1_000_000_000 / 86_400  # ≈ 11,574 reads/sec
#   storage_5yr       = 100_000_000 * 365 * 5 * 100  # bytes → convert to TB
#   cache_storage     = reads_per_second * 0.20 * 100  # 20% hot data cached
#
#   print(f"Writes/sec: {writes_per_second:.0f}")
#   print(f"Reads/sec:  {reads_per_second:.0f}")
#   print(f"Storage 5yr: {storage_5yr / 1e12:.1f} TB")
#
# Repeat for: Twitter timeline, WhatsApp messages, Netflix video streaming


# =============================================================================
# TODO 4: CAP Theorem — classify real systems
# =============================================================================
# A distributed system can guarantee only 2 of 3:
#   C — Consistency:  every read gets the latest write (or an error)
#   A — Availability: every request gets a response (not necessarily latest)
#   P — Partition tolerance: system works despite network splits
#
# In practice P is non-negotiable (networks DO partition), so the real choice is:
#   CP (sacrifice availability): strong consistency — Zookeeper, HBase, etcd
#   AP (sacrifice consistency):  high availability — Cassandra, DynamoDB, CouchDB
#
# EXERCISE: For each scenario, state CP or AP and justify:
#   1. Bank account balance — what's the consequence of a stale read?
#   2. Shopping cart contents — is it OK to show slightly stale data?
#   3. DNS resolution — does every client need the absolute latest record?
#   4. Distributed config store (etcd) — what breaks if config is inconsistent?
#   5. Social media likes count — strict accuracy or high availability?
#
# Write your answers:
# scenarios = {
#     "bank_balance": {"choice": "CP", "reason": "..."},
#     "shopping_cart": {"choice": "AP", "reason": "..."},
#     "dns": {"choice": "AP", "reason": "..."},
#     "config_store": {"choice": "CP", "reason": "..."},
#     "likes_count": {"choice": "AP", "reason": "..."},
# }


# =============================================================================
# TODO 5: Stateless vs Stateful — session handling
# =============================================================================
# Stateless servers are easy to scale (any server can handle any request).
# Stateful servers require sticky sessions or shared state.
#
# Implement two approaches to session storage:
#
# Approach A — Server-side session (stateful, bad for scaling):
# sessions: dict[str, dict] = {}
#
# def create_session(user_id: int) -> str:
#     session_id = secrets.token_urlsafe(32)
#     sessions[session_id] = {"user_id": user_id, "created_at": time.time()}
#     return session_id
#
# Problem: if request hits server-2 but session is on server-1 → 401 Unauthorized
#
# Approach B — JWT (stateless — any server can verify):
# import jwt, time
#
# SECRET = "your-secret-key"
#
# def create_jwt(user_id: int) -> str:
#     payload = {"user_id": user_id, "exp": time.time() + 3600}
#     return jwt.encode(payload, SECRET, algorithm="HS256")
#
# def verify_jwt(token: str) -> dict:
#     return jwt.decode(token, SECRET, algorithms=["HS256"])
#
# Trade-off: JWTs can't be revoked (until expiry) without a blocklist.
# When does a blocklist make sense? When would you still prefer server sessions?


if __name__ == "__main__":
    print("System Design Fundamentals — implement TODOs above")
    print("Run each section independently as you study it.")
