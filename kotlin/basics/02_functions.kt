package basics
// TOPIC: Functions | kotlinc 02_functions.kt -include-runtime -d out.jar && java -jar out.jar
// Docs: https://kotlinlang.org/docs/functions.html

fun main() {
    // TODO 1: Default parameters — fun greet(name: String, greeting: String = "Hello")
    //   - Define greet() above main() with a default greeting
    //   - Call with one arg (uses default), then call with both args
    //   - Show that default params remove need for overloads

    // TODO 2: Named arguments — call with named params in any order
    //   - Call greet(greeting = "Hey", name = "Alice") in any order
    //   - Show how named args improve readability for boolean flags

    // TODO 3: Extension functions — fun String.isPalindrome(): Boolean
    //   - Define isPalindrome() as a String extension above main()
    //   - Call "racecar".isPalindrome() and "hello".isPalindrome()
    //   - Define a second extension: fun List<Int>.secondOrNull(): Int?

    // TODO 4: Higher-order functions — fun transform(list: List<Int>, fn: (Int) -> Int): List<Int>
    //   - Define transform() above main()
    //   - Call it with a lambda: transform(listOf(1,2,3)) { it * 2 }
    //   - Pass a function reference: transform(list, ::square)

    // TODO 5: Lambda with receiver — fun buildString(block: StringBuilder.() -> Unit): String
    //   - Define buildString() above main() (note: stdlib has one, define your own)
    //   - Use it: val s = myBuildString { append("Hello"); append(" World") }
    //   - Explain how the receiver (this = StringBuilder) is available inside the block

    // TODO 6: Inline functions — inline fun measure(block: () -> Unit): Long
    //   - Define measure() that records System.currentTimeMillis() before/after block
    //   - Use it: val elapsed = measure { /* some work */ }
    //   - Explain why inline avoids lambda allocation overhead

    // TODO 7: Operator overloading — data class Vector(val x: Int, val y: Int), operator fun plus
    //   - Define Vector data class above main()
    //   - Add operator fun plus(other: Vector): Vector
    //   - Add operator fun times(scalar: Int): Vector
    //   - Use: val v3 = Vector(1,2) + Vector(3,4)

    // TODO 8: Tail-recursive functions — tailrec fun factorial(n: Long, acc: Long = 1): Long
    //   - Define tailrec factorial() above main()
    //   - Call factorial(20L) and print result
    //   - Explain: tailrec compiles to a loop, preventing stack overflow
    //   - Also implement tailrec fibonacci(n: Int, a: Int = 0, b: Int = 1): Int
}
