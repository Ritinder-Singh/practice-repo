const std = @import("std");
// PROJECT: Generic Data Structures | zig run generic_ds.zig
// Demonstrate Zig comptime type reflection to build fully generic containers.
//
// TODO 1: Generic Stack using comptime T
//   fn Stack(comptime T: type) type {
//       return struct {
//           items: std.ArrayList(T),
//           pub fn init(allocator: std.mem.Allocator) @This() { ... }
//           pub fn push(self: *@This(), item: T) !void { ... }
//           pub fn pop(self: *@This()) ?T { ... }
//           pub fn peek(self: @This()) ?T { ... }
//           pub fn deinit(self: *@This()) void { ... }
//       };
//   }
//   const IntStack = Stack(i32);
//
// TODO 2: Generic ring buffer (fixed capacity, no allocation)
//   fn RingBuffer(comptime T: type, comptime N: usize) type {
//       return struct {
//           data: [N]T = undefined,
//           head: usize = 0,
//           tail: usize = 0,
//           count: usize = 0,
//           pub fn push(self: *@This(), item: T) bool { ... }  // false if full
//           pub fn pop(self: *@This()) ?T { ... }
//       };
//   }
//
// TODO 3: Intrusive linked list via comptime field detection
//   // Node embeds "next" pointer; list finds it via @hasField + @fieldParentPtr
//   fn IntrusiveList(comptime T: type, comptime link_field: []const u8) type { ... }
//
// TODO 4: @typeInfo-based pretty printer
//   // Walk @typeInfo at comptime, print struct field names + values at runtime
//   fn prettyPrint(value: anytype) void {
//       const T = @TypeOf(value);
//       const info = @typeInfo(T);
//       switch (info) {
//           .Struct => |s| inline for (s.fields) |f| {
//               std.debug.print("{s} = {any}\n", .{f.name, @field(value, f.name)});
//           },
//           else => std.debug.print("{any}\n", .{value}),
//       }
//   }

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    // const allocator = gpa.allocator();

    const stdout = std.io.getStdOut().writer();
    try stdout.print("Generic Data Structures — TODO: implement\n", .{});
}
