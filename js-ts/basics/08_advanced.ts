// =============================================================================
// TypeScript — Advanced Type-Level Programming
// =============================================================================
// Topics: infer, recursive types, string manipulation types, tuple ops,
//         module augmentation, type-safe event emitter (Exclusive project).
// Run: npx ts-node 08_advanced.ts
// Ref: github.com/type-challenges/type-challenges
// =============================================================================

// TODO 1: Deep utility types
//   type DeepPartial<T>  = T extends object ? { [K in keyof T]?: DeepPartial<T[K]> } : T
//   type DeepReadonly<T> = T extends object ? { readonly [K in keyof T]: DeepReadonly<T[K]> } : T
//   type DeepRequired<T> = T extends object ? { [K in keyof T]-?: DeepRequired<T[K]> } : T

// TODO 2: String manipulation at type level
//   type TrimLeft<S>  = S extends ` ${infer R}` ? TrimLeft<R> : S
//   type Trim<S>      = TrimLeft<TrimRight<S>>
//   type CamelToSnake<S> — "camelCase" → "camel_case" (recursive with infer)
//   type SnakeToCamel<S> — "snake_case" → "snakeCase"

// TODO 3: Tuple manipulation types
//   type Head<T extends any[]>   = T extends [infer H, ...any[]] ? H : never
//   type Tail<T extends any[]>   = T extends [any, ...infer T] ? T : never
//   type Push<T extends any[],V> = [...T, V]
//   type Zip<T extends any[], U extends any[]> = ...  (recursive)

// TODO 4: Extract route params from string type
//   type ExtractParams<S extends string> =
//     S extends `${string}:${infer P}/${infer Rest}`
//       ? P | ExtractParams<`/${Rest}`>
//       : S extends `${string}:${infer P}` ? P : never
//   ExtractParams<"/users/:id/posts/:slug"> === "id" | "slug"

// TODO 5: Module augmentation — extend Express Request type
//   declare module "express-serve-static-core" {
//     interface Request { user?: { id:number; email:string; role:string } }
//   }
//   Now req.user is typed in all Express handlers.

// TODO 6: Type-safe EventEmitter (Exclusive project)
//   class TypedEmitter<Events extends Record<string, unknown>> {
//     on<E extends keyof Events>(event:E, handler:(data:Events[E])=>void): this
//     off<E extends keyof Events>(event:E, handler:(data:Events[E])=>void): this
//     emit<E extends keyof Events>(event:E, data:Events[E]): void
//     once<E extends keyof Events>(event:E, handler:(data:Events[E])=>void): this
//   }
//   interface AppEvents { login:{userId:string}; logout:{userId:string}; error:{msg:string} }
//   const emitter = new TypedEmitter<AppEvents>();
//   emitter.on("login", ({userId}) => ...);  // userId is string — fully typed
