# =============================================================================
# System Design — Microservices & Patterns
# =============================================================================
# Topics: circuit breaker, service discovery, health checks, saga pattern,
#         strangler fig, observability (traces/metrics/logs).
# Run: python 06_microservices.py
# Ref: https://microservices.io/patterns
#      https://martinfowler.com/articles/microservices.html
# =============================================================================

import time
import random
import threading
from enum import Enum
from dataclasses import dataclass, field
from collections import deque
from typing import Callable, Optional


# =============================================================================
# TODO 1: Circuit Breaker
# =============================================================================
# Problem: Service A calls Service B. Service B is down.
# Without circuit breaker: every request to A times out waiting for B → cascade failure.
# With circuit breaker: after N failures, stop calling B entirely for a cooldown period.
#
# States:
#   CLOSED    → requests flow normally (circuit is "closed"/connected)
#   OPEN      → requests fail fast, no calls to downstream service
#   HALF_OPEN → one probe request allowed — if succeeds, close; if fails, re-open
#
# class CircuitBreakerState(Enum):
#     CLOSED = "closed"
#     OPEN = "open"
#     HALF_OPEN = "half_open"
#
# class CircuitBreaker:
#     def __init__(self, failure_threshold: int = 5,
#                  recovery_timeout: float = 30.0,
#                  success_threshold: int = 2):
#         self.failure_threshold = failure_threshold
#         self.recovery_timeout = recovery_timeout
#         self.success_threshold = success_threshold
#         self.state = CircuitBreakerState.CLOSED
#         self.failure_count = 0
#         self.success_count = 0
#         self.last_failure_time: Optional[float] = None
#         self._lock = threading.Lock()
#
#     def call(self, func: Callable, *args, **kwargs):
#         with self._lock:
#             if self.state == CircuitBreakerState.OPEN:
#                 if time.time() - self.last_failure_time > self.recovery_timeout:
#                     self.state = CircuitBreakerState.HALF_OPEN
#                     self.success_count = 0
#                 else:
#                     raise Exception("Circuit OPEN — failing fast")
#         try:
#             result = func(*args, **kwargs)
#             self._on_success()
#             return result
#         except Exception:
#             self._on_failure()
#             raise
#
#     def _on_success(self) -> None:
#         with self._lock:
#             if self.state == CircuitBreakerState.HALF_OPEN:
#                 self.success_count += 1
#                 if self.success_count >= self.success_threshold:
#                     self.state = CircuitBreakerState.CLOSED
#                     self.failure_count = 0
#             elif self.state == CircuitBreakerState.CLOSED:
#                 self.failure_count = 0
#
#     def _on_failure(self) -> None:
#         with self._lock:
#             self.failure_count += 1
#             self.last_failure_time = time.time()
#             if self.failure_count >= self.failure_threshold:
#                 self.state = CircuitBreakerState.OPEN
#                 print(f"Circuit OPENED after {self.failure_count} failures")
#
# breaker = CircuitBreaker(failure_threshold=3, recovery_timeout=5.0)
#
# def flaky_service():
#     if random.random() < 0.7:   # 70% failure rate
#         raise ConnectionError("Service B unavailable")
#     return "OK"
#
# for i in range(10):
#     try:
#         result = breaker.call(flaky_service)
#         print(f"Request {i+1}: {result} | State: {breaker.state.value}")
#     except Exception as e:
#         print(f"Request {i+1}: FAILED ({e}) | State: {breaker.state.value}")
#     time.sleep(0.1)


# =============================================================================
# TODO 2: Service Registry & Discovery
# =============================================================================
# In microservices, service instances come and go (containers scale up/down).
# Service registry (like Consul, etcd, Eureka) tracks live instances.
# Clients discover instances at runtime — no hardcoded IPs.
#
# class ServiceRegistry:
#     def __init__(self):
#         self._services: dict[str, list[dict]] = {}   # name → [{host, port, healthy}]
#         self._lock = threading.Lock()
#
#     def register(self, name: str, host: str, port: int) -> str:
#         instance_id = f"{name}-{host}:{port}"
#         with self._lock:
#             if name not in self._services:
#                 self._services[name] = []
#             self._services[name].append({
#                 "id": instance_id, "host": host, "port": port,
#                 "healthy": True, "registered_at": time.time()
#             })
#         return instance_id
#
#     def deregister(self, name: str, instance_id: str) -> None:
#         with self._lock:
#             if name in self._services:
#                 self._services[name] = [i for i in self._services[name] if i["id"] != instance_id]
#
#     def get_instance(self, name: str) -> Optional[dict]:
#         """Round-robin load balance across healthy instances."""
#         with self._lock:
#             healthy = [i for i in self._services.get(name, []) if i["healthy"]]
#             if not healthy:
#                 return None
#             # Simple round-robin (track idx in real impl)
#             return healthy[int(time.time() * 1000) % len(healthy)]
#
#     def health_check(self, name: str, instance_id: str, healthy: bool) -> None:
#         with self._lock:
#             for inst in self._services.get(name, []):
#                 if inst["id"] == instance_id:
#                     inst["healthy"] = healthy
#
# registry = ServiceRegistry()
# registry.register("order-service", "10.0.1.1", 8080)
# registry.register("order-service", "10.0.1.2", 8080)
# registry.register("order-service", "10.0.1.3", 8080)
# # Simulate instance going down
# registry.health_check("order-service", "order-service-10.0.1.2:8080", healthy=False)
# instance = registry.get_instance("order-service")
# print(f"Routed to: {instance['host']}")  # Should never be 10.0.1.2


