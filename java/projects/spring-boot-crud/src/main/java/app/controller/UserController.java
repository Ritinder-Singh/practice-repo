package app.controller;

import app.dto.CreateUserRequest;
import app.dto.UpdateUserRequest;
import app.dto.UserDto;
import app.service.UserService;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.net.URI;
import java.util.List;
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

//public class UserController {
// stub
//}

@RestController
@RequestMapping("/api/users")
@RequiredArgsConstructor
public class UserController {

  private final UserService userService;

  @GetMapping
  public ResponseEntity<List<UserDto>> getAll() {
    return ResponseEntity.ok(userService.findAll());
  }

  @GetMapping("/{id}")
  public ResponseEntity<UserDto> getById(@PathVariable Long id) {
    return ResponseEntity.ok(userService.findById(id));
  }

  @PostMapping
  public ResponseEntity<UserDto> create(@Valid @RequestBody CreateUserRequest req) {
    UserDto created = userService.create(req);
    return ResponseEntity.created(URI.create("/api/users/" + created.id())).body(created);
  }

  @PutMapping("/{id}")
  public ResponseEntity<UserDto> update(@PathVariable Long id, @RequestBody UpdateUserRequest req) {
    return ResponseEntity.ok(userService.update(id, req));
  }

  @DeleteMapping("/{id}")
  public ResponseEntity<Void> delete(@PathVariable Long id) {
    userService.delete(id);
    return ResponseEntity.noContent().build();
  }
}
