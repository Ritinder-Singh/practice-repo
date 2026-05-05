# =============================================================================
# Python — Functions
# =============================================================================
# Topics: positional/keyword args, *args/**kwargs, default params,
#         first-class functions, closures, decorators, lambda.
# Run: python 02_functions.py
# =============================================================================

# TODO 1: *args and **kwargs
#   Write a function log(level: str, *messages, sep=" ", **context) that:
#   - Accepts variable messages
#   - Accepts keyword context (e.g. user_id=1, action="login")
#   - Prints: [LEVEL] message1 message2 | key=val key=val
#
# def log(level: str, *messages, sep: str = " ", **context) -> None:
#     pass

# TODO 2: Default mutable argument trap
#   Explain why this is a bug and fix it:
#   def add_item(item, lst=[]):
#       lst.append(item)
#       return lst
#   Fix: use None as default and create list inside function

# TODO 3: Closures
#   Implement a make_counter() factory that returns a counter function.
#   Each call to counter() increments and returns the count.
#   Use nonlocal to modify the enclosing scope variable.
#
# def make_counter(start: int = 0):
#     count = start
#     def counter() -> int:
#         nonlocal count
#         # increment and return
#         pass
#     return counter

# TODO 4: Decorators
#   TODO 4a: timer decorator — measures and prints execution time
#   TODO 4b: retry decorator — retries on exception up to N times
#   TODO 4c: cache decorator (simple memoization without functools.lru_cache)
#
# import time, functools
# def timer(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         pass
#     return wrapper

# TODO 5: Higher-order functions
#   Implement map(), filter(), reduce() from scratch (don't use builtins):
#
# def my_map(func, iterable):
#     pass
#
# def my_filter(func, iterable):
#     pass
#
# def my_reduce(func, iterable, initial=None):
#     pass

# TODO 6: Lambda and functional patterns
#   Given a list of dicts: [{"name": "Alice", "age": 30}, ...]
#   Sort by age using lambda
#   Filter those over 25 using filter + lambda
#   Extract names using map + lambda
#   Chain with list comprehension alternatives

# TODO 7: Partial functions
#   Use functools.partial to create specialized versions of a function:
#   base_url_builder(base, path, params) -> str
#   Create: api_v1 = partial(base_url_builder, "https://api.example.com", version="v1")
