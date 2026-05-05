// =============================================================================
// Rust — Advanced Topics
// =============================================================================
// Topics: lifetimes, smart pointers (Box/Rc/Arc), interior mutability
//         (RefCell/Mutex), macros, unsafe, WASM target, zero-cost abstractions.
// Compile: rustc 08_advanced.rs && ./08_advanced
// =============================================================================

fn main() {
    // TODO 1: Lifetimes
    //   fn longest<'a>(s1: &'a str, s2: &'a str) -> &'a str { ... }
    //   Lifetime annotations tell the borrow checker how long references live.
    //   struct Important<'a> { text: &'a str }
    //   'static lifetime: lives for entire program (string literals, leaked Box)

    // TODO 2: Box<T> — heap allocation
    //   let b = Box::new(5i32);     // 5 on heap
    //   Recursive types require Box: enum List { Cons(i32, Box<List>), Nil }
    //   Box<dyn Trait> — trait objects (dynamic dispatch)

    // TODO 3: Rc<T> and RefCell<T> — shared ownership + interior mutability
    //   Rc<T>: reference-counted shared ownership (single-threaded)
    //   RefCell<T>: runtime borrow checking (allows mutation through shared ref)
    //   Rc<RefCell<T>>: multiple owners that can mutate
    //   Arc<Mutex<T>>: thread-safe version

    // TODO 4: Declarative macros (macro_rules!)
    //   macro_rules! vec_of_strings {
    //       ($($x:expr),*) => { vec![$($x.to_string()),*] }
    //   }
    //   Patterns: tt (token tree), expr, ident, ty, pat, block

    // TODO 5: Procedural macros (derive macros — requires Cargo)
    //   #[derive(Debug, Clone, Serialize, Deserialize)]  — serde
    //   Custom derive: separate crate with proc-macro = true in Cargo.toml

    // TODO 6: Unsafe Rust
    //   unsafe {
    //       let raw = &x as *const i32;     // raw pointer
    //       let val = *raw;                  // dereference
    //   }
    //   5 unsafe superpowers: raw pointers, unsafe fn calls, static mut, unsafe traits, union fields

    // TODO 7: Zero-cost abstractions — iterator pipeline compiles to same as manual loop
    //   (1..=1_000_000).filter(|x| x%2==0).map(|x| x*x).sum::<u64>()
    //   vs manual loop — benchmark with criterion crate

    println!("Rust advanced topics — implement TODOs above");
}
