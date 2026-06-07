package app.dto;

// Represents the JSON body expected on PUT /api/users/{id}.
// Fields are nullable — if null, the service layer treats them as "not provided" and skips the update.
// This allows partial updates: send only the fields you want to change.
public record UpdateUserRequest(String name, String email) {
}