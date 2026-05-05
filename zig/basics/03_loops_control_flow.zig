const std = @import("std");
// TOPIC: Loops & Control Flow | zig run 03_loops_control_flow.zig

pub fn main() !void {
    // TODO 1: while loop — with continue expression
    //   var i: usize = 0;
    //   while (i < 10) : (i += 1) {
    //       std.debug.print("{d} ", .{i});
    //   }
    //   // while with optional (null check):
    //   var opt: ?i32 = 42;
    //   while (opt) |val| { std.debug.print("{d}\n", .{val}); opt = null; }

    // TODO 2: for loop over array/slice — with index
    //   const arr = [_]i32{ 10, 20, 30, 40, 50 };
    //   for (arr, 0..) |item, idx| {
    //       std.debug.print("[{d}]={d}\n", .{idx, item});
    //   }
    //   // Multi-array for (must be same length):
    //   for (arr1, arr2) |a, b| { ... }

    // TODO 3: Labeled break with value
    //   const val = blk: {
    //       var x: i32 = 0;
    //       while (x < 100) : (x += 1) {
    //           if (x * x > 50) break :blk x;
    //       }
    //       break :blk -1;
    //   };

    // TODO 4: inline for/while — unrolled at compile time
    //   const fields = @typeInfo(MyStruct).Struct.fields;
    //   inline for (fields) |field| {
    //       std.debug.print("field: {s}\n", .{field.name});
    //   }

    // TODO 5: switch expression
    //   const x: i32 = 5;
    //   const result = switch (x) {
    //       1, 2 => "one or two",
    //       3...7 => "three to seven",
    //       else => "other",
    //   };
    //   // switch must be exhaustive; ranges with ...

    // TODO 6: comptime if — conditional compilation
    //   comptime { if (@sizeOf(usize) == 8) { @compileLog("64-bit platform"); } }
    //   fn platformMessage() []const u8 {
    //       if (comptime @sizeOf(usize) == 8) return "64-bit" else return "32-bit";
    //   }

    // TODO 7: FizzBuzz using switch
    //   var i: u32 = 1;
    //   while (i <= 100) : (i += 1) {
    //       const msg = switch (@intFromBool(i % 15 == 0) * 3 + @intFromBool(i % 3 == 0) * 2 + @intFromBool(i % 5 == 0)) {
    //           3 => "FizzBuzz",
    //           2 => "Fizz",
    //           1 => "Buzz",
    //           else => blk: {
    //               var buf: [10]u8 = undefined;
    //               break :blk try std.fmt.bufPrint(&buf, "{d}", .{i});
    //           },
    //       };
    //       std.debug.print("{s}\n", .{msg});
    //   }

    // TODO 8: defer and errdefer
    //   {
    //       defer std.debug.print("cleanup\n", .{});  // runs at scope exit
    //       // errdefer: only runs on error path
    //       const data = try allocator.alloc(u8, 100);
    //       errdefer allocator.free(data);
    //       try processData(data);  // if this errors, errdefer frees data
    //       allocator.free(data);   // happy path: free normally
    //   }

    std.debug.print("TODO: implement control flow exercises\n", .{});
}
