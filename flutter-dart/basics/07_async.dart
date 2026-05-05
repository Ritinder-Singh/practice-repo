// TOPIC: Async & Streams | dart 07_async.dart
// Docs: https://dart.dev/codelabs/async-await

import 'dart:async';

void main() async {
  // TODO 1: Future and async/await
  //   Future<String> fetchGreeting() async {
  //     await Future.delayed(Duration(seconds: 1));
  //     return "Hello, World!";
  //   }
  //   String result = await fetchGreeting();

  // TODO 2: Future.wait — run multiple Futures concurrently
  //   final results = await Future.wait([
  //     fetchUser(1),
  //     fetchOrders(1),
  //     fetchPreferences(1),
  //   ]);
  //   Compare with sequential: slower by 3x

  // TODO 3: Stream basics
  //   Stream<int> countDown(int from) async* {
  //     for (var i = from; i >= 0; i--) {
  //       await Future.delayed(Duration(seconds: 1));
  //       yield i;
  //     }
  //   }
  //   await for (final n in countDown(5)) { print(n); }

  // TODO 4: StreamController — push events manually
  //   final controller = StreamController<String>();
  //   controller.stream.listen(
  //     (data) => print("Got: $data"),
  //     onError: (e) => print("Error: $e"),
  //     onDone: () => print("Done"),
  //   );
  //   controller.add("hello"); controller.add("world"); controller.close();

  // TODO 5: Stream transformations
  //   stream
  //     .where((x) => x.isNotEmpty)
  //     .map((x) => x.toUpperCase())
  //     .distinct()
  //     .take(10)
  //     .debounceTime(Duration(milliseconds: 300))  // needs rxdart
  //   Built-in: take, skip, where, map, expand, cast, asyncMap, asyncExpand

  // TODO 6: Completer — create a Future you can complete manually
  //   Completer<String> completer = Completer();
  //   Timer(Duration(seconds: 1), () => completer.complete("done"));
  //   String result = await completer.future;
  //   // Use case: bridge callback APIs to Futures

  // TODO 7: Isolates — true parallelism for CPU-bound work
  //   import 'dart:isolate';
  //   int heavyComputation(int n) => List.generate(n, (i) => i).fold(0, (a, b) => a + b);
  //   final result = await Isolate.run(() => heavyComputation(1000000));
  //   // Dart 2.19+: Isolate.run() is the simple API

  // TODO 8: runZonedGuarded — catch all unhandled async errors
  //   runZonedGuarded(() async {
  //     await riskyOperation();
  //   }, (error, stack) {
  //     print("Unhandled error: $error");
  //     print(stack);
  //   });
}
