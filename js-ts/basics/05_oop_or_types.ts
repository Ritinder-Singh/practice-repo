// =============================================================================
// TypeScript — OOP & Advanced Types
// =============================================================================
// Topics: classes, abstract, utility types, mapped types,
//         conditional types, template literals, decorators.
// Run: npx ts-node 05_oop_or_types.ts
// =============================================================================

// TODO 1: Abstract class hierarchy
//   abstract class Animal { abstract sound():string; move():string {...} }
//   class Dog extends Animal { sound() { return "woof"; } }
//   class Cat extends Animal { sound() { return "meow"; } }

// TODO 2: Utility types — build from scratch
//   type MyPartial<T>  = { [K in keyof T]?: T[K] }
//   type MyReadonly<T> = { readonly [K in keyof T]: T[K] }
//   type MyPick<T, K extends keyof T> = { [P in K]: T[P] }
//   type MyOmit<T, K extends keyof T> = MyPick<T, Exclude<keyof T, K>>
//   type MyRecord<K extends keyof any, V> = { [P in K]: V }

// TODO 3: Conditional types
//   type IsArray<T>   = T extends any[] ? true : false
//   type Flatten<T>   = T extends Array<infer U> ? U : T
//   type DeepPartial<T> = T extends object ? { [K in keyof T]?: DeepPartial<T[K]> } : T
//   type NonNullableDeep<T> = T extends null|undefined ? never : T extends object
//                             ? { [K in keyof T]: NonNullableDeep<T[K]> } : T

// TODO 4: Mapped types with modifiers
//   Remove optional:  { [K in keyof T]-?: T[K] }   (same as Required<T>)
//   Remove readonly:  { -readonly [K in keyof T]: T[K] }
//   Remap keys:       { [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K] }

// TODO 5: Template literal types — build accessor names
//   type Getters<T> = { [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K] }
//   type Setters<T> = { [K in keyof T as `set${Capitalize<string & K>}`]: (v:T[K]) => void }
//   type WithAccessors<T> = T & Getters<T> & Setters<T>

// TODO 6: Decorators (tsconfig: experimentalDecorators: true)
//   @log(target, key, desc) — logs args + return value
//   @memoize               — caches by JSON.stringify(args)
//   @readonly              — makes method non-writable
