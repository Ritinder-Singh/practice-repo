// TOPIC: Async/Await & Concurrency | swift 07_async.swift
// Docs: https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/

// TODO 1: async/await basics — async func fetchData() -> Data, await call, Task { }
// TODO 2: async let — parallel execution: async let user = fetchUser(), async let posts = fetchPosts()
// TODO 3: Task groups — withTaskGroup(of: Int.self) { group in group.addTask { } }
// TODO 4: Actors — actor BankAccount { var balance: Double; func deposit(_ amount: Double) }
// TODO 5: MainActor — @MainActor func updateUI(), await MainActor.run { }
// TODO 6: Sendable — @Sendable closures, Sendable protocol for value types crossing actor boundaries
// TODO 7: AsyncSequence — for await value in asyncStream { }, custom AsyncSequence
// TODO 8: Structured concurrency — cancellation propagation, Task.isCancelled, withTaskCancellationHandler
