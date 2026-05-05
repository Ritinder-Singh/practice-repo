const std = @import("std");
// TOPIC: Functions | zig run 02_functions.zig

pub fn main() !void {
    // TODO 1: Basic function definition
    //   fn add(a: i32, b: i32) i32 { return a + b; }
    //   fn greet(name: []const u8) void { std.debug.print("Hello, {s}!\n", .{name}); }

    // TODO 2: Comptime parameters — generics in Zig
    //   fn identity(comptime T: type, val: T) T { return val; }
    //   const n = identity(i32, 42);
    //   const s = identity([]const u8, "hello");

    // TODO 3: Optional return type
    //   fn parseInt(s: []const u8) ?i32 {
    //       return std.fmt.parseInt(i32, s, 10) catch null;
    //   }

    // TODO 4: Error return type
    //   fn readFile(path: []const u8, allocator: std.mem.Allocator) ![]u8 {
    //       const file = try std.fs.cwd().openFile(path, .{});
    //       defer file.close();
    //       return try file.readToEndAlloc(allocator, 1024 * 1024);
    //   }

    // TODO 5: Inline functions — expanded at call site
    //   inline fn square(x: i32) i32 { return x * x; }
    //   // Forces inlining; use for performance-critical paths

    // TODO 6: Function pointers
    //   const Fn = *const fn (i32) i32;
    //   fn applyTwice(f: Fn, x: i32) i32 { return f(f(x)); }
    //   const double = struct { fn f(x: i32) i32 { return x * 2; } }.f;
    //   std.debug.print("{d}\n", .{applyTwice(double, 3)});  // 12

    // TODO 7: Recursive function — fibonacci
    //   fn fibonacci(n: u32) u32 {
    //       if (n <= 1) return n;
    //       return fibonacci(n - 1) + fibonacci(n - 2);
    //   }
    //   // Tail-recursive version with accumulator:
    //   fn fibTail(n: u32, a: u32, b: u32) u32 {
    //       return if (n == 0) a else fibTail(n - 1, b, a + b);
    //   }

    // TODO 8: anytype parameter — duck typing at compile time
    //   fn printAny(val: anytype) void {
    //       const T = @TypeOf(val);
    //       switch (@typeInfo(T)) {
    //           .Int => std.debug.print("int: {d}\n", .{val}),
    //           .Float => std.debug.print("float: {d}\n", .{val}),
    //           .Bool => std.debug.print("bool: {}\n", .{val}),
    //           else => std.debug.print("other: {}\n", .{val}),
    //       }
    //   }

    std.debug.print("TODO: implement function exercises\n", .{});
}
