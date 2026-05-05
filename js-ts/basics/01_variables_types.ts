// =============================================================================
// TypeScript — Variables & Types
// =============================================================================
// Topics: primitives, type inference, union/intersection, literal types,
//         const assertions, interfaces vs type aliases, satisfies operator.
// Run: npx ts-node 01_variables_types.ts
// Docs: https://www.typescriptlang.org/docs/handbook/2/everyday-types.html
// =============================================================================

// TODO 1: Primitive types — explicit vs inferred
//   let x: number = 42;  vs  let x = 42;   (inferred)
//   const PI = 3.14;     // literal type 3.14, NOT number
//   Zero values: undefined (declared not assigned), never vs unknown
//   Show typeof narrowing: if (typeof val === "string") { val.toUpperCase() }

// TODO 2: Union and intersection types
//   type StringOrNumber = string | number;
//   type Named = { name: string };
//   type Aged  = { age: number };
//   type Person = Named & Aged;
//   Write: function formatId(id: string | number): string
//     — "#42" for numbers, "ID-abc" for strings. Use typeof to narrow.

// TODO 3: Literal types + const assertions
//   type Direction = "north" | "south" | "east" | "west";
//   const COLORS = ["red", "green", "blue"] as const;
//   type Color = typeof COLORS[number];   // "red" | "green" | "blue"
//   Write: function isValidColor(s: string): s is Color

// TODO 4: Interfaces vs type aliases
//   interface Animal { name: string; sound(): string; }
//   interface Dog extends Animal { breed: string; }
//   type Cat = Animal & { indoor: boolean };
//   Key rule: use interface for objects (supports declaration merging),
//   use type for unions, intersections, primitives, tuples.

// TODO 5: Utility types
//   Given: interface User { id: number; name: string; email: string; role: string }
//   Partial<User>       — all optional
//   Required<User>      — all required
//   Readonly<User>      — all readonly
//   Pick<User,"name"|"email">   — subset
//   Omit<User,"id">     — exclude fields
//   Record<string,User> — dict of users

// TODO 6: satisfies operator (TS 4.9+)
//   const palette = {
//     red: [255, 0, 0], green: "#00ff00"
//   } satisfies Record<string, string | number[]>;
//   palette.red is still number[], not string | number[] — inference preserved!

// TODO 7: Template literal types
//   type EventName = `on${Capitalize<string>}`;
//   type CSSUnit = `${number}${"px"|"em"|"rem"|"%"}`;
//   Write a type that extracts route params: "/users/:id/posts/:slug" → "id" | "slug"
