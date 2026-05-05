// TOPIC: Error Handling | dart 06_error_handling.dart
// Docs: https://dart.dev/language/error-handling

void main() {
  // TODO 1: try-catch-finally
  //   try {
  //     int result = int.parse("not a number");
  //   } on FormatException catch (e) {
  //     print("Format error: ${e.message}");
  //   } on RangeError catch (e, stackTrace) {
  //     print("Range error: $e");
  //     print(stackTrace);
  //   } catch (e) {
  //     print("Unknown error: $e");
  //   } finally {
  //     print("Always runs");
  //   }

  // TODO 2: Exception hierarchy
  //   Exception — application-level errors (implement this)
  //   Error — programming errors (should not catch in production: StateError, RangeError, TypeError)
  //   Demonstrate: throw FormatException("Invalid email");
  //   Custom: class ValidationException implements Exception { final String field; ... }

  // TODO 3: Custom exceptions
  //   class AppException implements Exception {
  //     final String message;
  //     final int? statusCode;
  //     const AppException(this.message, {this.statusCode});
  //     @override String toString() => "AppException: $message (code: $statusCode)";
  //   }
  //   class NotFoundException extends AppException {
  //     NotFoundException(String resource) : super("$resource not found", statusCode: 404);
  //   }

  // TODO 4: on clause — catch specific type without variable
  //   try { riskyOperation(); }
  //   on SocketException { print("No internet"); }
  //   on HttpException { print("HTTP error"); }

  // TODO 5: Result type pattern (no built-in Result, build your own)
  //   sealed class Result<T> {}
  //   final class Success<T> extends Result<T> { final T value; const Success(this.value); }
  //   final class Failure<T> extends Result<T> { final Exception error; const Failure(this.error); }
  //
  //   Result<User> findUser(int id) {
  //     try { return Success(repo.getUser(id)); }
  //     catch (e) { return Failure(e as Exception); }
  //   }
  //   switch (findUser(1)) {
  //     case Success(:var value): print(value);
  //     case Failure(:var error): print(error);
  //   }

  // TODO 6: rethrow — re-throw caught exception
  //   try { await fetchData(); }
  //   catch (e) {
  //     log.error("fetchData failed: $e");
  //     rethrow;  // preserves original stack trace (unlike throw e)
  //   }

  // TODO 7: Assertions — debug-only checks
  //   assert(value != null, "Value must not be null");
  //   assert(list.isNotEmpty);
  //   // Disabled in release mode; enabled with --enable-asserts

  // TODO 8: Error vs Exception — when to use each
  //   Error: programming mistakes (ArgumentError, StateError, AssertionError) — don't catch
  //   Exception: runtime conditions (IOException, FormatException) — do catch
  //   Show: throw ArgumentError("x must be positive: $x")  // programming error
  //         throw FormatException("invalid JSON")            // expected runtime error
}