# =============================================================================
# TODO 3: Saga Pattern — distributed transactions
# =============================================================================
# Problem: No 2-phase commit across microservices. A "checkout" spans:
#   OrderService → PaymentService → InventoryService → NotificationService
# If InventoryService fails after payment succeeded, you need to compensate.
#
# Choreography Saga (event-driven, no central coordinator):
#   Each service listens for events and publishes its own.
#   OrderCreated → PaymentService charges → PaymentCompleted → InventoryService reserves
#   If PaymentFailed → OrderService cancels order (compensating transaction)
#
# @dataclass
# class SagaStep:
#     name: str
#     action: Callable      # forward action
#     compensate: Callable  # rollback action
#
# class Saga:
#     def __init__(self, steps: list[SagaStep]):
#         self.steps = steps
#         self.completed: list[SagaStep] = []
#
#     def execute(self, context: dict) -> bool:
#         for step in self.steps:
#             try:
#                 step.action(context)
#                 self.completed.append(step)
#                 print(f"✅ {step.name} succeeded")
#             except Exception as e:
#                 print(f"❌ {step.name} failed: {e}. Rolling back...")
#                 self._compensate(context)
#                 return False
#         return True
#
#     def _compensate(self, context: dict) -> None:
#         for step in reversed(self.completed):
#             try:
#                 step.compensate(context)
#                 print(f"↩️  {step.name} compensated")
#             except Exception as e:
#                 print(f"⚠️  Compensation failed for {step.name}: {e}")
#
# Implement a checkout saga with 4 steps:
# checkout_saga = Saga([
#     SagaStep("CreateOrder",         create_order,         cancel_order),
#     SagaStep("ChargePayment",       charge_payment,       refund_payment),
#     SagaStep("ReserveInventory",    reserve_inventory,    release_inventory),
#     SagaStep("SendConfirmation",    send_email,           lambda _: None),  # no compensation needed
# ])
# checkout_saga.execute({"user_id": 1, "product_id": "prod_abc", "amount": 99.99})


# =============================================================================
# TODO 4: Health Check Endpoint — /health and /ready
# =============================================================================
# Kubernetes and load balancers use these to know if a pod can receive traffic.
# /health (liveness):  Is the service alive? Restart if this fails.
# /ready (readiness):  Is the service ready for traffic? Remove from LB if false.
#
# Implement a health checker that verifies all dependencies:
#
# from fastapi import FastAPI
# app = FastAPI()
#
# async def check_postgres() -> bool:
#     try:
#         await db.execute("SELECT 1")
#         return True
#     except: return False
#
# async def check_redis() -> bool:
#     try:
#         await redis.ping()
#         return True
#     except: return False
#
# @app.get("/health")
# async def health():
#     return {"status": "ok"}   # Just alive check — always return 200 unless crashed
#
# @app.get("/ready")
# async def ready():
#     checks = {
#         "postgres": await check_postgres(),
#         "redis": await check_redis(),
#     }
#     all_ok = all(checks.values())
#     return JSONResponse(
#         status_code=200 if all_ok else 503,
#         content={"status": "ready" if all_ok else "not ready", "checks": checks}
#     )


# =============================================================================
# TODO 5: Strangler Fig — migrate monolith to microservices
# =============================================================================
# Don't rewrite everything at once. Gradually strangle the monolith.
#
# Phase 1: Put a proxy/gateway in front of the monolith.
#          Route ALL traffic through the gateway (no change yet).
#
# Phase 2: Extract ONE service (e.g., UserService).
#          Route /users/* to new UserService. All other traffic still to monolith.
#
# Phase 3: Repeat for next bounded context (e.g., OrderService).
#          Gateway routes /orders/* to OrderService. Monolith shrinks.
#
# Phase 4: Monolith handles nothing — decommission it.
#
# Simulate the gateway routing logic:
#
# ROUTES = {
#     "/users":   "http://user-service:8001",
#     "/orders":  "http://order-service:8002",
#     # everything else goes to the legacy monolith
#     "*":        "http://monolith:8000",
# }
#
# def route_request(path: str) -> str:
#     for prefix, target in ROUTES.items():
#         if prefix != "*" and path.startswith(prefix):
#             return f"{target}{path}"
#     return f"{ROUTES['*']}{path}"
#
# print(route_request("/users/42"))          # → user-service
# print(route_request("/orders/123/items"))  # → order-service
# print(route_request("/dashboard"))         # → monolith


if __name__ == "__main__":
    print("Microservices & Patterns — implement TODOs above")
