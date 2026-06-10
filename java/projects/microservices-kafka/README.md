# Microservices with Spring Cloud + Kafka

## Architecture

```
[API Gateway (Spring Cloud Gateway)]
        |
   ┌────┴────┐
   ▼         ▼
[order-service]  [inventory-service]
       |               |
       └──── Kafka ────┘
             Topic: order-events
```

## Setup

```bash
# Start infrastructure
docker-compose up -d  # kafka, zookeeper, postgres, eureka

# Each service: spring init with dependencies
# order-service: web, data-jpa, kafka, eureka-client, cloud-gateway
# inventory-service: web, data-jpa, kafka, eureka-client
```

## What to Build

### order-service
- [ ] `POST /orders` — create order, publish `OrderCreatedEvent` to Kafka topic `order-events`
- [ ] `GET /orders/{id}` — fetch order status
- [ ] `@KafkaListener` on `inventory-confirmed` → update order status to CONFIRMED
- [ ] Saga pattern: compensate on failure (publish `OrderCancelledEvent`)

### inventory-service
- [ ] `@KafkaListener` on `order-events` → check stock, reduce if available
- [ ] Publish `InventoryConfirmedEvent` or `InventoryFailedEvent`
- [ ] `GET /inventory/{productId}` — current stock level

### API Gateway
- [ ] Spring Cloud Gateway routes: `/api/orders/**` → order-service, `/api/inventory/**` → inventory-service
- [ ] Rate limiting with Redis
- [ ] JWT validation filter

### Eureka Service Discovery
- [ ] `@EnableEurekaServer` standalone service
- [ ] Each service: `@EnableEurekaClient`, `eureka.client.serviceUrl.defaultZone=http://localhost:8761/eureka`

### Docker Compose
- [ ] `docker-compose.yml`: kafka (confluentinc/cp-kafka), zookeeper, postgres (x2), eureka, order-service, inventory-service

## Key Concepts Demonstrated

| Concept | Where |
|---------|-------|
| Event-driven architecture (publish / subscribe) | `order-service` publishes → Kafka → `inventory-service` consumes |
| Kafka topic producer and consumer (`@KafkaListener`) | `order-service`, `inventory-service` |
| Saga pattern for distributed transactions | `order-service` compensating `OrderCancelledEvent` |
| Service discovery with Eureka | `@EnableEurekaServer` + `@EnableEurekaClient` on each service |
| API Gateway routing (Spring Cloud Gateway) | Gateway routes `/api/orders/**` → `order-service` |
| JWT validation at the gateway layer | API Gateway filter |
| Redis-backed rate limiting | API Gateway |
| Docker Compose for multi-service orchestration | `docker-compose.yml` |
