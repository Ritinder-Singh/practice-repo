# =============================================================================
# System Design — Messaging & Queues
# =============================================================================
# Topics: message queues vs pub-sub, at-least-once delivery, dead-letter queues,
#         Kafka partitions/offsets, backpressure, CQRS, Outbox pattern.
# Run: python 04_messaging_queues.py
# Ref: https://kafka.apache.org/documentation/
#      "Designing Event-Driven Systems" — Confluent (free book)
# =============================================================================

import threading
import queue
import time
import json
import uuid
from dataclasses import dataclass, field
from typing import Callable, Optional
from collections import defaultdict


# =============================================================================
# TODO 1: In-memory message queue (baseline)
# =============================================================================
# Build a simple thread-safe queue with producer/consumer pattern.
# Demonstrates: why we need queues (decouple producers from slow consumers).
#
# @dataclass
# class Message:
#     id: str = field(default_factory=lambda: str(uuid.uuid4()))
#     payload: dict = field(default_factory=dict)
#     attempts: int = 0
#     created_at: float = field(default_factory=time.time)
#
# class SimpleQueue:
#     def __init__(self, maxsize: int = 0):
#         self._q: queue.Queue[Message] = queue.Queue(maxsize=maxsize)
#
#     def publish(self, payload: dict) -> Message:
#         msg = Message(payload=payload)
#         self._q.put(msg)
#         return msg
#
#     def consume(self, timeout: float = 1.0) -> Optional[Message]:
#         try:
#             return self._q.get(timeout=timeout)
#         except queue.Empty:
#             return None
#
#     def ack(self) -> None:
#         self._q.task_done()
#
# EXERCISE: Simulate order processing
# q = SimpleQueue()
#
# def producer():
#     for i in range(20):
#         msg = q.publish({"order_id": i, "amount": i * 10})
#         print(f"Published order {i}")
#         time.sleep(0.05)   # produce at 20/sec
#
# def consumer(worker_id: int):
#     while True:
#         msg = q.consume(timeout=2.0)
#         if msg is None:
#             break
#         time.sleep(0.15)   # simulate slow DB write (consume at ~7/sec)
#         print(f"Worker-{worker_id} processed order {msg.payload['order_id']}")
#         q.ack()
#
# Observation: without 3 workers, queue backs up — why? Producer is 3x faster.


# =============================================================================
# TODO 2: Dead Letter Queue — handle failed messages
# =============================================================================
# Messages that fail after max_retries are moved to a DLQ for inspection.
# Prevents poison pills from blocking the entire queue.
#
# class QueueWithDLQ:
#     MAX_RETRIES = 3
#
#     def __init__(self):
#         self.main = queue.Queue()
#         self.dlq: list[Message] = []
#
#     def publish(self, payload: dict) -> None:
#         self.main.put(Message(payload=payload))
#
#     def process(self, handler: Callable[[Message], None]) -> None:
#         while not self.main.empty():
#             msg = self.main.get()
#             try:
#                 handler(msg)
#             except Exception as e:
#                 msg.attempts += 1
#                 if msg.attempts < self.MAX_RETRIES:
#                     print(f"Retry {msg.attempts}/{self.MAX_RETRIES} for {msg.id}")
#                     self.main.put(msg)   # re-queue for retry
#                 else:
#                     print(f"Moving {msg.id} to DLQ after {self.MAX_RETRIES} failures")
#                     self.dlq.append(msg)
#             finally:
#                 self.main.task_done()
#
# q = QueueWithDLQ()
# q.publish({"type": "email", "to": "valid@example.com"})
# q.publish({"type": "email", "to": "INVALID_EMAIL"})   # will fail 3x → DLQ
#
# def send_email(msg: Message):
#     if "@" not in msg.payload["to"]:
#         raise ValueError(f"Invalid email: {msg.payload['to']}")
#     print(f"Email sent to {msg.payload['to']}")
#
# q.process(send_email)
# print(f"DLQ contents: {[m.payload for m in q.dlq]}")


# =============================================================================
# TODO 3: Pub/Sub — one publisher, many subscribers
# =============================================================================
# Unlike a queue (one consumer per message), pub/sub delivers to ALL subscribers.
# Used for: notifications, event broadcasting, microservice integration.
#
# class PubSubBroker:
#     def __init__(self):
#         self._subscribers: dict[str, list[Callable]] = defaultdict(list)
#
#     def subscribe(self, topic: str, handler: Callable[[dict], None]) -> None:
#         self._subscribers[topic].append(handler)
#
#     def publish(self, topic: str, event: dict) -> None:
#         for handler in self._subscribers.get(topic, []):
#             threading.Thread(target=handler, args=(event,), daemon=True).start()
#
# broker = PubSubBroker()
#
# broker.subscribe("order.created", lambda e: print(f"Inventory: reserve {e['product_id']}"))
# broker.subscribe("order.created", lambda e: print(f"Email: notify {e['user_email']}"))
# broker.subscribe("order.created", lambda e: print(f"Analytics: track conversion"))
#
# broker.publish("order.created", {
#     "order_id": "ord_123",
#     "product_id": "prod_456",
#     "user_email": "user@example.com",
# })
# All 3 handlers fire independently for the same event.


