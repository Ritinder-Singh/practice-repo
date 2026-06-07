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

// PROJECT: Spring Boot User Service
//
// TODO 1: @Service annotation, inject UserRepository
//
// TODO 2: findAll() → List<UserDto>
//   - userRepository.findAll().stream().map(this::toDto).toList()
//
// TODO 3: findById(Long id) → UserDto
//   - throw new UserNotFoundException("User not found: " + id) if absent
//
// TODO 4: create(CreateUserRequest req) → UserDto
//   - Check email uniqueness: if (userRepository.existsByEmail(req.email())) throw DuplicateEmailException
//   - Save and return DTO
//
// TODO 5: update(Long id, UpdateUserRequest req) → UserDto
//   - Load existing, apply changes, save
//
// TODO 6: delete(Long id) → void
//   - Verify exists, then userRepository.deleteById(id)
//
// TODO 7: Private toDto(User user) → UserDto helper method

//public class UserService {
//    // stub
//}

@Service
@RequiredArgsConstructor
public class UserService {

  private final UserRepository userRepository;

  public List<UserDto> findAll() {
    return userRepository.findAll().stream()
        .map(this::toDto)
        .toList();
  }

  public UserDto findById(Long id) {
    return userRepository.findById(id)
        .map(this::toDto)
        .orElseThrow(() -> new UserNotFoundException(id));
  }

  @Transactional
  public UserDto create(CreateUserRequest req) {
    User user = new User();
    user.setName(req.name());
    user.setEmail(req.email());
    return toDto(userRepository.save(user));
  }

  @Transactional
  public UserDto update(Long id, UpdateUserRequest req) {
    User user = userRepository.findById(id)
        .orElseThrow(() -> new UserNotFoundException(id));
    if (req.name() != null)
      user.setName(req.name());
    if (req.email() != null)
      user.setEmail(req.email());
    return toDto(userRepository.save(user));
  }

  @Transactional
  public void delete(Long id) {
    if (!userRepository.existsById(id))
      throw new UserNotFoundException(id);
    userRepository.deleteById(id);
  }

  private UserDto toDto(User user) {
    return new UserDto(user.getId(), user.getName(), user.getEmail(), user.getCreatedAt());
  }
}
