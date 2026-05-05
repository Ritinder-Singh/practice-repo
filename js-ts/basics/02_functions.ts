// =============================================================================
// TypeScript — Functions
// =============================================================================
// Topics: overloads, generics, rest params, higher-order functions,
//         currying, type predicates, assertion functions, ParamSpec equivalent.
// Run: npx ts-node 02_functions.ts
// =============================================================================

// TODO 1: Function overloads
//   Implement reverse() that works on string OR number[]:
//   function reverse(s: string): string;
//   function reverse(arr: number[]): number[];
//   function reverse(input: string | number[]): string | number[] { ... }

// TODO 2: Generic functions
//   identity<T>(x: T): T
//   first<T>(arr: T[]): T | undefined
//   zip<T,U>(a: T[], b: U[]): [T,U][]
//   groupBy<T>(arr: T[], key: (x:T) => string): Record<string, T[]>
//   flatten<T>(arr: (T | T[])[]): T[]

// TODO 3: Higher-order: pipe
//   type Fn<A,B> = (a:A) => B
//   Implement pipe with overloads for 2, 3, 4 functions:
//   pipe(f, g)       — g(f(x))
//   pipe(f, g, h)    — h(g(f(x)))
//   TypeScript must enforce output of each = input of next.

// TODO 4: Currying
//   const add = (a: number, b: number) => a + b;
//   const curriedAdd = curry(add);
//   curriedAdd(1)(2); // 3
//   Implement curry<A,B,C>(fn: (a:A, b:B) => C): (a:A) => (b:B) => C

// TODO 5: Type predicates (is keyword)
//   function isString(val: unknown): val is string { return typeof val === "string"; }
//   Implement:
//   - isError(val: unknown): val is Error
//   - isNonNull<T>(val: T | null | undefined): val is NonNullable<T>
//   - hasProperty<T extends object, K extends string>(obj: T, key: K): obj is T & Record<K, unknown>

// TODO 6: Assertion functions (asserts keyword)
//   function assert(cond: boolean, msg: string): asserts cond
//   function assertDefined<T>(val: T): asserts val is NonNullable<T>
//   After calling assertDefined(x), TypeScript narrows x to NonNullable<T>.

// TODO 7: Memoize with type preservation
//   function memoize<T extends (...args: any[]) => any>(fn: T): T
//   Must return same type as input fn — use Parameters<T> and ReturnType<T>.
