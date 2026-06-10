# Ktor REST API

## Setup

```bash
# Create a new Ktor project
curl -s "https://start.ktor.io/..." -o ktor-api.zip
# Or manually with Gradle:
# build.gradle.kts: add ktor-server-netty, ktor-server-content-negotiation, ktor-serialization-kotlinx-json
```

## What to Build

### Milestone 1 — Server Setup
- [ ] `embeddedServer(Netty, port = 8080) { ... }.start(wait = true)`
- [ ] Install `ContentNegotiation` plugin with `json()` serializer
- [ ] Install `StatusPages` for error handling
- [ ] Install `CallLogging` for request logs

### Milestone 2 — Routes
- [ ] `GET /users` — return all users as JSON array
- [ ] `GET /users/{id}` — return user or 404
- [ ] `POST /users` — create user from JSON body, return 201
- [ ] `PUT /users/{id}` — update user
- [ ] `DELETE /users/{id}` — delete, return 204

### Milestone 3 — Database (Exposed ORM)
- [ ] Add `exposed-core`, `exposed-dao`, `postgresql` driver deps
- [ ] Define `Users` object extending `IntIdTable`
- [ ] CRUD operations in a `UserRepository` class

### Milestone 4 — Authentication
- [ ] Add `ktor-server-auth-jwt` dependency
- [ ] `install(Authentication) { jwt("auth-jwt") { ... } }`
- [ ] Protect mutation routes with `authenticate("auth-jwt") { ... }`

## Key Concepts Demonstrated

| Concept | Where |
|---------|-------|
| `embeddedServer(Netty)` server bootstrap | `src/Application.kt` |
| Ktor routing DSL (`route`, `get`, `post`, `put`, `delete`) | `src/routes/UserRoutes.kt` |
| `ContentNegotiation` plugin with `kotlinx.json` serializer | `src/Application.kt` |
| `StatusPages` plugin for centralised error responses | Milestone 1 |
| `CallLogging` plugin for request logging | Milestone 1 |
| Exposed ORM `IntIdTable` + DAO pattern | Milestone 3 — `UserRepository` |
| JWT authentication plugin (`ktor-server-auth-jwt`) | Milestone 4 |
| `authenticate("auth-jwt")` route protection block | Milestone 4 |
