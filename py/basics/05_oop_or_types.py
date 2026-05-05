# =============================================================================
# Python — OOP & Type System
# =============================================================================
# Topics: classes, inheritance, MRO, abstract classes, protocols,
#         dunder methods, properties, slots, type hints with generics.
# Run: python 05_oop_or_types.py
# =============================================================================

from abc import ABC, abstractmethod
from typing import Protocol, Generic, TypeVar, runtime_checkable

T = TypeVar("T")

# TODO 1: Class fundamentals — Shape hierarchy
#   Define: Shape (abstract base), Circle, Rectangle, Triangle
#   Each concrete class implements: area() -> float, perimeter() -> float
#   Shape defines: __str__, __repr__, __eq__ (compare area)
#   Use @property for computed attributes where appropriate
#
# class Shape(ABC):
#     @abstractmethod
#     def area(self) -> float: ...
#
#     @abstractmethod
#     def perimeter(self) -> float: ...

# TODO 2: Dunder methods
#   Implement a Vector2D class with:
#   - __add__, __sub__, __mul__ (scalar), __truediv__
#   - __abs__ (magnitude), __neg__
#   - __eq__, __hash__ (so it can be used in sets/dicts)
#   - __repr__, __str__
#   - __iter__ (yield x then y, so x,y = vec unpacking works)
#
# class Vector2D:
#     def __init__(self, x: float, y: float):
#         self.x = x
#         self.y = y

# TODO 3: Properties and slots
#   Implement a Temperature class:
#   - Store internally in Celsius
#   - @property celsius / fahrenheit / kelvin with setters
#   - Validation: raise ValueError if kelvin < 0
#   - Use __slots__ = ['_celsius'] to prevent arbitrary attribute creation
#
# class Temperature:
#     __slots__ = ['_celsius']

# TODO 4: Class and static methods
#   Implement a Date class with:
#   - @classmethod from_string(cls, s: str) -> Date  (parse "2024-01-15")
#   - @classmethod today(cls) -> Date
#   - @staticmethod is_leap_year(year: int) -> bool
#   - Instance method: days_until(other: Date) -> int

# TODO 5: Protocol (Structural typing)
#   Define a Drawable protocol — any class with draw() -> str qualifies.
#   Use @runtime_checkable to allow isinstance() checks.
#   Test with two unrelated classes that both have draw() — no inheritance needed.
#
# @runtime_checkable
# class Drawable(Protocol):
#     def draw(self) -> str: ...

# TODO 6: Generic class
#   Implement a Stack[T] generic class:
#   - push(item: T), pop() -> T, peek() -> T, is_empty() -> bool
#   - Type-safe: Stack[int] only accepts integers
#
# class Stack(Generic[T]):
#     def __init__(self) -> None:
#         self._items: list[T] = []

# TODO 7: MRO — Multiple Inheritance diamond problem
#   Create: Animal, Flyable, Swimmable, Duck(Animal, Flyable, Swimmable)
#   Print Duck.__mro__ to understand resolution order.
#   Add a move() method at each level, call super() to chain.
