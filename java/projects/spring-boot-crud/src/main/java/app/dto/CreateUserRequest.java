package app.dto;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;

// Represents the JSON body expected on POST /api/users.
// Using a separate request object (instead of accepting a User entity directly) keeps
// the API contract decoupled from the DB model — callers can't accidentally set id or createdAt.
//
// @NotBlank — rejects null, empty string, or whitespace-only.
// @Email    — validates the email format.
// These are triggered by @Valid in the controller.
public record CreateUserRequest(
    @NotBlank String name,
    @Email @NotBlank String email) {
}