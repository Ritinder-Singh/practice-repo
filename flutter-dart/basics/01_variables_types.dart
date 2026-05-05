// TOPIC: Variables & Types | dart 01_variables_types.dart
// Docs: https://dart.dev/language/variables

void main() {
  // TODO 1: var, final, const — difference at runtime vs compile time
  //   var name = "Alice";          // inferred as String, mutable
  //   final age = 30;              // set once at runtime, immutable after
  //   const pi = 3.14159;          // compile-time constant, must be known at compile time
  //   Demonstrate: final allows dynamic values (DateTime.now()), const does not

  // TODO 2: Nullable types and null safety
  //   String? nullableName;        // can be null
  //   String nonNullable = "Bob";  // cannot be null
  //   nullableName?.length         // safe navigation
  //   nullableName ?? "default"    // null coalescing
  //   late String lazyInit;        // initialized before first use (not at declaration)

  // TODO 3: Basic types
  //   int, double, String, bool, List, Map, Set, Symbol
  //   Type conversion: int.parse("42"), double.parse("3.14"), 42.toString()
  //   Check: identical() vs == for reference vs value equality

  // TODO 4: Type inference and explicit annotation
  //   var inferred = [1, 2, 3];     // List<int>
  //   dynamic anything = 42;         // disables type checking (avoid)
  //   Object obj = "hello";          // any non-null value
  //   Demonstrate type check: if (obj is String) { obj.length } // smart cast

  // TODO 5: Records (Dart 3.0)
  //   (String, int) person = ("Alice", 30);
  //   print(person.$1);  // Alice
  //   print(person.$2);  // 30
  //   Named record fields: ({String name, int age}) p = (name: "Alice", age: 30);
  //   print(p.name);

  // TODO 6: Patterns (Dart 3.0)
  //   var [a, b, c] = [1, 2, 3];      // list pattern
  //   var {"x": x, "y": y} = {"x": 1, "y": 2};  // map pattern
  //   switch (person) {
  //     case ("Alice", int age): print("Alice is $age");
  //   }

  // TODO 7: typedef — type aliases for functions
  //   typedef Predicate<T> = bool Function(T value);
  //   typedef Callback = void Function(String message);
  //   Use as parameter: void process(List<int> nums, Predicate<int> test)

  // TODO 8: Extension types (Dart 3.0) — zero-cost wrappers
  //   extension type Meters(double value) { double toFeet() => value * 3.28084; }
  //   extension type UserId(int value) {}  // prevents mixing up int IDs
  //   Meters(5.0).toFeet()
}
