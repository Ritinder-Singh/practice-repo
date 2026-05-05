package basics
// TOPIC: Variables & Types | kotlinc 01_variables_types.kt -include-runtime -d out.jar && java -jar out.jar
// Docs: https://kotlinlang.org/docs/basic-types.html

fun main() {
    // TODO 1: val vs var — immutability, smart cast after null check
    //   - Declare a val and try to reassign it (should fail to compile)
    //   - Declare a var and reassign it
    //   - Show smart cast: if (x != null) use x as non-null without !!

    // TODO 2: Nullable types — String?, ?.let, ?: elvis operator, !! operator (when safe)
    //   - Declare nullable String?, call ?.length
    //   - Use ?.let { } to run a block only when non-null
    //   - Use ?: to provide a default: val len = s?.length ?: 0
    //   - Use !! only when you are certain it is non-null, show the NPE risk

    // TODO 3: Type inference — let Kotlin infer types, use explicit annotation when ambiguous
    //   - val x = 42 (inferred Int), val pi = 3.14 (inferred Double)
    //   - Show when explicit annotation matters: val items: List<String> = emptyList()

    // TODO 4: Data classes — data class Person(val name: String, val age: Int), copy(), componentN()
    //   - Define Person data class above main()
    //   - Create instance, print it (auto toString)
    //   - Use copy() to make a modified clone
    //   - Show component1(), component2() calls

    // TODO 5: Sealed classes — sealed class Result<T>: Success(val data: T), Failure(val error: String)
    //   - Define sealed class Result<T> with Success and Failure subclasses above main()
    //   - Use when expression to handle each branch exhaustively

    // TODO 6: Object declarations — singleton object AppConfig with constants
    //   - Define object AppConfig { const val BASE_URL = "..."; val timeout = 30 }
    //   - Access AppConfig.BASE_URL from main()

    // TODO 7: Companion objects — factory method inside class, @JvmStatic annotation
    //   - Define class User with companion object { fun fromJson(json: String): User }
    //   - Call User.fromJson("...") from main()
    //   - Add @JvmStatic to make it callable from Java without Companion qualifier

    // TODO 8: Destructuring — (name, age) = person; for ((k,v) in map)
    //   - Destructure a Person into (name, age)
    //   - Iterate a mapOf<String,Int> using for ((key, value) in map)
    //   - Destructure a Pair with (first, second)
}
