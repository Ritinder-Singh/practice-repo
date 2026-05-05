# TOPIC: Threads & Fibers | ruby 07_async.rb
# Docs: https://ruby-doc.org/core/Thread.html

# TODO 1: Thread.new — launch threads, join, capture return value
#   threads = (1..5).map { |i| Thread.new { sleep(rand * 0.1); i * i } }
#   results = threads.map(&:value)
#   puts results.inspect
#   - Thread#value blocks until thread finishes and returns the block result

# TODO 2: Mutex for thread-safe shared state
#   mutex = Mutex.new
#   counter = 0
#   threads = 10.times.map { Thread.new { 1000.times { mutex.synchronize { counter += 1 } } } }
#   threads.each(&:join)
#   puts counter  # should be 10_000 (not less due to race conditions)

# TODO 3: Queue (thread-safe) for producer-consumer
#   require 'thread'
#   queue = Queue.new
#   producer = Thread.new { 10.times { |i| queue.push(i); sleep 0.01 } }
#   consumer = Thread.new { loop { item = queue.pop; break if item == :stop; puts "Got #{item}" } }
#   producer.join; queue.push(:stop); consumer.join

# TODO 4: Fiber — cooperative coroutines (manual yield/resume)
#   fib = Fiber.new do
#     a, b = 0, 1
#     loop { Fiber.yield(a); a, b = b, a + b }
#   end
#   10.times { print "#{fib.resume} " }
#   - Fibers are NOT threads — single-threaded, explicit scheduling

# TODO 5: Ractor (Ruby 3+) — parallel execution without GVL
#   r = Ractor.new { Ractor.recv * 2 }
#   r.send(21)
#   puts r.take  # => 42
#   - Only Ractors can share state safely; objects must be shareable

# TODO 6: Thread.abort_on_exception
#   Thread.abort_on_exception = true  # unhandled exception in thread kills main program
#   - Default: exceptions in threads are silently swallowed unless joined
#   - Alternative: Thread.report_on_exception = true (Ruby 2.4+)

# TODO 7: Async gem — non-blocking I/O with fibers (external gem)
#   # require 'async'
#   # Async do |task|
#   #   5.times { task.async { |t| t.sleep(rand); puts "done" } }
#   # end

# TODO 8: GVL (Global VM Lock) explanation
#   # MRI Ruby has a GVL — only one thread runs Ruby code at a time
#   # Threads CAN run in parallel during C extensions and I/O (e.g., sleep, HTTP)
#   # For CPU-parallel work: use Ractor (Ruby 3+) or fork processes
#   # Demonstrate: two CPU-bound threads vs two I/O-bound threads
