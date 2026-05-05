// TOPIC: Advanced Dart | dart 08_advanced.dart
// Docs: https://dart.dev/language

void main() {
  // TODO 1: Isolates for CPU-parallel work
  //   import 'dart:isolate';
  //   void isolateFunction(SendPort sendPort) {
  //     final result = expensiveComputation();
  //     sendPort.send(result);
  //   }
  //   final receivePort = ReceivePort();
  //   await Isolate.spawn(isolateFunction, receivePort.sendPort);
  //   final result = await receivePort.first;
  //   // Dart 2.19+ short form: await Isolate.run(expensiveComputation)

  // TODO 2: Generators — sync* and async*
  //   // sync* — produces an Iterable lazily
  //   Iterable<int> fibonacci() sync* {
  //     var a = 0, b = 1;
  //     while (true) { yield a; [a, b] = [b, a + b]; }
  //   }
  //   fibonacci().take(10).toList()
  //
  //   // async* — produces a Stream
  //   Stream<String> streamLines(String text) async* {
  //     for (final line in text.split('\n')) {
  //       await Future.delayed(Duration(milliseconds: 100));
  //       yield line;
  //     }
  //   }

  // TODO 3: yield* — delegate to another generator
  //   Iterable<int> range(int start, int end) sync* {
  //     for (var i = start; i < end; i++) yield i;
  //   }
  //   Iterable<int> rangeWithMiddle(int start, int end, int mid) sync* {
  //     yield* range(start, mid);
  //     yield mid;
  //     yield* range(mid + 1, end);
  //   }

  // TODO 4: Metadata annotations
  //   @override, @deprecated, @immutable — built-in annotations
  //   Custom: class Route { final String path; const Route(this.path); }
  //   @Route("/users")
  //   class UsersController { }
  //   // Read at runtime with dart:mirrors (mirrors disabled in Flutter AOT)

  // TODO 5: const constructor — compile-time constant objects
  //   class Color {
  //     final int r, g, b;
  //     const Color(this.r, this.g, this.b);
  //     static const red = Color(255, 0, 0);
  //     static const green = Color(0, 255, 0);
  //   }
  //   const c = Color.red;  // same object as Color.red (identical)

  // TODO 6: Callable classes — implement call()
  //   class Multiplier {
  //     final int factor;
  //     const Multiplier(this.factor);
  //     int call(int value) => value * factor;
  //   }
  //   final triple = Multiplier(3);
  //   print(triple(5));  // 15 — used like a function

  // TODO 7: noSuchMethod — intercept missing methods
  //   class DynamicProxy {
  //     @override
  //     dynamic noSuchMethod(Invocation invocation) {
  //       print("Called: ${invocation.memberName}");
  //       print("Args: ${invocation.positionalArguments}");
  //       return super.noSuchMethod(invocation);
  //     }
  //   }

  // TODO 8: Late final — lazy singleton initialization
  //   class Database {
  //     late final Connection _connection;
  //     void connect(String url) { _connection = Connection(url); }
  //     // _connection can only be assigned once; throws if accessed before set
  //   }
}
