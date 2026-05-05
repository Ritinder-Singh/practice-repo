// TOPIC: OOP & Type System | dart 05_oop_or_types.dart
// Docs: https://dart.dev/language/classes

void main() {
  // TODO 1: Classes — constructor shorthand, named constructors
  //   class Point {
  //     final double x, y;
  //     Point(this.x, this.y);                 // shorthand
  //     Point.origin() : x = 0, y = 0;        // named constructor
  //     Point.fromMap(Map<String, double> m) : x = m["x"]!, y = m["y"]!;
  //     double distanceTo(Point other) => ...
  //   }

  // TODO 2: Mixins — reuse behavior without inheritance
  //   mixin Flyable { void fly() => print("Flying"); }
  //   mixin Swimmable { void swim() => print("Swimming"); }
  //   class Duck extends Animal with Flyable, Swimmable { }
  //   Constraint: mixin on Animal { } — only apply to Animal subclasses

  // TODO 3: Interfaces (implements keyword) — Dart classes are implicit interfaces
  //   abstract class Serializable {
  //     Map<String, dynamic> toJson();
  //     factory Serializable.fromJson(Map<String, dynamic> json) { ... }
  //   }
  //   class User implements Serializable { ... }  // must implement all methods

  // TODO 4: Abstract classes vs sealed classes
  //   abstract class Shape { double area(); }   // can't be instantiated
  //   sealed class Result<T> { }                // Dart 3 — exhaustive switch
  //   final class Success<T> extends Result<T> { final T data; Success(this.data); }
  //   final class Failure<T> extends Result<T> { final String error; Failure(this.error); }

  // TODO 5: Operator overloading
  //   class Vector {
  //     final double x, y;
  //     Vector(this.x, this.y);
  //     Vector operator +(Vector other) => Vector(x + other.x, y + other.y);
  //     Vector operator *(double scalar) => Vector(x * scalar, y * scalar);
  //     bool operator ==(Object other) => other is Vector && x == other.x && y == other.y;
  //     @override int get hashCode => Object.hash(x, y);
  //   }

  // TODO 6: Generics with constraints
  //   class SortedList<T extends Comparable<T>> {
  //     final _items = <T>[];
  //     void add(T item) {
  //       _items.add(item);
  //       _items.sort();
  //     }
  //   }

  // TODO 7: Factory constructors — return cached or subtype instances
  //   class Logger {
  //     static final _cache = <String, Logger>{};
  //     final String name;
  //     Logger._internal(this.name);
  //     factory Logger(String name) => _cache.putIfAbsent(name, () => Logger._internal(name));
  //   }

  // TODO 8: Enum with methods (Dart 2.17+)
  //   enum Planet {
  //     mercury(3.303e+23, 2.4397e6),
  //     venus(4.869e+24, 6.0518e6),
  //     earth(5.976e+24, 6.37814e6);
  //     final double mass, radius;
  //     const Planet(this.mass, this.radius);
  //     double get surfaceGravity => 6.67430e-11 * mass / (radius * radius);
  //   }
}
