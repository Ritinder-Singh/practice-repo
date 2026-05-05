package basics
// TOPIC: Advanced Kotlin | kotlinc 08_advanced.kt -include-runtime -d out.jar && java -jar out.jar
// Docs: https://kotlinlang.org/docs/kotlin-reference.html

fun main() {
    // TODO 1: DSL builders — buildList { add(1); add(2) }, apply, also, let, run, with
    //   - buildList { add("a"); add("b") } — stdlib DSL
    //   - apply: configures receiver, returns receiver (use for object init)
    //   - also: receives as 'it', returns receiver (use for side effects/logging)
    //   - let: receives as 'it', returns lambda result (use for null-safe transforms)
    //   - run: like apply but returns lambda result (use as expression)
    //   - with: non-extension, takes receiver as arg (use for calling multiple methods)

    // TODO 2: Reflection — KClass<*>, memberFunctions, callBy, annotations
    //   - val kClass = String::class
    //   - kClass.memberFunctions.forEach { println(it.name) }
    //   - kClass.constructors, kClass.memberProperties
    //   - Call a function by name: kClass.memberFunctions.first { it.name == "length" }
    //   - Read annotations: kClass.annotations, fun.findAnnotation<MyAnnotation>()
    //   - Note: requires kotlin-reflect dependency on classpath

    // TODO 3: Contracts — contract { returns() implies (value != null) } for smart cast hints
    //   - @OptIn(ExperimentalContracts::class)
    //   - fun requireNonNull(value: Any?): Unit { contract { returns() implies (value != null) }; require(value != null) }
    //   - After calling requireNonNull(x), Kotlin knows x is non-null (smart cast)
    //   - Also: contract { callsInPlace(block, InvocationKind.EXACTLY_ONCE) }

    // TODO 4: Context receivers (preview) — context(Logger) fun loggedOperation()
    //   - Compile with -Xcontext-receivers flag
    //   - interface Logger { fun log(msg: String) }
    //   - context(Logger) fun process(data: String) { log("Processing $data") }
    //   - Call with: with(consoleLogger) { process("hello") }
    //   - Note: may be replaced by context parameters in future Kotlin versions

    // TODO 5: Multiplatform expect/actual — expect fun currentTimeMs(): Long
    //   - expect fun currentTimeMs(): Long  — in commonMain
    //   - actual fun currentTimeMs(): Long = System.currentTimeMillis()  — in jvmMain
    //   - expect class Platform() { val name: String }
    //   - Use case: shared business logic with platform-specific implementations

    // TODO 6: Inline classes (value classes) — @JvmInline value class UserId(val id: Int)
    //   - @JvmInline value class UserId(val id: Int)
    //   - @JvmInline value class Email(val address: String)
    //   - Compile to their underlying type (Int, String) at runtime — zero overhead
    //   - Prevents mixing up UserId and PostId even though both are Ints at runtime
    //   - Can have methods and implement interfaces

    // TODO 7: Property delegates — ReadOnlyProperty, ReadWriteProperty, Delegates.observable
    //   - Delegates.observable("initial") { prop, old, new -> println("$old -> $new") }
    //   - Delegates.vetoable(0) { _, old, new -> new >= old }  — reject invalid updates
    //   - Custom delegate: class CachedProperty<T>(val compute: () -> T) : ReadOnlyProperty<Any?, T>
    //   - Map delegate: val name: String by map  — store properties in a Map
    //   - by lazy (revisited): LazyThreadSafetyMode.NONE for single-thread perf

    // TODO 8: Annotation processing — @Target, @Retention, runtime annotation reading via reflection
    //   - @Target(AnnotationTarget.CLASS, AnnotationTarget.FUNCTION)
    //   - @Retention(AnnotationRetention.RUNTIME)
    //   - annotation class Logged(val level: String = "INFO")
    //   - Read at runtime: MyClass::class.findAnnotation<Logged>()?.level
    //   - Note: compile-time annotation processing (KAPT/KSP) requires separate tooling
}
