# =============================================================================
# Python — Variables & Types
# =============================================================================
# Topics: built-in types (int, float, str, bool, None), type coercion,
#         type hints, f-strings, string methods, bytes vs str.
# Run: python 01_variables_types.py
# Docs: https://docs.python.org/3/library/stdtypes.html
# =============================================================================

# TODO 1: Declare variables of each built-in type and print their type()
#   integer, float, complex, bool, None, str, bytes
#   x: int = 42
#   pi: float = 3.14
#   ...

# TODO 2: Type conversion — convert between int, float, str, bool
#   int("42"), float("3.14"), str(100), bool(0), bool(""), bool("hello")
#   Understand: truthy vs falsy values

# TODO 3: String methods — implement a function clean_text(s: str) -> str
#   that: strips whitespace, lowercases, replaces spaces with underscores,
#   removes non-alphanumeric chars (use str.replace or regex).
#
# def clean_text(s: str) -> str:
#     pass

# TODO 4: f-strings — format a table of products with aligned columns
#   Use f-string format specifiers: {value:<20} {price:>10.2f}
#   Output:
#     Product             Price
#     MacBook Pro          1299.99
#     AirPods                 199.00

# TODO 5: String slicing and indexing
#   s = "Hello, World!"
#   Practice: s[0], s[-1], s[0:5], s[::2], s[::-1]
#   Implement: reverse_words(s) -> str  (reverse word order, not chars)
#
# def reverse_words(s: str) -> str:
#     pass

# TODO 6: Bytes vs str
#   Understand encoding/decoding:
#   text = "Hello, 世界"
#   encoded = text.encode("utf-8")  # bytes
#   decoded = encoded.decode("utf-8")  # str back
#   Show the difference in len() for multi-byte characters

# TODO 7: Type hints with Python 3.10+ union syntax
#   Write a function that accepts int | str | None and returns str
#   def stringify(val: int | str | None) -> str:
#       pass
