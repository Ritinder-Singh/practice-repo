package basics
// TOPIC: OOP & Type System | kotlinc 05_oop_or_types.kt -include-runtime -d out.jar && java -jar out.jar
// Docs: https://kotlinlang.org/docs/classes.html

fun main() {
    // TODO 1: Open classes & inheritance — open class Animal, class Dog : Animal()
    //   - Define open class Animal(val name: String) with open fun speak(): String
    //   - Define class Dog : Animal(name) that overrides speak()
    //   - Define class Cat : Animal(name) with its own override
    //   - Show that non-open classes cannot be subclassed (final by default)

    // TODO 2: Interfaces — multiple interface implementation, default implementations
    //   - interface Flyable { fun fly(): String }
    //   - interface Swimmable { fun swim(): String = "splashing" }  // default impl
    //   - class Duck : Flyable, Swimmable { override fun fly() = "flapping" }
    //   - Show diamond problem resolution: override required when two defaults conflict

    // TODO 3: Abstract classes — abstract class Shape with abstract fun area(): Double
    //   - abstract class Shape(val color: String) with abstract fun area(): Double
    //   - Non-abstract fun describe() that calls area()
    //   - class Circle(val radius: Double, color: String) : Shape(color)
    //   - class Rectangle(val w: Double, val h: Double, color: String) : Shape(color)

    // TODO 4: Generics — class Box<T>(val value: T), in/out variance keywords
    //   - class Box<T>(val value: T) with fun unwrap(): T
    //   - out (covariant): interface Producer<out T> { fun produce(): T }
    //   - in (contravariant): interface Consumer<in T> { fun consume(item: T) }
    //   - Reified type parameter: inline fun <reified T> isInstance(value: Any): Boolean

    // TODO 5: Type aliases — typealias UserId = Int, typealias Handler = (String) -> Unit
    //   - typealias UserId = Int
    //   - typealias StringPredicate = (String) -> Boolean
    //   - typealias UserMap = Map<UserId, String>
    //   - Show how aliases improve readability without runtime overhead

    // TODO 6: Delegation — class LoggingList<T>(list: MutableList<T> = mutableListOf()) : MutableList<T> by list
    //   - Implement LoggingList that overrides add() to print before delegating
    //   - All other MutableList methods are auto-delegated to the wrapped list
    //   - Show property delegation with: var p: String by Delegates.observable("init") { _, old, new -> ... }

    // TODO 7: lateinit vs lazy — lateinit var db: Database vs val config by lazy { loadConfig() }
    //   - lateinit var: use for DI or setup-before-use, only for var, only non-null reference types
    //     - Check with ::field.isInitialized before accessing
    //   - lazy: evaluated on first access, thread-safe by default (LazyThreadSafetyMode)
    //     - val heavyObject by lazy { ExpensiveClass() }
    //   - Show the UninitializedPropertyAccessException if lateinit accessed early

    // TODO 8: Smart casts — is checks, as? safe cast, as unsafe cast with exception
    //   - if (shape is Circle) shape.radius  — smart cast inside if block
    //   - when (shape) { is Circle -> ...; is Rectangle -> ... }
    //   - val circle = shape as? Circle  — returns null if not Circle
    //   - val circle = shape as Circle   — throws ClassCastException if not Circle
    //   - Show that smart cast fails when var could be changed by another thread
}
