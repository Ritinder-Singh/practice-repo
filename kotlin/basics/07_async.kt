package basics
// TOPIC: Coroutines & Async | kotlinc 07_async.kt -include-runtime -d out.jar && java -jar out.jar
// Requires: kotlinx-coroutines-core — add to classpath or use Gradle/Maven
// Docs: https://kotlinlang.org/docs/coroutines-overview.html

fun main() {
    // TODO 1: runBlocking + launch — basic coroutine, delay instead of sleep
    //   - runBlocking { } to bridge blocking world and coroutines
    //   - launch { delay(1000); println("done") } — fire-and-forget
    //   - delay() is non-blocking (suspends coroutine, frees thread)
    //   - join() a Job to wait for it: val job = launch { ... }; job.join()

    // TODO 2: async/await — async { fetchUser() }, async { fetchPosts() }, awaitAll()
    //   - val userDeferred = async { fetchUser() }
    //   - val postsDeferred = async { fetchPosts() }
    //   - Both run concurrently; await each: userDeferred.await()
    //   - awaitAll(userDeferred, postsDeferred) — wait for all at once
    //   - Measure total time: should be max(t1, t2) not t1+t2

    // TODO 3: Flows — flow { emit(1); emit(2) }, collect, map, filter, flowOn
    //   - val numberFlow = flow { for (i in 1..5) { emit(i); delay(100) } }
    //   - numberFlow.collect { println(it) }
    //   - numberFlow.map { it * 2 }.filter { it > 4 }.collect { ... }
    //   - flowOn(Dispatchers.IO) to change upstream context
    //   - Terminal operators: collect, toList, first, single, reduce

    // TODO 4: Channels — producer-consumer with Channel<Int>(capacity=10)
    //   - val channel = Channel<Int>(capacity = 10)
    //   - Producer coroutine: channel.send(item); channel.close()
    //   - Consumer coroutine: for (item in channel) { process(item) }
    //   - produce { } builder creates a ReceiveChannel
    //   - Channel types: UNLIMITED, BUFFERED, RENDEZVOUS, CONFLATED

    // TODO 5: Structured concurrency — coroutineScope, supervisorScope, cancellation propagation
    //   - coroutineScope { }: fails fast — any child failure cancels all siblings
    //   - supervisorScope { }: isolated failures — siblings continue on child failure
    //   - Cancellation is cooperative: check isActive or use cancellable suspend fns
    //   - withTimeout(3000L) { ... } — cancels block after timeout

    // TODO 6: withContext — switch dispatchers: IO, Default, Main
    //   - Dispatchers.IO: for blocking I/O (file, network, DB)
    //   - Dispatchers.Default: for CPU-intensive work (sorting, parsing)
    //   - Dispatchers.Main: for UI updates (Android)
    //   - withContext(Dispatchers.IO) { readFile() } — suspends, doesn't block

    // TODO 7: StateFlow & SharedFlow — hot flows for state management
    //   - val stateFlow = MutableStateFlow(0) — always has current value, replays to new collectors
    //   - stateFlow.value = 1; stateFlow.update { it + 1 }
    //   - val sharedFlow = MutableSharedFlow<Event>() — no initial value, configurable replay
    //   - sharedFlow.emit(Event.Click); sharedFlow.collect { handle(it) }
    //   - Use case: StateFlow for UI state, SharedFlow for one-time events

    // TODO 8: Mutex — Mutex().withLock { } for coroutine-safe shared state
    //   - val mutex = Mutex()
    //   - var counter = 0
    //   - launch { mutex.withLock { counter++ } }
    //   - Compare with atomic operations: AtomicInteger (but prefer structured concurrency)
    //   - Show race condition without mutex, then fix it
}
