// =============================================================================
// Rust — Error Handling
// =============================================================================
// Topics: Option<T>, Result<T,E>, ? operator, custom error types,
//         thiserror/anyhow (note: require Cargo), error conversion.
// Compile: rustc 06_error_handling.rs && ./06_error_handling
// Docs: https://doc.rust-lang.org/book/ch09-00-error-handling.html
// =============================================================================

use std::num::ParseIntError;
use std::fmt;

// TODO 1: Option<T> — absence of value
//   fn find_first_even(nums: &[i32]) -> Option<i32>
//   Methods: .unwrap(), .unwrap_or(default), .unwrap_or_else(|| ...), .expect("msg")
//   .map(|x| x*2), .and_then(|x| ...), .filter(|x| x>0), .is_some(), .is_none()

// TODO 2: Result<T, E> — success or failure
//   fn parse_number(s: &str) -> Result<i32, ParseIntError> { s.parse() }
//   .ok() → Option<T>, .err() → Option<E>
//   .map(|x| x*2), .map_err(|e| ...), .and_then(|x| ...), .unwrap_or(0)

// TODO 3: ? operator — early return on error
//   fn read_username(path: &str) -> Result<String, std::io::Error> {
//       let mut s = String::new();
//       std::fs::File::open(path)?.read_to_string(&mut s)?;  // ? = if err { return Err(e) }
//       Ok(s)
//   }

// TODO 4: Custom error type
//   #[derive(Debug)]
//   enum AppError { ParseError(ParseIntError), NotFound(String), InvalidInput(String) }
//   impl fmt::Display for AppError { ... }
//   impl std::error::Error for AppError {}
//   impl From<ParseIntError> for AppError { fn from(e: ParseIntError) -> Self { Self::ParseError(e) } }

// TODO 5: Combining multiple error types
//   Box<dyn std::error::Error>  — easiest, heap-allocated, erases error type
//   Custom enum + From impls    — explicit, zero-cost, preserves types
//   Note: thiserror crate simplifies #4 with derive macros (requires Cargo)

// TODO 6: panic! vs Result
//   Use panic: unrecoverable (test failure, logic bugs, index out of bounds)
//   Use Result: expected failures (I/O, parsing, network)
//   Unwinding vs abort: RUST_BACKTRACE=1 for panic traces

fn main() {
    // Suppress unused import warnings
    let _: Option<ParseIntError> = None;
    let _: &dyn fmt::Display = &"suppress";
    println!("Rust error handling — implement TODOs above");
}
