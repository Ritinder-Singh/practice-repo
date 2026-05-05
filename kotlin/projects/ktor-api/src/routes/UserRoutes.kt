// PROJECT: Ktor User Routes

// TODO 1: Extension function on Application or Route:
//   fun Application.configureRouting() {
//       routing { userRoutes() }
//   }

// TODO 2: Route group for /users:
//   fun Route.userRoutes() {
//       val userRepo = UserRepository()
//       route("/users") {
//           get { /* return all */ }
//           get("{id}") { /* return one */ }
//           post { /* create */ }
//           put("{id}") { /* update */ }
//           delete("{id}") { /* delete */ }
//       }
//   }

// TODO 3: Response helpers:
//   - call.respond(HttpStatusCode.OK, users)
//   - call.respond(HttpStatusCode.NotFound, mapOf("error" to "User not found"))
//   - call.respond(HttpStatusCode.Created, newUser)

// TODO 4: Request parsing:
//   val user = call.receive<CreateUserRequest>()
//   val id = call.parameters["id"]?.toIntOrNull() ?: return@get call.respond(HttpStatusCode.BadRequest)
