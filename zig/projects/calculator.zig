const std = @import("std");
// PROJECT: Calculator | zig run calculator.zig
// Build a command-line REPL calculator in pure Zig.
//
// TODO 1 (Mini): Basic REPL — read line, tokenize, compute
//   - Support: +, -, *, /
//   - Read from stdin with std.io.getStdIn().reader()
//   - Handle division by zero with error union
//
// TODO 2 (Intermediate): Recursive descent parser (no eval)
//   - Grammar:
//       expr   → term (('+' | '-') term)*
//       term   → factor (('*' | '/') factor)*
//       factor → NUMBER | '(' expr ')'
//   - Store tokens in a comptime-friendly union
//
// TODO 3 (Advanced): Variables + history
//   - Assignment: x = 5 + 3  (store in StringHashMap)
//   - Reference vars in subsequent expressions
//   - Print result history with !history command

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    // const allocator = gpa.allocator();

    const stdout = std.io.getStdOut().writer();
    try stdout.print("Calculator — TODO: implement\n", .{});
}
