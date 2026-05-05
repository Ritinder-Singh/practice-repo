const std = @import("std");
// TOPIC: Variables & Types | zig run 01_variables_types.zig
// Docs: https://ziglang.org/documentation/master/

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();

    // TODO 1: const vs var — mutability
    //   const x: i32 = 42;         // immutable
    //   var y: f64 = 3.14;          // mutable
    //   y = 2.71;                   // ok
    //   x = 100;                    // compile error: cannot assign to const
    //   _ = x;                      // suppress unused variable error

    // TODO 2: Integer types
    //   i8, i16, i32, i64, i128, isize  (signed)
    //   u8, u16, u32, u64, u128, usize  (unsigned)
    //   comptime_int — arbitrary precision integer at compile time
    //   Overflow: x + y overflows → compile error (in safety mode)
    //   Wrapping ops: x +% y, x -% y, x *% y
    //   @addWithOverflow(i32, a, b) — returns {result, overflow_bit}

    // TODO 3: Float types
    //   f16, f32, f64, f80, f128
    //   const pi: f64 = std.math.pi;
    //   @as(f32, @floatFromInt(myInt))  — int to float cast

    // TODO 4: Optionals
    //   var opt: ?i32 = null;
    //   opt = 42;
    //   if (opt) |val| { try stdout.print("Got: {d}\n", .{val}); }
    //   const x = opt orelse 0;  // unwrap with default

    // TODO 5: Error unions
    //   fn divide(a: i32, b: i32) !i32 {
    //       if (b == 0) return error.DivisionByZero;
    //       return @divExact(a, b);
    //   }
    //   const result = divide(10, 2) catch 0;  // default on error
    //   const result2 = try divide(10, 2);     // propagate error upward

    // TODO 6: Arrays
    //   const arr = [5]i32{ 1, 2, 3, 4, 5 };
    //   arr[0]          // 1
    //   arr.len         // 5
    //   const arr2 = [_]i32{ 1, 2, 3 };  // infer length
    //   comptime const zeros = [10]i32{ 0 } ** 10;  // repeat

    // TODO 7: Slices — pointer + length, no ownership
    //   const slice: []const i32 = arr[1..4];  // [2, 3, 4]
    //   slice.len        // 3
    //   slice.ptr        // pointer to first element
    //   var mutable_slice: []i32 = &arr;  // won't compile — arr is const

    // TODO 8: Structs
    //   const Point = struct { x: f32, y: f32 };
    //   const p = Point{ .x = 1.0, .y = 2.0 };
    //   p.x  // 1.0
    //   // Packed struct: @sizeOf(PackedFlags) may be less than field sum

    try stdout.print("TODO: implement variable/type exercises\n", .{});
}
