// =============================================================================
// Rust — Loops & Control Flow
// =============================================================================
// Topics: if let, while let, loop, for..in, iterators, match, patterns.
// Compile: rustc 03_loops_control_flow.rs && ./03_loops_control_flow
// =============================================================================

fn main() {
    // TODO 1: if/else and if let
    //   let num = Some(7);
    //   if let Some(n) = num { println!("{n}") }  // matches and binds
    //   if let Some(n) = num && n > 5 { ... }     // with condition (Rust 1.64+)

    // TODO 2: loop — infinite loop with return value
    //   let result = loop {
    //       counter += 1;
    //       if counter == 10 { break counter * 2; }  // loop returns a value!
    //   };

    // TODO 3: while and while let
    //   while condition { ... }
    //   let mut stack = vec![1,2,3];
    //   while let Some(top) = stack.pop() { println!("{top}") }

    // TODO 4: for..in with ranges and iterators
    //   for i in 0..5 { }             // exclusive end (0,1,2,3,4)
    //   for i in 0..=5 { }            // inclusive end (0,1,2,3,4,5)
    //   for (i, v) in vec.iter().enumerate() { }
    //   for v in vec.iter() / vec.iter_mut() / vec.into_iter() { }

    // TODO 5: match — exhaustive pattern matching
    //   match x {
    //       0 => "zero",
    //       1 | 2 => "one or two",
    //       3..=5 => "three to five",
    //       n if n < 0 => "negative",
    //       _ => "other",
    //   }
    //   Destructure tuples: (x, y) | structs: Struct { field, .. } | enums

    // TODO 6: Iterator adapters — lazy, zero-cost abstractions
    //   .map() .filter() .take() .skip() .enumerate() .zip() .flat_map()
    //   .collect::<Vec<_>>() .sum::<i32>() .product() .any() .all() .find()
    //   Implement: fizzbuzz using (1..=100).map(|n| ...).collect::<Vec<String>>()

    println!("Rust loops & control flow — implement TODOs above");
}
