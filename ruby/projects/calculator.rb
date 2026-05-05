# PROJECT: Ruby Calculator | ruby calculator.rb

# TODO 1 (Mini): Simple REPL using eval (learning purposes only)
#   loop do
#     print ">> "
#     input = gets&.chomp
#     break if input.nil? || input == "exit"
#     begin
#       puts eval(input)   # NOTE: eval is dangerous in production — never use on untrusted input
#     rescue ZeroDivisionError
#       puts "Error: division by zero"
#     rescue SyntaxError, StandardError => e
#       puts "Error: #{e.message}"
#     end
#   end

# TODO 2 (Intermediate): Tokenizer + recursive descent parser (no eval)
#   TOKENS = /\d+\.?\d*|[+\-*\/()]/
#   def tokenize(input) = input.scan(TOKENS)
#
#   # Parser methods:
#   # def parse_expr(tokens)   — handles + and -
#   # def parse_term(tokens)   — handles * and /
#   # def parse_factor(tokens) — handles numbers and (expr)
#   # Grammar:
#   #   expr   → term (('+' | '-') term)*
#   #   term   → factor (('*' | '/') factor)*
#   #   factor → NUMBER | '(' expr ')' | '-' factor

# TODO 3 (Advanced): Variable assignment
#   @vars = {}
#   # Parse "x = 5 + 3" → @vars["x"] = 8
#   # Allow "x * 2" in subsequent expressions — substitute variable values before parsing
#
#   # Bonus: method definitions
#   # Parse "def square(x) = x**2" → store in @functions hash
