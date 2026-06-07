package app.exception;

// Custom exception thrown when a user id doesn't exist in the DB.
// Extending RuntimeException means it's unchecked — you don't need to declare it in method signatures.
// GlobalExceptionHandler catches this and maps it to a 404 HTTP response.
public class UserNotFoundException extends RuntimeException {
  public UserNotFoundException(Long id) {
    super("User Not Found: " + id);
  }
}
