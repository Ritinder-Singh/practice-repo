// =============================================================================
// Rust — Structs, Enums, Traits & Type System
// =============================================================================
// Topics: structs (named/tuple/unit), impl blocks, enums with data,
//         traits (defining, implementing, default methods, derive),
//         trait objects (dyn), generics with bounds, newtype pattern.
// Compile: rustc 05_oop_or_types.rs && ./05_oop_or_types
// Docs: https://doc.rust-lang.org/book/ch10-02-traits.html
// =============================================================================

fn main() {
    // TODO 1: Named struct + impl block
    //   struct Rectangle { width: f64, height: f64 }
    //   impl Rectangle {
    //       fn new(w: f64, h: f64) -> Self { Rectangle { width: w, height: h } }
    //       fn area(&self) -> f64 { self.width * self.height }
    //       fn is_square(&self) -> bool { self.width == self.height }
    //       fn scale(&mut self, factor: f64) { self.width *= factor; self.height *= factor }
    //   }

    // TODO 2: Enum with associated data
    //   enum Shape {
    //       Circle { radius: f64 },
    //       Rectangle { width: f64, height: f64 },
    //       Triangle { base: f64, height: f64 },
    //   }
    //   impl Shape {
    //       fn area(&self) -> f64 { match self { Shape::Circle {radius} => ... } }
    //   }

    // TODO 3: Traits — define behavior
    //   trait Drawable { fn draw(&self); fn area(&self) -> f64; }
    //   impl Drawable for Circle { ... }
    //   impl Drawable for Rectangle { ... }
    //   Default method: fn describe(&self) -> String { format!("Area: {}", self.area()) }

    // TODO 4: Generics with trait bounds
    //   fn largest<T: PartialOrd>(list: &[T]) -> &T { ... }
    //   fn print_info<T: Drawable + std::fmt::Debug>(shape: &T) { ... }
    //   Where clause: fn foo<T>(x: T) where T: Drawable + Clone { ... }

    // TODO 5: Trait objects (dynamic dispatch)
    //   let shapes: Vec<Box<dyn Drawable>> = vec![Box::new(Circle{radius:5.0}), ...];
    //   Why Box<dyn Drawable> not Vec<Drawable>: trait objects are unsized

    // TODO 6: Derive macros
    //   #[derive(Debug, Clone, PartialEq, Eq, Hash)]
    //   struct Point { x: i32, y: i32 }
    //   Debug: enables {:?} formatting
    //   Clone: .clone() deep copy | Copy: implicit bitwise copy for simple types

    // TODO 7: Newtype pattern — type-safe wrappers
    //   struct Meters(f64);
    //   struct Kilograms(f64);
    //   impl Add for Meters { ... }  // Meters + Meters = Meters
    //   Meters + Kilograms → compile error!

    println!("Rust structs, enums, traits — implement TODOs above");
}
