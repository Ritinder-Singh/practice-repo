# =============================================================================
# System Design — Database Internals
# =============================================================================
# Topics: B-tree vs LSM-tree, Write-Ahead Log (WAL), MVCC, Bloom filters,
#         read/write amplification, compaction strategies.
# Run: python 02_database_internals.py
# Ref: "Designing Data-Intensive Applications" — Kleppmann (chapters 3, 7)
#      CMU 15-445 lectures: https://youtube.com/@CMUDatabaseGroup
# =============================================================================

import struct
import os
import time
import hashlib
from dataclasses import dataclass, field
from typing import Optional


# =============================================================================
# TODO 1: Bitcask-style Log-Structured Key-Value Store
# =============================================================================
# Bitcask (used in Riak): append-only log + in-memory hash index.
# All writes go to the end of a log file. No in-place updates.
# Reads: look up byte offset in memory, seek directly — O(1).
# Crash recovery: replay log file to rebuild the in-memory index.
#
# class BitcaskStore:
#     def __init__(self, path: str):
#         self.path = path
#         self.index: dict[str, int] = {}   # key → byte offset in log file
#         self.log = open(path, "ab+")
#         self._rebuild_index()
#
#     def _encode(self, key: str, value: str) -> bytes:
#         k = key.encode()
#         v = value.encode()
#         # Format: [key_len: 4 bytes][val_len: 4 bytes][key][value]
#         return struct.pack(">II", len(k), len(v)) + k + v
#
#     def _decode_at(self, offset: int) -> tuple[str, str]:
#         with open(self.path, "rb") as f:
#             f.seek(offset)
#             k_len, v_len = struct.unpack(">II", f.read(8))
#             key = f.read(k_len).decode()
#             val = f.read(v_len).decode()
#             return key, val
#
#     def set(self, key: str, value: str) -> None:
#         offset = self.log.tell()
#         self.log.write(self._encode(key, value))
#         self.log.flush()
#         self.index[key] = offset
#
#     def get(self, key: str) -> Optional[str]:
#         if key not in self.index:
#             return None
#         _, val = self._decode_at(self.index[key])
#         return val
#
#     def delete(self, key: str) -> None:
#         self.set(key, "__TOMBSTONE__")   # tombstone marker
#         del self.index[key]
#
#     def _rebuild_index(self) -> None:
#         """Replay log from disk to rebuild the in-memory index."""
#         pass  # TODO: implement
#
# store = BitcaskStore("/tmp/bitcask.log")
# store.set("name", "Ritinder")
# store.set("role", "SDE")
# print(store.get("name"))   # "Ritinder"
# store.set("name", "Ritinder Singh")
# print(store.get("name"))   # "Ritinder Singh" — latest wins


# =============================================================================
# TODO 2: Bloom Filter — probabilistic membership check
# =============================================================================
# Used in: LSM-tree (avoid disk reads for missing keys), Redis (key existence),
#          Cassandra (reduce read amplification).
# Properties: no false negatives, small false positive rate.
# Space: ~10 bits/element for 1% false positive rate.
#
# class BloomFilter:
#     def __init__(self, capacity: int, error_rate: float = 0.01):
#         import math
#         self.size = int(-capacity * math.log(error_rate) / (math.log(2) ** 2))
#         self.hash_count = int(self.size / capacity * math.log(2))
#         self.bits = bytearray(self.size // 8 + 1)
#
#     def _hashes(self, item: str) -> list[int]:
#         results = []
#         for i in range(self.hash_count):
#             h = int(hashlib.md5(f"{i}:{item}".encode()).hexdigest(), 16)
#             results.append(h % self.size)
#         return results
#
#     def add(self, item: str) -> None:
#         for pos in self._hashes(item):
#             self.bits[pos // 8] |= (1 << (pos % 8))
#
#     def might_contain(self, item: str) -> bool:
#         return all(
#             self.bits[pos // 8] & (1 << (pos % 8))
#             for pos in self._hashes(item)
#         )
#
# bf = BloomFilter(capacity=1000)
# for key in ["user:1", "user:2", "user:3"]:
#     bf.add(key)
# print(bf.might_contain("user:1"))    # True (definitely in set)
# print(bf.might_contain("user:999")) # False (probably not, could be false positive)


