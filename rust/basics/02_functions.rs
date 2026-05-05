// =============================================================================
// Rust — Functions
// =============================================================================
// Topics: fn syntax, expressions vs statements, closures, higher-order functions,
//         function pointers, diverging functions (!), const fn.
// Compile: rustc 02_functions.rs && ./02_functions
// =============================================================================

fn main() {
    // TODO 1: Function syntax — expressions vs statements
    //   fn add(a: i32, b: i32) -> i32 { a + b }  // last expression = return value
    //   Statements don't return values; expressions do.
    //   let y = { let x = 3; x + 1 };   // block is an expression → y = 4

    // TODO 2: Closures — capture environment
    //   let add_one = |x: i32| -> i32 { x + 1 };  // verbose
    //   let add_one = |x| x + 1;                   // type inferred
    //   let threshold = 5;
    //   let above = |x| x > threshold;             // borrows threshold from scope
    //   move |x| x > threshold                     // moves threshold into closure

    // TODO 3: Higher-order functions with iterators
    //   let nums = vec![1,2,3,4,5];
    //   nums.iter().map(|x| x * 2).filter(|x| x > &4).collect::<Vec<_>>()
    //   Implement using closures: map, filter, reduce (fold)

    // TODO 4: Function pointers vs trait objects
    //   fn apply(f: fn(i32) -> i32, x: i32) -> i32 { f(x) }
    //   fn apply_dyn(f: &dyn Fn(i32) -> i32, x: i32) -> i32 { f(x) }  // trait object
    //   fn apply_generic<F: Fn(i32) -> i32>(f: F, x: i32) -> i32 { f(x) }  // generic (zero-cost)

    // TODO 5: Returning closures
    //   fn make_adder(x: i32) -> impl Fn(i32) -> i32 { move |y| x + y }
    //   fn make_adder_box(x: i32) -> Box<dyn Fn(i32) -> i32> { Box::new(move |y| x + y) }

    // TODO 6: const fn — evaluated at compile time
    //   const fn factorial(n: u64) -> u64 { if n <= 1 { 1 } else { n * factorial(n-1) } }
    //   const FACT_10: u64 = factorial(10);

    // TODO 7: Diverging functions — return type !
    //   fn panic_always() -> ! { panic!("this never returns") }
    //   fn infinite_loop() -> ! { loop { } }

    println!("Rust functions — implement TODOs above");
}
