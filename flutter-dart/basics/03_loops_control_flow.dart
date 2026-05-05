// TOPIC: Loops & Control Flow | dart 03_loops_control_flow.dart
// Docs: https://dart.dev/language/loops

void main() {
  // TODO 1: for, while, do-while
  //   for (var i = 0; i < 10; i++) { }
  //   for (var item in list) { }           // for-in
  //   list.forEach((item) { });            // forEach
  //   while (condition) { }
  //   do { } while (condition);

  // TODO 2: break and continue with labels
  //   outer: for (var i = 0; i < 3; i++) {
  //     for (var j = 0; j < 3; j++) {
  //       if (j == 1) continue outer;
  //       if (i == 2) break outer;
  //     }
  //   }

  // TODO 3: switch expressions (Dart 3.0)
  //   String day = switch (dayNumber) {
  //     1 || 7 => "Weekend",
  //     2 | 3 | 4 | 5 | 6 => "Weekday",
  //     _ => "Unknown"
  //   };
  //   Also: switch with patterns and guards
  //   switch (value) {
  //     case int n when n > 0: print("positive");
  //     case int n: print("non-positive");
  //   }

  // TODO 4: Iterable methods — the functional approach to loops
  //   list.where((x) => x > 0)         // filter
  //   list.map((x) => x * 2)           // transform
  //   list.reduce((a, b) => a + b)     // fold to single value
  //   list.fold(0, (acc, x) => acc + x) // fold with initial value
  //   list.any((x) => x > 5)           // returns bool
  //   list.every((x) => x > 0)         // returns bool
  //   list.takeWhile((x) => x < 10)    // take until false
  //   list.skipWhile((x) => x < 10)    // skip until false

  // TODO 5: FizzBuzz using various approaches
  //   Approach 1: traditional for loop
  //   Approach 2: Iterable.generate(100, (i) => ...) with switch expression
  //   Approach 3: List.generate + join for one-liner

  // TODO 6: Generators — sync* and async*
  //   Iterable<int> naturals(int n) sync* {
  //     for (var i = 1; i <= n; i++) yield i;
  //   }
  //   Iterable<int> fibonacci() sync* {
  //     var a = 0, b = 1;
  //     while (true) { yield a; var t = a + b; a = b; b = t; }
  //   }
  //   fibonacci().take(10).toList()

  // TODO 7: assert — development-only checks
  //   assert(list.isNotEmpty, "List must not be empty");
  //   assert(x > 0);   // throws AssertionError in debug mode if false

  // TODO 8: Pattern matching in control flow (Dart 3.0)
  //   final shape = Circle(radius: 5.0);
  //   if (shape case Circle(radius: var r)) {
  //     print("Circle with radius $r");
  //   }
  //   // switch with record patterns
  //   switch ((x, y)) {
  //     case (0, 0): print("origin");
  //     case (var a, 0): print("x-axis at $a");
  //     case (0, var b): print("y-axis at $b");
  //     case (var a, var b): print("($a, $b)");
  //   }
}