# =============================================================================
# TODO 3: Write-Ahead Log (WAL) — crash recovery
# =============================================================================
# Rule: write to log BEFORE modifying data. If crash during write:
#   - Replay WAL on restart → recover to consistent state
#   - Used by: PostgreSQL, SQLite, RocksDB, etcd
#
# @dataclass
# class WALEntry:
#     lsn: int          # log sequence number (monotonically increasing)
#     operation: str    # "SET" or "DELETE"
#     key: str
#     value: str
#     committed: bool = False
#
# class WriteAheadLog:
#     def __init__(self, path: str):
#         self.path = path
#         self.lsn = 0
#         self._log: list[WALEntry] = []
#         self._restore()
#
#     def append(self, op: str, key: str, value: str = "") -> WALEntry:
#         self.lsn += 1
#         entry = WALEntry(lsn=self.lsn, operation=op, key=key, value=value)
#         self._log.append(entry)
#         self._persist(entry)   # fsync to disk before returning
#         return entry
#
#     def commit(self, lsn: int) -> None:
#         for entry in self._log:
#             if entry.lsn == lsn:
#                 entry.committed = True
#                 break
#
#     def recover(self) -> list[WALEntry]:
#         """Return committed entries to replay on startup."""
#         return [e for e in self._log if e.committed]
#
#     def _persist(self, entry: WALEntry) -> None:
#         pass  # TODO: serialize to file and fsync
#
#     def _restore(self) -> None:
#         pass  # TODO: deserialize log from disk


# =============================================================================
# TODO 4: MVCC — Multi-Version Concurrency Control
# =============================================================================
# MVCC allows readers to see a consistent snapshot without blocking writers.
# Each row has a version. Readers see the latest committed version at their
# transaction start time. Writers create new versions, not overwrites.
# Used by: PostgreSQL, MySQL InnoDB, CockroachDB.
#
# @dataclass
# class RowVersion:
#     value: str
#     created_txn: int   # transaction ID that created this version
#     deleted_txn: int   # transaction ID that deleted this version (0 = not deleted)
#
# class MVCCTable:
#     def __init__(self):
#         self.data: dict[str, list[RowVersion]] = defaultdict(list)
#         self.current_txn = 0
#
#     def begin_transaction(self) -> int:
#         self.current_txn += 1
#         return self.current_txn
#
#     def write(self, txn_id: int, key: str, value: str) -> None:
#         # Mark old versions as deleted by this transaction
#         for v in self.data[key]:
#             if v.deleted_txn == 0:
#                 v.deleted_txn = txn_id
#         self.data[key].append(RowVersion(value=value, created_txn=txn_id, deleted_txn=0))
#
#     def read(self, txn_id: int, key: str) -> Optional[str]:
#         # Find the version visible to this transaction (created before txn_id, not yet deleted)
#         for v in reversed(self.data.get(key, [])):
#             if v.created_txn <= txn_id and (v.deleted_txn == 0 or v.deleted_txn > txn_id):
#                 return v.value
#         return None


# =============================================================================
# TODO 5: B-Tree vs LSM-Tree — trade-off analysis
# =============================================================================
# Understand the read/write amplification trade-off:
#
# B-Tree (PostgreSQL, MySQL):
#   ✅ Fast reads: O(log N) — navigate tree directly
#   ✅ Good for range queries (leaf nodes linked)
#   ❌ Write amplification: must update pages in-place (random I/O)
#   ❌ Fragmentation — pages become partially empty over time
#
# LSM-Tree (RocksDB, Cassandra, LevelDB):
#   ✅ Fast writes: sequential append to MemTable → flush to SSTable
#   ✅ High write throughput — no random I/O on writes
#   ❌ Read amplification: may need to check multiple SSTables + bloom filters
#   ❌ Compaction cost — background merge of SSTables consumes I/O
#
# EXERCISE: For each workload, choose B-Tree or LSM-Tree and justify:
#   1. Time-series sensor data (100K writes/sec, rarely read)
#   2. User profile lookups (50/50 reads and writes, point lookups)
#   3. E-commerce product catalog (mostly reads, infrequent writes)
#   4. Event log storage (append-only, occasional range scan)
#
# workload_choices = {
#     "time_series":     {"choice": "LSM", "reason": "high write throughput, sequential appends"},
#     "user_profiles":   {"choice": "???", "reason": "???"},
#     "product_catalog": {"choice": "???", "reason": "???"},
#     "event_log":       {"choice": "???", "reason": "???"},
# }


if __name__ == "__main__":
    print("Database Internals — implement TODOs above")
