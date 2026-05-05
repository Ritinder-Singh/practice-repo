# =============================================================================
# Python — Advanced Topics
# =============================================================================
# Topics: generators/coroutines, metaclasses, descriptors, CPython internals,
#         context managers, type hints advanced, functools.
# Run: python 08_advanced.py
# =============================================================================

import functools, sys
from typing import TypeVar, ParamSpec, Callable

P = ParamSpec("P")
R = TypeVar("R")

# TODO 1: Metaclasses
#   Create a Singleton metaclass that ensures only one instance of any class.
#   Create a RegisteredMeta metaclass that maintains a registry of all subclasses.
#
# class SingletonMeta(type):
#     _instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super().__call__(*args, **kwargs)
#         return cls._instances[cls]

# TODO 2: Descriptors
#   Implement a Validated descriptor that:
#   - Enforces a type check on set
#   - Optionally enforces a min/max range for numbers
#   Use it to create a typed dataclass-like class:
#
# class Typed:
#     def __set_name__(self, owner, name): ...
#     def __get__(self, obj, objtype=None): ...
#     def __set__(self, obj, value): ...

# TODO 3: __slots__ and memory optimization
#   Create a Point class with and without __slots__.
#   Use sys.getsizeof() and tracemalloc to compare memory usage
#   for 1 million instances.

# TODO 4: CPython internals — id(), is, interning
#   Explain and demonstrate:
#   - Integer interning (-5 to 256 are cached)
#   - String interning (single-word strings)
#   - The difference between `is` and `==`
#   - LEGB scope resolution

# TODO 5: Advanced decorators with ParamSpec
#   Write a fully type-safe retry decorator using ParamSpec:
#
# def retry(n: int, exceptions: tuple = (Exception,)):
#     def decorator(func: Callable[P, R]) -> Callable[P, R]:
#         @functools.wraps(func)
#         def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
#             for attempt in range(n):
#                 try:
#                     return func(*args, **kwargs)
#                 except exceptions as e:
#                     if attempt == n - 1:
#                         raise
#             raise RuntimeError("unreachable")
#         return wrapper
#     return decorator

# TODO 6: __init_subclass__ and class registration
#   Build a plugin system where subclasses automatically register themselves:
#
# class Plugin:
#     _registry = {}
#     def __init_subclass__(cls, plugin_name: str, **kwargs):
#         super().__init_subclass__(**kwargs)
#         Plugin._registry[plugin_name] = cls

# TODO 7: Generator-based coroutines (pre-async/await history)
#   Implement a simple coroutine scheduler using generator .send():
#   - Two generators that yield control to each other
#   - A scheduler that drives them forward
#   (This is how asyncio worked internally before Python 3.5)