# =============================================================================
# TODO 4: Kafka concepts — simulate partition/offset model
# =============================================================================
# Kafka guarantees: ordered delivery WITHIN a partition, not across partitions.
# Partition key determines which partition a message lands in.
# Consumer groups: each message processed by exactly one consumer in the group.
#
# class KafkaPartition:
#     """Single Kafka partition — append-only log."""
#     def __init__(self, partition_id: int):
#         self.id = partition_id
#         self.log: list[dict] = []
#
#     def append(self, message: dict) -> int:
#         offset = len(self.log)
#         self.log.append({"offset": offset, "message": message, "timestamp": time.time()})
#         return offset
#
#     def read_from(self, offset: int, max_records: int = 10) -> list[dict]:
#         return self.log[offset: offset + max_records]
#
# class SimpleTopic:
#     def __init__(self, name: str, num_partitions: int = 3):
#         self.name = name
#         self.partitions = [KafkaPartition(i) for i in range(num_partitions)]
#
#     def _select_partition(self, key: Optional[str]) -> KafkaPartition:
#         if key is None:
#             # round-robin when no key (no ordering guarantee)
#             return self.partitions[int(time.time() * 1000) % len(self.partitions)]
#         # hash-based — same key always goes to same partition (ordering guarantee)
#         return self.partitions[hash(key) % len(self.partitions)]
#
#     def produce(self, message: dict, key: Optional[str] = None) -> tuple[int, int]:
#         partition = self._select_partition(key)
#         offset = partition.append(message)
#         return partition.id, offset
#
# topic = SimpleTopic("orders", num_partitions=3)
# # Orders for same user always go to same partition → preserve per-user ordering
# for i in range(10):
#     p, o = topic.produce({"order_id": i}, key="user:42")
# print("All user:42 orders should be on same partition — verify:")
# # They should all be on partition hash("user:42") % 3


# =============================================================================
# TODO 5: Outbox Pattern — guaranteed message delivery
# =============================================================================
# Problem: You write to DB and then publish to Kafka.
# If Kafka publish fails AFTER DB write → message lost.
# If Kafka publish fails BEFORE DB write → duplicate on retry.
#
# Solution — Outbox Pattern:
#   1. Write your main record AND an outbox event to DB in ONE transaction
#   2. A separate process (or Debezium CDC) reads the outbox table and publishes
#   3. Mark outbox event as published in DB
#
# class OutboxRepository:
#     """Simulates DB operations with an outbox table."""
#
#     def create_order_with_event(self, order: dict) -> None:
#         with db.transaction():
#             order_id = db.insert("orders", order)
#             db.insert("outbox_events", {
#                 "event_type": "order.created",
#                 "payload": json.dumps({**order, "order_id": order_id}),
#                 "published": False,
#                 "created_at": time.time(),
#             })
#         # If anything above fails → both rolled back. Atomicity guaranteed.
#
#     def get_unpublished_events(self) -> list[dict]:
#         return db.query("SELECT * FROM outbox_events WHERE published = FALSE ORDER BY created_at LIMIT 100")
#
#     def mark_published(self, event_id: int) -> None:
#         db.execute("UPDATE outbox_events SET published = TRUE WHERE id = ?", [event_id])
#
# class OutboxPublisher:
#     """Polls outbox table and publishes to Kafka. Runs as a background process."""
#     def run(self):
#         while True:
#             events = repo.get_unpublished_events()
#             for event in events:
#                 kafka.produce(event["event_type"], json.loads(event["payload"]))
#                 repo.mark_published(event["id"])
#             time.sleep(1)


# =============================================================================
# TODO 6: Backpressure — don't let producers overwhelm consumers
# =============================================================================
# When consumers are slower than producers, the queue grows unboundedly.
# Solutions: bounded queue (block producer), drop messages, sample messages.
#
# EXERCISE: Observe backpressure in action.
#
# BOUNDED_QUEUE = queue.Queue(maxsize=10)   # bounded — producer blocks when full
#
# def fast_producer():
#     for i in range(100):
#         BOUNDED_QUEUE.put({"event": i})   # blocks if queue full
#         print(f"Produced {i}")
#
# def slow_consumer():
#     while True:
#         item = BOUNDED_QUEUE.get()
#         time.sleep(0.1)   # 10/sec — slower than producer
#         print(f"Consumed {item['event']}")
#         BOUNDED_QUEUE.task_done()
#
# threading.Thread(target=fast_producer).start()
# threading.Thread(target=slow_consumer).start()
#
# Observation: producer slows to match consumer speed — natural backpressure.
# In Kafka: consumers control their own read rate (pull model, not push).


if __name__ == "__main__":
    print("Messaging & Queues — implement TODOs above")
