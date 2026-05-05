// =============================================================================
// TypeScript — Loops & Control Flow
// =============================================================================
// Topics: for..of, for..in, array methods chain, generators,
//         Symbol.iterator, exhaustive checks with never.
// Run: npx ts-node 03_loops_control_flow.ts
// =============================================================================

// TODO 1: for..of vs for..in
//   for..of → values (arrays, sets, maps, strings, generators)
//   for..in → keys (plain objects — prefer Object.entries)
//   Iterate over Map<string,number>, Set<string>, string with for..of

// TODO 2: Array method chain (one expression, no temp vars)
//   orders: { id, product, price, qty, status }[]
//   Filter completed → map to total=price*qty → filter total>100 → sort desc → reduce sum

// TODO 3: Generator functions
//   function* counter(start=0, step=1): Generator<number>   // infinite
//   function* range(start:number, end:number, step=1): Generator<number>
//   function* lazyMap<T,U>(gen: Generator<T>, fn:(x:T)=>U): Generator<U>

// TODO 4: Custom iterable with Symbol.iterator
//   Make LinkedList<T> iterable:
//   [Symbol.iterator](): Iterator<T> { let cur = this.head; return { next() { ... } } }

// TODO 5: Exhaustive checks with never
//   type Shape = { kind:"circle"; r:number } | { kind:"rect"; w:number; h:number };
//   function area(s: Shape): number {
//     switch(s.kind) {
//       case "circle": return Math.PI * s.r ** 2;
//       case "rect":   return s.w * s.h;
//       default:
//         const _: never = s;  // compile error if case added but not handled
//         throw new Error("unreachable");
//     }
//   }

// TODO 6: Async iteration
//   async function* paginate<T>(url:string): AsyncGenerator<T[]>
//   Yield one page at a time. Use: for await (const page of paginate(...)) { ... }
