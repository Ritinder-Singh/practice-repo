# Spring Boot CRUD REST API

A fully working REST API for managing users, built with Spring Boot 3, Spring Data JPA, and an H2 in-memory database. Built as a learning project to understand the three-layer architecture of a Spring Boot application.

---

## Architecture

Every HTTP request passes through three layers in order:

```
HTTP Request
     │
     ▼
┌─────────────┐
│  Controller │  Handles routes, parses request/response, delegates to service
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Service   │  Business logic, transactions, converts entities ↔ DTOs
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Repository  │  Talks to the database — SQL is generated automatically
└──────┬──────┘
       │
       ▼
  H2 Database
```

Each layer only talks to the layer directly below it. The controller never touches the database.

---

## Project Structure

```
src/main/java/app/
├── Application.java                  # Entry point — boots the Spring app
│
├── model/
│   └── User.java                     # @Entity — maps to the "users" table
│
├── repository/
│   └── UserRepository.java           # JpaRepository — free CRUD + custom queries
│
├── service/
│   └── UserService.java              # Business logic, @Transactional
│
├── controller/
│   └── UserController.java           # REST endpoints, HTTP request/response
│
├── dto/
│   ├── UserDto.java                  # Response shape (what the API returns)
│   ├── CreateUserRequest.java        # POST body shape
│   └── UpdateUserRequest.java        # PUT body shape
│
└── exception/
    ├── UserNotFoundException.java    # Thrown when a user id doesn't exist
    └── GlobalExceptionHandler.java   # Maps exceptions to HTTP error responses
```

---

## Key Concepts

**Why DTOs?**
We never expose raw `User` entities in API responses. DTOs (`UserDto`, `CreateUserRequest`, etc.) decouple the API contract from the database schema. If you rename a DB column, the API stays the same.

**Why a Service layer?**
Keeps business logic out of the controller. The controller's only job is HTTP — parsing requests and returning responses.

**Why `JpaRepository`?**
Spring Data JPA generates SQL from method names (derived queries) and provides `save()`, `findById()`, `deleteById()`, etc. for free — no SQL needed for basic operations.

**Why `@Transactional`?**
Wraps a method in a database transaction. If anything throws, the DB rolls back automatically — no partial writes.

---

## Running the App

**Prerequisites:** Java 17+, Maven

```bash
mvn spring-boot:run
```

The app starts on `http://localhost:8080`.

The H2 browser console (for inspecting the DB) is available at `http://localhost:8080/h2-console`.
Use JDBC URL: `jdbc:h2:mem:testdb`, leave username/password blank.

---

## API Endpoints

| Method | Path | Description | Status |
|--------|------|-------------|--------|
| GET | `/api/users` | Get all users | 200 |
| GET | `/api/users/{id}` | Get user by id | 200 / 404 |
| POST | `/api/users` | Create a user | 201 |
| PUT | `/api/users/{id}` | Update a user | 200 / 404 |
| DELETE | `/api/users/{id}` | Delete a user | 204 / 404 |

---

## Example Requests

```bash
# Create a user
curl -s -X POST http://localhost:8080/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com"}' | jq

# Get all users
curl -s http://localhost:8080/api/users | jq

# Get user by id
curl -s http://localhost:8080/api/users/1 | jq

# Update a user
curl -s -X PUT http://localhost:8080/api/users/1 \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice Smith"}' | jq

# Delete a user
curl -s -X DELETE http://localhost:8080/api/users/1

# Trigger a 404
curl -s http://localhost:8080/api/users/999 | jq

# Trigger a 400 (validation failure)
curl -s -X POST http://localhost:8080/api/users \
  -H "Content-Type: application/json" \
  -d '{"name":"","email":"notanemail"}' | jq
```

---

## Dependencies

| Dependency | Purpose |
|---|---|
| `spring-boot-starter-web` | Embedded Tomcat, REST controllers |
| `spring-boot-starter-data-jpa` | JPA/Hibernate, repository layer |
| `spring-boot-starter-validation` | Bean Validation (`@NotBlank`, `@Email`) |
| `h2` | In-memory database — zero setup |
| `lombok` | Eliminates boilerplate (`@Getter`, `@Setter`, `@RequiredArgsConstructor`) |

---

## Key Concepts Demonstrated

| Concept | Where |
|---------|-------|
| Three-layer architecture (Controller → Service → Repository) | `controller/UserController.java` → `service/UserService.java` → `repository/UserRepository.java` |
| Spring Data JPA derived queries | `repository/UserRepository.java` |
| `@Transactional` and automatic rollback | `service/UserService.java` |
| DTO pattern (decoupling API contract from DB schema) | `dto/UserDto.java`, `dto/CreateUserRequest.java`, `dto/UpdateUserRequest.java` |
| Bean Validation (`@NotBlank`, `@Email`) on request DTOs | `dto/CreateUserRequest.java` |
| Constructor injection via Lombok `@RequiredArgsConstructor` | `service/UserService.java`, `controller/UserController.java` |
| Centralised exception handling with `@RestControllerAdvice` | `exception/GlobalExceptionHandler.java` |
| `@PrePersist` lifecycle hook for auto-timestamps | `model/User.java` |
| H2 in-memory database (zero-setup dev DB) | `src/main/resources/application.properties` |
| RFC 9457 `ProblemDetail` structured error responses | `exception/GlobalExceptionHandler.java` |
