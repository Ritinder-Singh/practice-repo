// TOPIC: Error Handling | swift 06_error_handling.swift
// Docs: https://docs.swift.org/swift-book/documentation/the-swift-programming-language/errorhandling/

// TODO 1: Error protocol — enum NetworkError: Error { case notFound, timeout, serverError(Int) }
// TODO 2: throws/try/catch — func fetchUser(id: Int) throws -> User, do-catch block
// TODO 3: try? and try! — convert throwing to Optional or force (with crash risk)
// TODO 4: Result type — Result<User, NetworkError>, .success/.failure, map, flatMap
// TODO 5: rethrows — func transform<T>(_ value: T, using fn: (T) throws -> T) rethrows -> T
// TODO 6: Multiple catch patterns — catch NetworkError.notFound { } catch let e as NetworkError { }
// TODO 7: defer in error handling — defer { connection.close() } runs even after throw
// TODO 8: Custom error with localized description — implement LocalizedError protocol
