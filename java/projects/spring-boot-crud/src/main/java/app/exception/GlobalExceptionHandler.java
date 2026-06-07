package app.exception;

import org.springframework.http.HttpStatus;
import org.springframework.http.ProblemDetail;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

// @RestControllerAdvice intercepts exceptions thrown anywhere in your controllers
// and lets you handle them centrally instead of try/catching in every method.
@RestControllerAdvice
public class GlobalExceptionHandler {

  // @ExceptionHandler maps a specific exception type to this method.
  // When UserNotFoundException is thrown anywhere, Spring calls this instead of returning a 500.
  // ProblemDetail is Spring 6's standard error response format (RFC 9457) — returns structured JSON.
  @ExceptionHandler(UserNotFoundException.class)
  public ProblemDetail handleNotFound(UserNotFoundException ex) {
    ProblemDetail problem = ProblemDetail.forStatus(HttpStatus.NOT_FOUND);
    problem.setDetail(ex.getMessage());
    return problem;
  }

  // MethodArgumentNotValidException is thrown when @Valid fails on a @RequestBody.
  // We collect all field-level errors into a single readable string and return a 400.
  @ExceptionHandler(MethodArgumentNotValidException.class)
  public ProblemDetail handleValidation(MethodArgumentNotValidException ex) {
    ProblemDetail problem = ProblemDetail.forStatus(HttpStatus.BAD_REQUEST);
    problem.setDetail(ex.getBindingResult().getFieldErrors().stream()
        .map(e -> e.getField() + ": " + e.getDefaultMessage())
        .reduce("", (a, b) -> a.isEmpty() ? b : a + ", " + b));
    return problem;
  }
}
