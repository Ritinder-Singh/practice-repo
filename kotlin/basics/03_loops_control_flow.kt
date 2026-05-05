package basics
// TOPIC: Loops & Control Flow | kotlinc 03_loops_control_flow.kt -include-runtime -d out.jar && java -jar out.jar
// Docs: https://kotlinlang.org/docs/control-flow.html

fun main() {
    // TODO 1: Ranges — for (i in 1..10), downTo, step, until
    //   - Print 1..10 inclusive
    //   - Print 10 downTo 1
    //   - Print 0 until 10 step 2 (evens, exclusive upper bound)
    //   - Use a range in an if condition: if (score in 90..100)

    // TODO 2: when expression — replaces switch, use as expression returning value
    //   - val grade = when (score) { in 90..100 -> "A"; in 80..89 -> "B"; else -> "F" }
    //   - when on a sealed class (exhaustive, no else needed)
    //   - when without argument: when { x > 0 -> "positive"; else -> "non-positive" }

    // TODO 3: while & do-while — FizzBuzz 1-100
    //   - Implement FizzBuzz using a while loop
    //   - Show do-while: var input: String; do { input = readLine()!! } while (input.isBlank())

    // TODO 4: break/continue with labels — @outer label to break nested loop
    //   - Nested loop searching for a value, break@outer when found
    //   - continue@outer to skip to next outer iteration
    //   - Show the difference between plain break and labeled break

    // TODO 5: Collection operations — filter, map, reduce, fold, groupBy, partition
    //   - val nums = (1..20).toList()
    //   - filter { it % 2 == 0 }, map { it * it }
    //   - reduce { acc, n -> acc + n } vs fold(0) { acc, n -> acc + n }
    //   - groupBy { if (it % 3 == 0) "fizz" else "other" }
    //   - partition { it > 10 } — returns Pair<List,List>

    // TODO 6: Sequences — asSequence() for lazy evaluation, compare with eager List ops
    //   - (1..1_000_000).asSequence().filter { it % 2 == 0 }.map { it * it }.first()
    //   - Compare with eager list version: note sequences short-circuit on terminal op
    //   - generateSequence(1) { it + 1 }.take(10).toList()

    // TODO 7: forEach vs for — when to use each, forEach with index (forEachIndexed)
    //   - for loop: prefer when you need break/continue
    //   - forEach: cleaner for full iteration, no early exit
    //   - forEachIndexed { index, value -> println("$index: $value") }
    //   - mapIndexed { index, value -> "$index=$value" }

    // TODO 8: repeat — repeat(5) { println("Hello $it") }
    //   - repeat(5) { println("Hello $it") } — it is the zero-based iteration index
    //   - Use repeat to build a string: val s = buildString { repeat(3) { append("ha") } }
    //   - Show difference vs for loop — repeat is for simple side-effect repetition
}
