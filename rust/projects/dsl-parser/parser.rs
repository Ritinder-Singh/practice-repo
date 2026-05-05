// =============================================================================
// PROJECT: Zero-Copy DSL Parser (Exclusive)
// =============================================================================
// Roadmap: Exclusive — "Zero-copy DSL parser using ownership to guarantee
//          memory safety at compile time"
//
// Build a parser for a simple configuration DSL:
//   [server]
//   host = "localhost"
//   port = 8080
//   [database]
//   url = "postgres://..."
//
// TODO 1: Tokenizer — zero-copy using &str slices (no String allocation)
//   enum Token<'a> { Section(&'a str), Key(&'a str), Value(Value<'a>) }
//   enum Value<'a> { Str(&'a str), Int(i64), Float(f64), Bool(bool) }
//   fn tokenize<'a>(input: &'a str) -> Vec<Token<'a>>
//
// TODO 2: Parser — builds AST from tokens
//   type Config<'a> = HashMap<&'a str, Section<'a>>;
//   type Section<'a> = HashMap<&'a str, Value<'a>>;
//   fn parse<'a>(tokens: &[Token<'a>]) -> Result<Config<'a>, ParseError>
//
// TODO 3: Ownership guarantees
//   The Config borrows from the original input &str.
//   If input goes out of scope, Config is invalid → compile error.
//   Demonstrate: Config cannot outlive the input string it borrows from.
//
// TODO 4: Serializer
//   fn serialize(config: &Config) -> String   // owned, no lifetime needed
//
// Compile: rustc parser.rs && ./parser
// =============================================================================

fn main() {
    let input = r#"
[server]
host = "localhost"
port = 8080
debug = true

[database]
url = "postgres://localhost/mydb"
pool_size = 5
"#;
    // TODO: tokenize(input), parse(tokens), query config
    println!("DSL parser — implement TODO sections");
    let _ = input;
}
