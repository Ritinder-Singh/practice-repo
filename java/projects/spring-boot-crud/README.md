# Spring Boot CRUD REST API

## Setup

```bash
# Option 1: Spring Initializr CLI
curl https://start.spring.io/starter.zip \
  -d dependencies=web,data-jpa,postgresql,lombok,validation \
  -d type=maven-project \
  -d language=java \
  -d bootVersion=3.2.0 \
  -d artifactId=crud-api \
  -o crud-api.zip
unzip crud-api.zip && cd crud-api

# Option 2: start.spring.io browser → generate
```

## What to Build

### Milestone 1 — Entity + Repository
- [ ] `User` entity: `@Entity`, `@Id @GeneratedValue`, fields: id, name, email, createdAt
- [ ] `UserRepository extends JpaRepository<User, Long>` — free CRUD + custom queries
- [ ] Configure `application.properties`: datasource URL, username, password, `ddl-auto=update`

### Milestone 2 — Service Layer
- [ ] `UserService` with `@Service` — business logic, `@Transactional`
- [ ] Custom exception: `UserNotFoundException extends RuntimeException`

### Milestone 3 — REST Controller
- [ ] `GET /api/users` — return all users
- [ ] `GET /api/users/{id}` — return one or 404
- [ ] `POST /api/users` — create with `@Valid @RequestBody`
- [ ] `PUT /api/users/{id}` — update
- [ ] `DELETE /api/users/{id}` — delete

### Milestone 4 — Exception Handling
- [ ] `@ControllerAdvice` `GlobalExceptionHandler`
- [ ] Handle `MethodArgumentNotValidException`, `UserNotFoundException`
- [ ] Return `ProblemDetail` (Spring 6) or custom `ErrorResponse`

### Milestone 5 — Advanced
- [ ] Pagination: `Pageable` parameter, `Page<User>` response
- [ ] Spring Security: JWT authentication for all endpoints
- [ ] Docker Compose: `docker-compose.yml` with postgres + app services
