// =============================================================================
// Rust — Variables & Types
// =============================================================================
// Topics: let/const/static, mutability, shadowing, ownership intro,
//         scalar types, compound types, type inference, type casting.
// Compile: rustc 01_variables_types.rs && ./01_variables_types
// Docs: https://doc.rust-lang.org/book/ch03-00-common-programming-concepts.html
// =============================================================================

fn main() {
    // TODO 1: Immutable vs mutable bindings
    //   let x = 5;           // immutable — reassignment is compile error
    //   let mut y = 5;       // mutable
    //   y = 10;              // ok
    //   Shadowing: let x = x + 1; (creates new binding, can change type)

    // TODO 2: Scalar types
    //   Integer: i8 i16 i32 i64 i128 isize | u8 u16 u32 u64 u128 usize
    //   Float: f32 f64
    //   Boolean: bool (true/false)
    //   Character: char (4 bytes, Unicode scalar value)
    //   Numeric literals: 1_000_000, 0xFF, 0b1010, 0o17, b'A' (byte)

    // TODO 3: Compound types
    //   Tuple: let tup: (i32, f64, char) = (42, 3.14, 'z');
    //          let (a, b, c) = tup;     // destructuring
    //          tup.0, tup.1             // index access
    //   Array: let arr: [i32; 5] = [1,2,3,4,5];
    //          let zeros = [0; 100];    // 100 zeros
    //          arr[0]                   // index (bounds-checked at runtime)

    // TODO 4: Type inference and explicit casting
    //   Rust infers types from usage context — no runtime coercion.
    //   Cast: let x: i32 = 300; let y = x as i64;  // explicit cast
    //   Overflow: i32::MAX + 1 panics in debug, wraps in release (use checked_add)

    // TODO 5: const and static
    //   const MAX_POINTS: u32 = 100_000;    // must have type annotation, compile-time
    //   static HELLO: &str = "Hello";       // static lifetime, can be mutable with unsafe

    // TODO 6: Shadowing vs mutability — when to use each
    //   Shadowing: let x: i32 = 5; let x: &str = "five";  // type changes allowed
    //   Mutation:  let mut x = 5; x = 6;                  // same type only

    println!("Rust variables & types — implement TODOs above");
}
