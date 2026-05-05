package projects;
// PROJECT: Task Scheduler with Virtual Threads (Java 21 Project Loom — Exclusive)
// Virtual threads are lightweight threads that don't map 1:1 to OS threads.
// Run with: javac --release 21 TaskScheduler.java && java projects.TaskScheduler

public class TaskScheduler {

    // TODO 1: Create 1000 virtual threads with Thread.ofVirtual().start()
    //   for (int i = 0; i < 1000; i++) {
    //       final int taskId = i;
    //       Thread.ofVirtual().start(() -> {
    //           Thread.sleep(ThreadLocalRandom.current().nextLong(100, 500));
    //           System.out.println("Task " + taskId + " done on " + Thread.currentThread());
    //       });
    //   }
    //   - Notice: thread name shows "VirtualThread" not "Thread-N"

    // TODO 2: ExecutorService with virtual threads
    //   try (var exec = Executors.newVirtualThreadPerTaskExecutor()) {
    //       List<Future<String>> futures = exec.invokeAll(tasks);
    //       futures.forEach(f -> System.out.println(f.get()));
    //   }

    // TODO 3: Structured Concurrency (Java 21 preview — enable with --enable-preview)
    //   try (var scope = new StructuredTaskScope.ShutdownOnFailure()) {
    //       Future<String> user  = scope.fork(() -> fetchUser(userId));
    //       Future<String> order = scope.fork(() -> fetchOrders(userId));
    //       scope.join().throwIfFailed();
    //       System.out.println(user.get() + " " + order.get());
    //   }

    // TODO 4: Benchmark — compare platform thread pool vs virtual threads
    //   - Task: sleep 10ms (simulates I/O)
    //   - Platform: Executors.newFixedThreadPool(200) with 10_000 tasks
    //   - Virtual: Executors.newVirtualThreadPerTaskExecutor() with 10_000 tasks
    //   - Measure wall-clock time with System.nanoTime()

    // TODO 5: Pinning problem — demonstrate that synchronized blocks pin virtual threads
    //   - Use ReentrantLock instead of synchronized for virtual-thread-friendly locking

    public static void main(String[] args) throws Exception {
        System.out.println("TODO: implement virtual thread task scheduler");
    }
}
