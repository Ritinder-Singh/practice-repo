package basics;
// TOPIC: Async & Concurrency | javac AsyncConcurrency.java && java basics.AsyncConcurrency
import java.util.concurrent.*;
import java.util.concurrent.atomic.*;
import java.util.concurrent.locks.*;
import java.util.*;

public class AsyncConcurrency {
    public static void main(String[] args) throws Exception {
        // TODO 1: Thread — basic creation and lifecycle
        //   - Thread t = new Thread(() -> System.out.println("Hello from thread " + Thread.currentThread().getName()));
        //     t.setName("my-thread");
        //     t.start();      // starts new OS thread, calls run() asynchronously
        //     t.join();       // main thread waits for t to finish
        //   - Thread.sleep(1000);  // pauses current thread 1s (throws InterruptedException)
        //   - Thread states: NEW → RUNNABLE → BLOCKED/WAITING/TIMED_WAITING → TERMINATED
        //   - Daemon threads: t.setDaemon(true); — JVM exits when only daemon threads remain

        // TODO 2: Runnable vs Callable
        //   - Runnable: void run() — no return value, no checked exception
        //   - Callable<V>: V call() throws Exception — returns value, can throw
        //   - ExecutorService ex = Executors.newSingleThreadExecutor();
        //   - Future<Integer> future = ex.submit(() -> { Thread.sleep(500); return 42; });
        //   - System.out.println(future.get());  // blocks until result ready
        //   - future.get(1, TimeUnit.SECONDS);   // with timeout
        //   - future.isDone(), future.cancel(true)

        // TODO 3: ExecutorService — thread pool
        //   - ExecutorService pool = Executors.newFixedThreadPool(4);
        //   - Submit 10 tasks: pool.submit(() -> { ... })
        //   - Collect futures into List<Future<Integer>>
        //   - pool.shutdown();           // no new tasks accepted; existing tasks finish
        //   - pool.awaitTermination(10, TimeUnit.SECONDS);
        //   - pool.shutdownNow();        // interrupts running tasks
        //   - Other factory methods: newCachedThreadPool(), newScheduledThreadPool(n), newSingleThreadExecutor()

        // TODO 4: CompletableFuture — async composition
        //   - CompletableFuture<String> cf = CompletableFuture.supplyAsync(() -> fetchData())
        //       .thenApply(data -> process(data))         // transform result (sync)
        //       .thenApplyAsync(data -> furtherProcess())  // transform (async, new thread)
        //       .thenCompose(data -> CompletableFuture.supplyAsync(() -> anotherFetch()))  // flatMap
        //       .exceptionally(ex -> "default on error");
        //   - Combine multiple:
        //     CompletableFuture<Void> all = CompletableFuture.allOf(cf1, cf2, cf3);
        //     CompletableFuture<Object> any = CompletableFuture.anyOf(cf1, cf2, cf3);
        //   - cf.thenAccept(System.out::println).join();  // wait for completion

        // TODO 5: synchronized — thread-safe counter
        //   - Unsafe counter (demonstrate race condition):
        //     int count = 0;  // 10 threads each increment 1000x → result != 10000
        //   - synchronized method: synchronized void increment() { count++; }
        //   - synchronized block: synchronized (this) { count++; }
        //   - AtomicInteger: AtomicInteger atomicCount = new AtomicInteger(0);
        //     atomicCount.incrementAndGet(); atomicCount.addAndGet(5); atomicCount.compareAndSet(expected, update);
        //   - Benchmark: synchronized vs AtomicInteger performance for 10 threads × 100,000 increments

        // TODO 6: ReentrantLock — explicit locking
        //   - ReentrantLock lock = new ReentrantLock();
        //   - lock.lock(); try { /* critical section */ } finally { lock.unlock(); }  // ALWAYS unlock in finally
        //   - tryLock with timeout: if (lock.tryLock(500, TimeUnit.MILLISECONDS)) { ... }
        //   - lock.isHeldByCurrentThread(), lock.getQueueLength()
        //   - ReentrantReadWriteLock: allow concurrent reads, exclusive writes
        //     ReadWriteLock rwLock = new ReentrantReadWriteLock();
        //     rwLock.readLock().lock() / rwLock.writeLock().lock()

        // TODO 7: BlockingQueue — producer-consumer pattern
        //   - BlockingQueue<Integer> queue = new ArrayBlockingQueue<>(10);  // capacity 10
        //   - Producer thread: queue.put(item);    // blocks if full
        //   - Consumer thread: int item = queue.take();  // blocks if empty
        //   - Non-blocking variants: offer(item, timeout, unit), poll(timeout, unit)
        //   - Demonstrate with 2 producers and 3 consumers, each producing/consuming 50 items
        //   - Use poison pill pattern to signal consumers to stop (e.g., put(-1))

        // TODO 8: Virtual threads (Java 21) — Project Loom
        //   - Platform thread: Thread.ofPlatform().start(() -> doWork());  // OS thread, ~1MB stack
        //   - Virtual thread:  Thread.ofVirtual().start(() -> doWork());   // JVM-managed, ~1KB
        //   - Thread.startVirtualThread(runnable);  // shorthand
        //   - VT executor: try (var exec = Executors.newVirtualThreadPerTaskExecutor()) {
        //       for (int i = 0; i < 10_000; i++) exec.submit(() -> { Thread.sleep(100); return null; });
        //     }  // 10,000 virtual threads — negligible overhead
        //   - Virtual threads are ideal for I/O-bound tasks; pinning pitfall: avoid synchronized in VT (use ReentrantLock)
        //   - Compare: launch 100,000 virtual threads vs fixed pool of 200 platform threads — time the difference
    }
}
