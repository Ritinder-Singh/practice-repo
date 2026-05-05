package app.service;

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

public class UserService {
    // stub
}
