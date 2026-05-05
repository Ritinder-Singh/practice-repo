// =============================================================================
// TypeScript — Async/Await & Promises
// =============================================================================
// Topics: Promise combinators, retry, AbortController, async generators,
//         rate limiting, event-to-promise conversion.
// Run: npx ts-node 07_async.ts
// Docs: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
// =============================================================================

// TODO 1: delay utility + Promise chaining vs async/await comparison
//   const delay = (ms:number) => new Promise<void>(r => setTimeout(r, ms))
//   Show: .then chain vs async/await are equivalent transforms

// TODO 2: Promise combinators
//   Promise.all     — all resolve or first rejection
//   Promise.allSettled — all settle (success or fail), never rejects
//   Promise.race    — first to settle (resolve or reject)
//   Promise.any     — first to RESOLVE (AggregateError if all reject)
//   Demonstrate each with a set of mock async operations

// TODO 3: Retry with exponential backoff
//   interface RetryOptions { attempts:number; delayMs:number; backoff?:number }
//   async function retry<T>(fn:()=>Promise<T>, opts:RetryOptions): Promise<T>
//   On failure: wait delayMs * (backoff^attempt) before next try

// TODO 4: fetchWithTimeout using AbortController
//   async function fetchWithTimeout<T>(url:string, ms:number): Promise<T>
//   const ctrl = new AbortController();
//   setTimeout(() => ctrl.abort(), ms);
//   fetch(url, { signal: ctrl.signal })

// TODO 5: Async generator — paginated fetcher
//   async function* fetchPages<T>(url:string): AsyncGenerator<T[]>
//   Lazily fetches pages until empty array returned.
//   for await (const page of fetchPages("/api/items")) { process(page) }

// TODO 6: Semaphore — limit concurrent async operations
//   class Semaphore {
//     constructor(private permits:number) {}
//     async acquire(): Promise<void>
//     release(): void
//   }
//   Use: async function rateLimitedFetch<T>(urls:string[], limit:number): Promise<T[]>

// TODO 7: once() — event to Promise
//   function once<T>(emitter: EventEmitter, event:string): Promise<T>
//   Returns a Promise that resolves on next emit of event.
