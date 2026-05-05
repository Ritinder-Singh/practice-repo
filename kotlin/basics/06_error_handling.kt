package basics
// TOPIC: Error Handling | kotlinc 06_error_handling.kt -include-runtime -d out.jar && java -jar out.jar
// Docs: https://kotlinlang.org/docs/exceptions.html

fun main() {
    // TODO 1: try-catch-finally — catch Exception, multiple catch blocks
    //   - Wrap parseInt in try-catch-finally
    //   - Catch NumberFormatException specifically, then catch Exception as fallback
    //   - finally block always runs — use for cleanup (close resources)
    //   - Note: Kotlin has no checked exceptions (unlike Java)

    // TODO 2: Result type — Result.success / Result.failure, runCatching, getOrElse, fold
    //   - val result = runCatching { "abc".toInt() }
    //   - result.isSuccess, result.isFailure
    //   - result.getOrElse { 0 }, result.getOrDefault(0)
    //   - result.fold(onSuccess = { it * 2 }, onFailure = { -1 })
    //   - Chain: runCatching { ... }.map { transform(it) }.recover { fallback }

    // TODO 3: Custom exceptions — class DatabaseException(msg: String, cause: Throwable?) : Exception(msg, cause)
    //   - Define DatabaseException above main()
    //   - Define NotFoundException(val id: Int) : RuntimeException("Not found: $id")
    //   - Throw, catch, and re-throw with cause (exception chaining)

    // TODO 4: require/check/error — precondition checks, IllegalArgumentException
    //   - require(age >= 0) { "Age must be non-negative, got $age" }  — IAE
    //   - check(isInitialized) { "Must call init() first" }  — ISE
    //   - error("Unreachable code reached")  — always throws ISE
    //   - requireNotNull(value) { "Value must not be null" }

    // TODO 5: Elvis with throw — val user = findUser(id) ?: throw NotFoundException("User $id not found")
    //   - Define findUser(id: Int): User? above main() returning null for unknown IDs
    //   - Use elvis-throw pattern to short-circuit
    //   - Chain: findUser(id)?.takeIf { it.isActive } ?: throw InactiveUserException(id)

    // TODO 6: Sealed class for errors — sealed class ApiError: NotFound, Unauthorized, ServerError(val code: Int)
    //   - Define sealed class ApiError above main()
    //   - object NotFound : ApiError()
    //   - object Unauthorized : ApiError()
    //   - class ServerError(val code: Int) : ApiError()
    //   - Use when to handle exhaustively — no else needed

    // TODO 7: try as expression — val result = try { parseInt(s) } catch (e: Exception) { 0 }
    //   - Assign the result of try-catch directly to a val
    //   - Both try block and catch block must produce the same type
    //   - Combine with when: val parsed = try { s.toInt() } catch (e: NumberFormatException) { null }

    // TODO 8: Coroutine exception handling — CoroutineExceptionHandler, SupervisorJob
    //   - Note: requires kotlinx-coroutines dependency; leave as conceptual TODOs
    //   - CoroutineExceptionHandler { _, throwable -> println("Error: $throwable") }
    //   - SupervisorJob: child failure does NOT cancel siblings or parent
    //   - supervisorScope { } vs coroutineScope { } — failure propagation difference
    //   - Use try-catch inside a coroutine for local handling
}
