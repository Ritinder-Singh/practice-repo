// TOPIC: Data Structures | dart 04_data_structures.dart
// Docs: https://dart.dev/guides/libraries/library-tour#collections

void main() {
  // TODO 1: List — ordered, indexed, growable vs fixed-length
  //   var list = [1, 2, 3];           // growable
  //   var fixed = List.filled(5, 0);  // fixed-length, all zeros
  //   list.add(4); list.addAll([5,6]);
  //   list.insert(0, 0);
  //   list.removeWhere((x) => x % 2 == 0);
  //   list.sort(); list.sort((a, b) => b.compareTo(a));  // custom comparator

  // TODO 2: Map — key-value pairs
  //   var map = <String, int>{"a": 1, "b": 2};
  //   map["c"] = 3;                        // add/update
  //   map.putIfAbsent("d", () => 4);       // only add if absent
  //   map.update("a", (v) => v + 10);      // update existing
  //   map.entries.map((e) => "${e.key}=${e.value}")
  //   map.removeWhere((k, v) => v < 2);

  // TODO 3: Set — unique unordered values
  //   var s1 = {1, 2, 3, 4};
  //   var s2 = {3, 4, 5, 6};
  //   s1.intersection(s2);   // {3, 4}
  //   s1.union(s2);          // {1, 2, 3, 4, 5, 6}
  //   s1.difference(s2);     // {1, 2}

  // TODO 4: Queue (from dart:collection)
  //   import 'dart:collection';
  //   var q = Queue<int>();
  //   q.addLast(1); q.addLast(2);   // enqueue
  //   q.removeFirst();               // dequeue
  //   q.addFirst(0);                 // push to front (deque usage)

  // TODO 5: LinkedList (from dart:collection) — O(1) insert/remove at ends
  //   class MyNode extends LinkedListEntry<MyNode> { int val; MyNode(this.val); }
  //   var ll = LinkedList<MyNode>();
  //   ll.add(MyNode(1)); ll.add(MyNode(2));
  //   ll.first.insertBefore(MyNode(0));

  // TODO 6: Implement generic Stack<T>
  //   class Stack<T> {
  //     final _items = <T>[];
  //     void push(T item) => _items.add(item);
  //     T pop() => _items.removeLast();
  //     T get peek => _items.last;
  //     bool get isEmpty => _items.isEmpty;
  //     int get length => _items.length;
  //   }

  // TODO 7: Spread and collection-if/for (Dart 2.3+)
  //   var extra = [4, 5];
  //   var combined = [1, 2, 3, ...extra];   // spread
  //   var filtered = [
  //     for (var x in combined) if (x % 2 == 0) x * 10
  //   ];  // collection-if and collection-for

  // TODO 8: SplayTreeMap / SplayTreeSet — ordered, O(log n) operations
  //   import 'dart:collection';
  //   var sorted = SplayTreeMap<String, int>();
  //   sorted.addAll({"banana": 2, "apple": 1, "cherry": 3});
  //   sorted.keys.toList()   // ["apple", "banana", "cherry"]
  //   sorted.lastKey()       // "cherry"
}
