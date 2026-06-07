package app.service;

import app.dto.CreateUserRequest;
import app.dto.UpdateUserRequest;
import app.dto.UserDto;
import app.exception.UserNotFoundException;
import app.model.User;
import app.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

// @Service marks this as a Spring-managed bean so it can be injected into other components.
// @RequiredArgsConstructor (Lombok) generates a constructor for all final fields —
// this is constructor injection, the preferred way to inject dependencies in Spring.
@Service
@RequiredArgsConstructor
public class UserService {

  // Spring injects UserRepository here via the constructor Lombok generated above.
  private final UserRepository userRepository;

  // findAll() fetches every row, converts each User entity to a UserDto using a stream,
  // and returns a List. We never expose raw entities to the outside world.
  public List<UserDto> findAll() {
    return userRepository.findAll().stream()
        .map(this::toDto)
        .toList();
  }

  // findById() returns an Optional<User> from the DB.
  // .map(this::toDto) converts it to UserDto if present.
  // .orElseThrow() throws UserNotFoundException if the id doesn't exist — becomes a 404.
  public UserDto findById(Long id) {
    return userRepository.findById(id)
        .map(this::toDto)
        .orElseThrow(() -> new UserNotFoundException(id));
  }

  // @Transactional wraps this method in a DB transaction.
  // If anything throws, the transaction rolls back automatically — no partial writes.
  @Transactional
  public UserDto create(CreateUserRequest req) {
    User user = new User();
    user.setName(req.name());
    user.setEmail(req.email());
    // save() inserts the row and returns the saved entity (now with a generated id and createdAt).
    return toDto(userRepository.save(user));
  }

  @Transactional
  public UserDto update(Long id, UpdateUserRequest req) {
    // Load the existing user first — throw 404 if not found.
    User user = userRepository.findById(id)
        .orElseThrow(() -> new UserNotFoundException(id));
    // Only apply fields that were actually sent (null = not provided, skip it).
    if (req.name() != null)
      user.setName(req.name());
    if (req.email() != null)
      user.setEmail(req.email());
    return toDto(userRepository.save(user));
  }

  @Transactional
  public void delete(Long id) {
    // Check existence first so we can throw a meaningful 404 instead of silently doing nothing.
    if (!userRepository.existsById(id))
      throw new UserNotFoundException(id);
    userRepository.deleteById(id);
  }

  // Private helper: converts the internal User entity into a UserDto for the response.
  // Keeps the DB schema decoupled from what the API exposes.
  private UserDto toDto(User user) {
    return new UserDto(user.getId(), user.getName(), user.getEmail(), user.getCreatedAt());
  }
}