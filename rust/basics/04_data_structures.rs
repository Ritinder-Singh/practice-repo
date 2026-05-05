// =============================================================================
// Rust — Data Structures
// =============================================================================
// Topics: Vec, HashMap, HashSet, String vs &str, BTreeMap, linked list,
//         custom collection with generics.
// Compile: rustc 04_data_structures.rs && ./04_data_structures
// =============================================================================

use std::collections::{HashMap, HashSet, BTreeMap, VecDeque};

fn main() {
    // TODO 1: Vec<T> — growable array
    //   let mut v: Vec<i32> = Vec::new();
    //   v.push(1); v.push(2); v.pop();
    //   v[0], v.get(0) -> Option<&T> (safe), v.len(), v.capacity()
    //   Slicing: &v[1..3], v.iter(), v.windows(2), v.chunks(3)
    //   Sorting: v.sort(), v.sort_by(|a,b| a.cmp(b)), v.sort_by_key(|x| x.abs())

    // TODO 2: String vs &str
    //   &str: immutable string slice (reference to UTF-8 bytes)
    //   String: owned, growable heap-allocated string
    //   let s: String = String::from("hello") | "hello".to_string()
    //   Concatenation: format!("{s1}{s2}") preferred over s1 + &s2 (moves s1)
    //   String methods: .contains(), .starts_with(), .split(), .trim(), .replace()
    //   Iteration: s.chars() (Unicode), s.bytes() (raw bytes), s.char_indices()

    // TODO 3: HashMap<K,V>
    //   let mut scores: HashMap<String, i32> = HashMap::new();
    //   scores.insert("Alice".to_string(), 100);
    //   scores.get("Alice")                → Option<&i32>
    //   scores.entry("Bob").or_insert(0)   → &mut i32 (insert if missing)
    //   scores.contains_key("Alice")
    //   for (k, v) in &scores { }

    // TODO 4: HashSet<T> — unique elements
    //   set operations: union(), intersection(), difference(), is_subset()

    // TODO 5: Implement a generic Stack<T>
    //   struct Stack<T> { data: Vec<T> }
    //   impl<T> Stack<T> {
    //       pub fn push(&mut self, item: T) { self.data.push(item) }
    //       pub fn pop(&mut self) -> Option<T> { self.data.pop() }
    //       pub fn peek(&self) -> Option<&T> { self.data.last() }
    //       pub fn is_empty(&self) -> bool { self.data.is_empty() }
    //   }

    // TODO 6: BTreeMap — sorted keys (useful for ordered iteration)
    //   let mut bm: BTreeMap<i32, &str> = BTreeMap::new();
    //   When to prefer over HashMap: when you need sorted keys or range queries.

    let _: HashSet<i32> = HashSet::new();
    let _: BTreeMap<i32, i32> = BTreeMap::new();
    let _: VecDeque<i32> = VecDeque::new();
    let _: HashMap<i32, i32> = HashMap::new();

    println!("Rust data structures — implement TODOs above");
}
