// =============================================================================
// PROJECT: Rust CLI JSON Formatter (Mini)
// =============================================================================
// Roadmap: Mini — "Command-line JSON formatter"
//
// TODO 1 (Mini): Pretty-print JSON from stdin
//   Read JSON from stdin or file argument, output indented.
//   Use only std (no serde): parse JSON manually or use minimal hand-rolled parser.
//   Compile: rustc json_formatter.rs && echo '{"a":1}' | ./json_formatter
//
// TODO 2 (Intermediate): Full JSON parser
//   Parse: null, bool, number, string (with escape sequences), array, object
//   Build recursive parse(tokens) -> JsonValue enum
//   Pretty-print with configurable indent (--indent=4)
//
// TODO 3 (Advanced): jq-like queries
//   ./json_formatter --query ".users[0].name" input.json
//   Support: field access (.name), array index ([0]), array iteration (.users[])
//
// Compile: rustc json_formatter.rs && ./json_formatter
// =============================================================================

use std::io::{self, Read};

#[derive(Debug)]
enum JsonValue {
    Null,
    Bool(bool),
    Number(f64),
    Str(String),
    Array(Vec<JsonValue>),
    Object(Vec<(String, JsonValue)>),  // Vec to preserve order
}

impl JsonValue {
    // TODO: fn pretty_print(&self, indent: usize) -> String
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    // TODO: parse input, pretty-print
    println!("JSON formatter — implement parser and pretty-printer");
}
