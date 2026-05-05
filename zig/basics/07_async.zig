const std = @import("std");
// TOPIC: Threads & Concurrency | zig run 07_async.zig
// Note: Zig removed async/await in 0.12+ (they are being redesigned)
// This file covers std.Thread and synchronization primitives

pub fn main() !void {
    // TODO 1: std.Thread.spawn — create OS thread
    //   const thread = try std.Thread.spawn(.{}, workerFn, .{42});
    //   thread.join();  // wait for completion
    //   fn workerFn(id: u32) void {
    //       std.debug.print("Worker {d} running on thread {d}\n", .{id, std.Thread.getCurrentId()});
    //   }

    // TODO 2: Mutex — mutual exclusion
    //   var mutex = std.Thread.Mutex{};
    //   var counter: u32 = 0;
    //   fn increment() void {
    //       mutex.lock();
    //       defer mutex.unlock();
    //       counter += 1;
    //   }
    //   // Spawn 10 threads each incrementing 1000 times
    //   // Result should be 10000

    // TODO 3: Semaphore — limit concurrent access
    //   var sem = std.Thread.Semaphore{ .permits = 3 };  // max 3 concurrent
    //   fn worker(i: u32) void {
    //       sem.wait();
    //       defer sem.post();
    //       std.debug.print("Worker {d} running\n", .{i});
    //       std.time.sleep(100 * std.time.ns_per_ms);
    //   }

    // TODO 4: Condition variable — signal between threads
    //   var mutex = std.Thread.Mutex{};
    //   var cond  = std.Thread.Condition{};
    //   var ready = false;
    //   fn producer() void {
    //       mutex.lock(); defer mutex.unlock();
    //       ready = true;
    //       cond.signal();
    //   }
    //   fn consumer() void {
    //       mutex.lock(); defer mutex.unlock();
    //       while (!ready) cond.wait(&mutex);
    //       std.debug.print("Consumer: data is ready\n", .{});
    //   }

    // TODO 5: Atomic operations
    //   var atomic_counter = std.atomic.Value(u32).init(0);
    //   fn atomicIncrement() void {
    //       _ = atomic_counter.fetchAdd(1, .seq_cst);
    //   }

    // TODO 6: Thread pool pattern
    //   // Spawn N workers, feed work via channel (use Mutex + ArrayList as queue)
    //   // Worker loop: lock, check queue, pop item, unlock, process
    //   // Demonstrates producer-consumer with bounded buffer

    // TODO 7: std.Thread.sleep
    //   std.time.sleep(500 * std.time.ns_per_ms);  // sleep 500ms
    //   // Compare: sleep does NOT yield to other Zig threads (OS sleep)

    // TODO 8: Async I/O (future — Zig async/await redesign in progress)
    //   // See: https://github.com/ziglang/zig/issues/6025
    //   // Current approach: use OS threads or io_uring (linux) for async I/O
    //   // std.io.poll for multiplexed I/O

    std.debug.print("TODO: implement thread exercises\n", .{});
}
