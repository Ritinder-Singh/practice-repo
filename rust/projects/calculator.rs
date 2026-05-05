// =============================================================================
// PROJECT: Rust CLI Calculator
// =============================================================================
// TODO 1 (Mini): REPL — +,-,*,/,% on f64; handle divide-by-zero
// TODO 2 (Intermediate): Recursive descent parser
//   Tokens: Number(f64) | Op(char) | LParen | RParen
//   Grammar: expr→term((+|-)term)* | term→factor((*|/)factor)* | factor→NUM|(expr)
// TODO 3 (Advanced): Variables (x=5+3), functions (sqrt, abs), history
// Compile: rustc calculator.rs && ./calculator
// =============================================================================

use std::io::{self, BufRead, Write};

fn main() {
    let stdin = io::stdin();
    print!("Rust Calculator — type 'quit' to exit\n");
    io::stdout().flush().unwrap();
    for line in stdin.lock().lines() {
        let line = line.unwrap();
        let line = line.trim();
        if line == "quit" { break; }
        print!("> ");
        // TODO: tokenize, parse, evaluate
        println!("(not implemented)");
        io::stdout().flush().unwrap();
    }
}
