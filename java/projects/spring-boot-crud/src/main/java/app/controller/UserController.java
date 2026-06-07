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

// @RestController = @Controller + @ResponseBody — every method return value is written as JSON automatically.
// @RequestMapping("/api/users") prefixes all routes in this class with /api/users.
// @RequiredArgsConstructor injects UserService via constructor (same pattern as the service layer).
@RestController
@RequestMapping("/api/users")
@RequiredArgsConstructor
public class UserController {

  private final UserService userService;

  // GET /api/users — returns all users. 200 OK with a JSON array.
  @GetMapping
  public ResponseEntity<List<UserDto>> getAll() {
    return ResponseEntity.ok(userService.findAll());
  }

  // GET /api/users/{id} — @PathVariable pulls the {id} segment out of the URL.
  // Returns 200 with the user, or throws UserNotFoundException (caught by GlobalExceptionHandler → 404).
  @GetMapping("/{id}")
  public ResponseEntity<UserDto> getById(@PathVariable Long id) {
    return ResponseEntity.ok(userService.findById(id));
  }

  // POST /api/users — @RequestBody deserializes the JSON body into a CreateUserRequest.
  // @Valid triggers Bean Validation (@NotBlank, @Email) on the request object.
  // Returns 201 Created with a Location header pointing to the new resource.
  @PostMapping
  public ResponseEntity<UserDto> create(@Valid @RequestBody CreateUserRequest req) {
    UserDto created = userService.create(req);
    return ResponseEntity.created(URI.create("/api/users/" + created.id())).body(created);
  }

  // PUT /api/users/{id} — updates an existing user. Returns 200 with the updated user.
  @PutMapping("/{id}")
  public ResponseEntity<UserDto> update(@PathVariable Long id, @RequestBody UpdateUserRequest req) {
    return ResponseEntity.ok(userService.update(id, req));
  }

  // DELETE /api/users/{id} — deletes the user. Returns 204 No Content (success with no body).
  @DeleteMapping("/{id}")
  public ResponseEntity<Void> delete(@PathVariable Long id) {
    userService.delete(id);
    return ResponseEntity.noContent().build();
  }
}