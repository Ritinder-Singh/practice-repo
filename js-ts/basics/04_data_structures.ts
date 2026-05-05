// =============================================================================
// TypeScript — Data Structures
// =============================================================================
// Topics: generic Stack/Queue, Map vs Object, Set operations,
//         typed arrays, binary heap / priority queue.
// Run: npx ts-node 04_data_structures.ts
// =============================================================================

// TODO 1: Generic Stack<T>
//   push(item:T): void | pop(): T|undefined | peek(): T|undefined
//   get size(): number | isEmpty(): boolean | [Symbol.iterator](): Iterator<T>

// TODO 2: Generic Queue<T> using two stacks (amortized O(1))
//   enqueue / dequeue / peek

// TODO 3: Map utilities
//   wordFrequency(text:string): Map<string,number>
//   invertMap<K,V>(m: Map<K,V>): Map<V,K[]>   — handle duplicate values
//   mergeMap<K,V>(a: Map<K,V>, b: Map<K,V>, resolve:(a:V,b:V)=>V): Map<K,V>

// TODO 4: Set operations (generic)
//   union<T>, intersection<T>, difference<T>, isSubset<T>

// TODO 5: Priority Queue using min-heap
//   class PriorityQueue<T> {
//     constructor(private cmp: (a:T, b:T) => number) {}
//     enqueue(item:T): void   // O(log n) — sift up
//     dequeue(): T|undefined  // O(log n) — sift down
//     peek(): T|undefined     // O(1)
//   }
//   Internal array representation: parent at i, children at 2i+1, 2i+2

// TODO 6: LRU Cache in TypeScript
//   class LRUCache<K,V> {
//     constructor(private capacity: number) {}
//     get(key:K): V|undefined
//     put(key:K, val:V): void
//   }
//   Use Map (preserves insertion order) for O(1) operations.
