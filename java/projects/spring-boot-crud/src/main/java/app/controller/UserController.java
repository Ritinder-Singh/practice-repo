package app.controller;

// PROJECT: Spring Boot User Controller
//
// TODO 1: Add class-level annotations:
//   @RestController
//   @RequestMapping("/api/users")
//   @RequiredArgsConstructor   (Lombok)
//
// TODO 2: Inject UserService via constructor injection
//
// TODO 3: GET /api/users → List<UserDto>
//   @GetMapping
//   public ResponseEntity<List<UserDto>> getAllUsers() { ... }
//
// TODO 4: GET /api/users/{id} → UserDto or 404
//   @GetMapping("/{id}")
//   public ResponseEntity<UserDto> getUserById(@PathVariable Long id) { ... }
//
// TODO 5: POST /api/users → 201 Created with Location header
//   @PostMapping
//   public ResponseEntity<UserDto> createUser(@Valid @RequestBody CreateUserRequest req) { ... }
//
// TODO 6: PUT /api/users/{id} → updated UserDto
//   @PutMapping("/{id}")
//   public ResponseEntity<UserDto> updateUser(@PathVariable Long id, @RequestBody UpdateUserRequest req) { ... }
//
// TODO 7: DELETE /api/users/{id} → 204 No Content
//   @DeleteMapping("/{id}")
//   public ResponseEntity<Void> deleteUser(@PathVariable Long id) { ... }

public class UserController {
    // stub
}
