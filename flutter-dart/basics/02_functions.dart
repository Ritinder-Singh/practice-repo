// TOPIC: Functions | dart 02_functions.dart
// Docs: https://dart.dev/language/functions

void main() {
  // TODO 1: Named & positional parameters — required, optional [], default values
  //   void printInfo(String name, {required int age, String role = "user"}) { }
  //   printInfo("Alice", age: 30);           // named, required
  //   void greet(String greeting, [String? name]) { }
  //   greet("Hello");                        // optional positional
  //   greet("Hello", "World");

  // TODO 2: Arrow functions — single expression
  //   int double(int x) => x * 2;
  //   bool isEven(int n) => n % 2 == 0;
  //   List<String> toUpperCase(List<String> words) => words.map((w) => w.toUpperCase()).toList();

  // TODO 3: First-class functions
  //   Function type annotations: int Function(int) transformer;
  //   Assign: transformer = (x) => x * 2;
  //   Pass: List<int> applyAll(List<int> nums, int Function(int) fn) => nums.map(fn).toList();

  // TODO 4: Closures — capture outer scope
  //   Function makeCounter() {
  //     int count = 0;
  //     return () => ++count;  // captures count variable
  //   }
  //   var counter = makeCounter();
  //   counter(); counter(); counter();  // 1, 2, 3

  // TODO 5: Generics
  //   T identity<T>(T value) => value;
  //   List<T> repeat<T>(T val, int n) => List.generate(n, (_) => val);
  //   Pair<A,B> zip<A,B>(A a, B b) => (a, b);  // using records

  // TODO 6: Extension methods — add methods to existing types
  //   extension StringExtensions on String {
  //     bool get isPalindrome => this == split('').reversed.join();
  //     String repeat(int n) => this * n;
  //   }
  //   "racecar".isPalindrome  // true
  //   "ha".repeat(3)          // "hahaha"

  // TODO 7: Cascade notation (..) — method chaining
  //   final sb = StringBuffer()
  //     ..write("Hello")
  //     ..write(", ")
  //     ..write("World");
  //   sb.toString();  // "Hello, World"
  //   Also works on objects: list..add(1)..add(2)..add(3);

  // TODO 8: Tear-offs — reference method without calling it
  //   list.forEach(print);         // tear-off — same as (e) => print(e)
  //   list.map(int.parse);         // static method tear-off
  //   list.map(someObj.process);   // instance method tear-off
  //   Demonstrate difference: list.forEach(print) vs list.forEach((e) => print(e))
}
