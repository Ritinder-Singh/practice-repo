<?php
declare(strict_types=1);
// TOPIC: Error Handling | php 06_error_handling.php

// TODO 1: try-catch-finally
//   try {
//       $result = 10 / 0;  // not an exception in PHP! Returns INF or triggers warning
//       throw new \RuntimeException("Something went wrong");
//   } catch (\InvalidArgumentException $e) {
//       echo "Invalid arg: " . $e->getMessage();
//   } catch (\RuntimeException $e) {
//       echo "Runtime: " . $e->getMessage() . "\n";
//       echo $e->getTraceAsString();
//   } finally {
//       echo "Always runs\n";  // even if exception propagates
//   }

// TODO 2: Exception hierarchy
//   Throwable
//     ├── Error (programming errors — OOM, type error in strict mode, parse error)
//     │   ├── TypeError
//     │   ├── ParseError
//     │   └── ArithmeticError → DivisionByZeroError
//     └── Exception (application logic errors)
//         ├── RuntimeException
//         ├── InvalidArgumentException
//         ├── LogicException
//         └── ...
//   Catch \Throwable to catch both errors and exceptions (use sparingly)

// TODO 3: Custom exceptions
//   class AppException extends \RuntimeException {
//       public function __construct(
//           string $message,
//           private readonly string $context = "",
//           int $code = 0,
//           ?\Throwable $previous = null,
//       ) { parent::__construct($message, $code, $previous); }
//       public function getContext(): string { return $this->context; }
//   }
//   class NotFoundException extends AppException {}
//   class ValidationException extends AppException {
//       public function __construct(private readonly array $errors) {
//           parent::__construct("Validation failed");
//       }
//       public function getErrors(): array { return $this->errors; }
//   }

// TODO 4: set_exception_handler — global uncaught exception handler
//   set_exception_handler(function (\Throwable $e) {
//       error_log("Uncaught: " . $e->getMessage() . " in " . $e->getFile() . ":" . $e->getLine());
//       http_response_code(500);
//       echo json_encode(["error" => "Internal Server Error"]);
//   });

// TODO 5: set_error_handler — convert PHP errors to exceptions
//   set_error_handler(function (int $errno, string $errstr, string $errfile, int $errline): bool {
//       throw new \ErrorException($errstr, 0, $errno, $errfile, $errline);
//   });

// TODO 6: Multiple catch types (PHP 8.0)
//   catch (\TypeError | \ValueError $e) { }

// TODO 7: Exception chaining — preserve original cause
//   try { $db->query($sql); }
//   catch (\PDOException $e) {
//       throw new DatabaseException("Query failed: $sql", previous: $e);
//   }
//   // $e->getPrevious() returns the original PDOException

// TODO 8: Result pattern (no exceptions for flow control)
//   class Result {
//       private function __construct(private readonly bool $ok, private readonly mixed $value) {}
//       public static function ok(mixed $value): self { return new self(true, $value); }
//       public static function err(string $error): self { return new self(false, $error); }
//       public function isOk(): bool { return $this->ok; }
//       public function getValue(): mixed { return $this->ok ? $this->value : throw new \LogicException("No value on error"); }
//       public function getError(): string { return !$this->ok ? $this->value : throw new \LogicException("No error on success"); }
//   }
