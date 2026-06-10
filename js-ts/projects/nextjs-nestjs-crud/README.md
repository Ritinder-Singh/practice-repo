# User CRUD — NextJS + NestJS (Monorepo)

## Architecture

```
[NextJS Frontend (JS)]  ──HTTP──►  [NestJS Backend (TS)]  ──ORM──►  [SQLite]
      port 3000                          port 3001
```

## Project Structure

```
nextjs-nestjs-crud/
├── frontend/                        # NextJS (JavaScript)
│   ├── package.json
│   ├── next.config.js
│   └── src/
│       ├── app/                     # App Router
│       │   └── users/
│       │       ├── page.js          # GET /users — list all users
│       │       └── [id]/
│       │           └── page.js      # GET /users/:id — user detail
│       ├── components/
│       │   └── UserCard.js          # Reusable user display component
│       └── services/
│           └── userService.js       # fetch() wrapper for all API calls
│
└── backend/                         # NestJS (TypeScript)
    ├── package.json
    ├── tsconfig.json
    └── src/
        ├── main.ts                  # Bootstrap app, CORS config, global filter
        ├── app.module.ts            # Root module — imports UsersModule
        └── users/
            ├── users.module.ts      # Wires together controller, service, repository
            ├── users.controller.ts  # @Controller('users') — HTTP route handlers
            ├── users.service.ts     # @Injectable() — business logic, calls repository
            ├── users.repository.ts  # DB queries via TypeORM EntityManager
            ├── entities/
            │   └── user.entity.ts   # @Entity() — maps to users table
            ├── dto/
            │   ├── create-user.dto.ts    # POST body: name, email (@IsNotEmpty, @IsEmail)
            │   ├── update-user.dto.ts    # PUT body: optional name, email
            │   └── user-response.dto.ts  # Response shape: id, name, email, createdAt
            └── exceptions/
                └── user-not-found.exception.ts  # extends NotFoundException
```

## Setup

```bash
# Backend
cd backend
npm install         # installs NestJS, TypeORM, sqlite3, class-validator
npm run start:dev   # runs on http://localhost:3001

# Frontend
cd frontend
npm install         # installs Next.js
npm run dev         # runs on http://localhost:3000
```

## API Endpoints (Backend)

| Method | Path         | Description              |
|--------|--------------|--------------------------|
| GET    | /users       | Return all users         |
| GET    | /users/:id   | Return one user (404 if missing) |
| POST   | /users       | Create user              |
| PUT    | /users/:id   | Update user (partial OK) |
| DELETE | /users/:id   | Delete user              |

## What to Build

### Backend (NestJS — TypeScript)
- [ ] `user.entity.ts` — `@Entity()` with `id`, `name`, `email`, `createdAt`; `@BeforeInsert()` to auto-set timestamp
- [ ] `create-user.dto.ts` — `@IsNotEmpty()` name, `@IsEmail()` email
- [ ] `update-user.dto.ts` — same fields but all optional (`@IsOptional()`)
- [ ] `user-response.dto.ts` — plain class with `id`, `name`, `email`, `createdAt`
- [ ] `user-not-found.exception.ts` — `extends NotFoundException`, message `"User not found: {id}"`
- [ ] `users.repository.ts` — `find()`, `findOne()`, `save()`, `delete()` via TypeORM
- [ ] `users.service.ts` — `findAll()`, `findById()`, `create()`, `update()`, `delete()`; maps entities → response DTOs; throws `UserNotFoundException`
- [ ] `users.controller.ts` — `@Get()`, `@Get(':id')`, `@Post()`, `@Put(':id')`, `@Delete(':id')`; uses `@UsePipes(ValidationPipe)` for DTO validation
- [ ] `users.module.ts` — `@Module()` importing TypeORM entity, providing service + repository
- [ ] `app.module.ts` — `TypeOrmModule.forRoot()` with SQLite + `synchronize: true` (dev only)
- [ ] `main.ts` — bootstrap, `app.enableCors()`, `app.useGlobalPipes(new ValidationPipe())`

### Frontend (NextJS — JavaScript)
- [ ] `userService.js` — `getUsers()`, `getUserById(id)`, `createUser(data)`, `updateUser(id, data)`, `deleteUser(id)` using `fetch()`
- [ ] `users/page.js` — Server Component that fetches and lists all users; link to detail page
- [ ] `users/[id]/page.js` — Server Component for user detail view
- [ ] `UserCard.js` — displays name, email, createdAt

## Key Concepts Demonstrated

| Concept | Where |
|---------|-------|
| NestJS `@Module()` wiring controller + service + repository | `users/users.module.ts` |
| TypeORM `@Entity()` + `@BeforeInsert()` lifecycle hook | `entities/user.entity.ts` |
| DTO validation with `class-validator` decorators | `dto/create-user.dto.ts`, `dto/update-user.dto.ts` |
| Global `ValidationPipe` for automatic DTO enforcement | `backend/src/main.ts` |
| Custom `NotFoundException` extension | `exceptions/user-not-found.exception.ts` |
| NestJS global exception filter | `common/filters/http-exception.filter.ts` |
| CORS configuration for cross-origin frontend | `backend/src/main.ts` |
| NextJS App Router server components | `frontend/src/app/users/page.js`, `[id]/page.js` |
| Fetch service abstraction layer (JS) | `frontend/src/services/userService.js` |
