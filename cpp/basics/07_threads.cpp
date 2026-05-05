#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <atomic>
#include <future>
#include <vector>
// TOPIC: Threads & Concurrency | g++ -std=c++20 -o out 07_threads.cpp -pthread && ./out

int main() {
    // TODO 1: std::thread — basic spawn + join
    //   auto worker = [](int id) { std::cout << "Worker " << id << "\n"; };
    //   std::thread t(worker, 42);
    //   t.join();   // or t.detach() (runs independently, can't join)

    // TODO 2: std::mutex + lock_guard
    //   std::mutex mu; int counter = 0;
    //   auto inc = [&] { for (int i = 0; i < 1000; ++i) { std::lock_guard lock(mu); counter++; } };
    //   std::thread t1(inc), t2(inc); t1.join(); t2.join();
    //   // counter should be 2000

    // TODO 3: std::condition_variable — signal between threads
    //   std::mutex mu; std::condition_variable cv; bool ready = false;
    //   // Producer: { std::lock_guard lk(mu); ready=true; } cv.notify_one();
    //   // Consumer: { std::unique_lock lk(mu); cv.wait(lk, []{ return ready; }); }

    // TODO 4: std::atomic — lock-free operations
    //   std::atomic<int> count{0};
    //   count.fetch_add(1);           // atomic increment
    //   count.compare_exchange_strong(expected, desired);  // CAS

    // TODO 5: std::async + std::future
    //   auto fut = std::async(std::launch::async, []{ return 42; });
    //   int result = fut.get();   // blocks until done

    // TODO 6: std::promise / std::future pair
    //   std::promise<int> p; std::future<int> f = p.get_future();
    //   std::thread t([&p]{ p.set_value(99); });
    //   std::cout << f.get() << "\n";  // prints 99
    //   t.join();

    // TODO 7: Thread pool with std::queue + condition_variable
    //   // Workers: wait on cv, pop job from queue, execute
    //   // Submit: push job, notify_one
    //   // Shutdown: set done=true, notify_all, join all threads

    // TODO 8: std::jthread (C++20) — auto-joining, stoppable
    //   std::jthread t([](std::stop_token st) {
    //       while (!st.stop_requested()) { /* do work */ }
    //   });
    //   t.request_stop();  // signals stop; join called in destructor

    std::cout << "TODO: implement thread exercises\n";
    return 0;
}
