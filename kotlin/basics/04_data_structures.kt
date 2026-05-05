package basics
// TOPIC: Data Structures | kotlinc 04_data_structures.kt -include-runtime -d out.jar && java -jar out.jar
// Docs: https://kotlinlang.org/docs/collections-overview.html

fun main() {
    // TODO 1: List — listOf (immutable) vs mutableListOf, add/remove/sort
    //   - val immutable = listOf(3, 1, 2) — cannot add/remove
    //   - val mutable = mutableListOf(3, 1, 2) — add(4), remove(1), sort()
    //   - subList(fromIndex, toIndex), contains(), indexOf()
    //   - Convert between: immutable.toMutableList(), mutable.toList()

    // TODO 2: Map — mapOf vs mutableMapOf, getOrDefault, getOrElse, merge
    //   - val scores = mapOf("Alice" to 95, "Bob" to 87)
    //   - mutableMapOf, put(), remove(), keys, values, entries
    //   - getOrDefault("Charlie", 0), getOrElse("Charlie") { computeDefault() }
    //   - Merge two maps: map1 + map2 (map2 wins on key collision)
    //   - Update with compute: freq.merge(word, 1, Int::plus) pattern

    // TODO 3: Set — setOf, intersect, union, subtract
    //   - val a = setOf(1, 2, 3, 4), val b = setOf(3, 4, 5, 6)
    //   - a intersect b, a union b, a subtract b
    //   - mutableSetOf, add(), remove(), contains() — O(1) for HashSet
    //   - LinkedHashSet preserves insertion order; TreeSet is sorted

    // TODO 4: Pair & Triple — to infix, destructuring
    //   - val pair = "Alice" to 95  (infix 'to' creates Pair)
    //   - val (name, score) = pair
    //   - Triple("a", 1, true), val (x, y, z) = triple
    //   - Use case: returning two values from a function

    // TODO 5: ArrayDeque — as stack (addLast/removeLast) and queue (addFirst/removeLast)
    //   - val stack = ArrayDeque<Int>(); stack.addLast(1); stack.removeLast()
    //   - val queue = ArrayDeque<Int>(); queue.addLast(1); queue.removeFirst()
    //   - peekFirst() / peekLast() without removing
    //   - Show isEmpty() guard before remove to avoid NoSuchElementException

    // TODO 6: Implement Stack<T> — generic class using MutableList as backing store
    //   - Define class Stack<T> above main() with MutableList<T> backing
    //   - fun push(item: T), fun pop(): T?, fun peek(): T?, val size: Int, val isEmpty: Boolean
    //   - Use it in main(): push strings, pop and print them (LIFO order)

    // TODO 7: sortedBy/sortedWith — sort by multiple fields using compareBy
    //   - data class Student(val name: String, val gpa: Double, val year: Int)
    //   - sortedByDescending { it.gpa }
    //   - sortedWith(compareBy({ it.year }, { it.name })) — primary then secondary sort
    //   - compareByDescending, thenBy, thenByDescending

    // TODO 8: groupBy + mapValues — transform map values after grouping
    //   - val students = listOf(Student("Alice", 3.9, 2), Student("Bob", 3.5, 2), ...)
    //   - groupBy { it.year } — Map<Int, List<Student>>
    //   - .mapValues { (_, list) -> list.map { it.name } } — Map<Int, List<String>>
    //   - .mapValues { (_, list) -> list.maxByOrNull { it.gpa } } — top student per year
}
