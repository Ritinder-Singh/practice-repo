# =============================================================================
# Python — Error Handling
# =============================================================================
# Topics: try/except/else/finally, raising exceptions, custom exception classes,
#         context managers (__enter__/__exit__), exception chaining.
# Run: python 06_error_handling.py
# =============================================================================

from dataclasses import dataclass
from typing import Generic, TypeVar
import contextlib, time

T = TypeVar("T")
E = TypeVar("E")

# TODO 1: try/except/else/finally
#   Write safe_divide(a, b) that:
#   - Returns a / b as float
#   - Catches ZeroDivisionError → return None
#   - Catches TypeError → re-raise with descriptive message
#   - finally block prints "safe_divide called"
#
# def safe_divide(a: float, b: float) -> float | None:
#     pass

# TODO 2: Custom exception hierarchy
#   AppError (base)
#   ├── ValidationError(AppError)  — field: str, message: str
#   └── NotFoundError(AppError)    — resource: str, id: int
#   Write find_user(users: dict, user_id: int) that raises NotFoundError.
#
# class AppError(Exception):
#     pass

# TODO 3: Context manager with class
#   Implement timer() context manager — prints elapsed time on exit.
#   Then implement same thing using @contextlib.contextmanager decorator.
#
# class timer:
#     def __enter__(self): ...
#     def __exit__(self, exc_type, exc_val, exc_tb): ...

# TODO 4: Exception chaining
#   Write load_config(path: str) -> dict that:
#   - Opens a JSON file
#   - Raises ConfigError chained from FileNotFoundError using `raise X from Y`
#
# class ConfigError(AppError):
#     pass

# TODO 5: Simulated Result type (Rust-style)
#   Implement Ok[T] and Err[E] dataclasses, define Result = Ok | Err.
#   Write parse_int(s: str) -> Result[int, str] — no try/except in caller.
#
# @dataclass
# class Ok(Generic[T]):
#     value: T
#
# @dataclass
# class Err(Generic[E]):
#     error: E

# TODO 6: ExceptionGroup (Python 3.11+)
#   Write validate_form(data: dict) that collects ALL validation errors
#   and raises them as an ExceptionGroup. Use `except*` syntax to handle.
