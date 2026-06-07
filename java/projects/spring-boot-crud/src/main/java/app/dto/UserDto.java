package app.dto;

import java.time.LocalDateTime;

// DTO (Data Transfer Object) — what we send back in API responses.
// We never expose the raw User entity directly because it's tied to the DB schema.
// If the schema changes (e.g. we rename a column), the API response stays the same.
//
// record is a modern Java feature (Java 16+) that auto-generates:
//   constructor, getters (via id(), name(), etc.), equals(), hashCode(), toString().
// One line replaces ~40 lines of boilerplate.
public record UserDto(Long id, String name, String email, LocalDateTime createdAt) {
}