const std = @import("std");
// TOPIC: Structs, Enums & Unions | zig run 05_oop_or_types.zig

pub fn main() !void {
    // TODO 1: Structs with methods
    //   const Rectangle = struct {
    //       width: f32,
    //       height: f32,
    //       pub fn area(self: Rectangle) f32 { return self.width * self.height; }
    //       pub fn scale(self: *Rectangle, factor: f32) void {
    //           self.width *= factor; self.height *= factor;
    //       }
    //   };
    //   var rect = Rectangle{ .width = 3.0, .height = 4.0 };
    //   rect.scale(2.0);
    //   std.debug.print("Area: {d}\n", .{rect.area()});

    // TODO 2: Enums with methods
    //   const Direction = enum {
    //       North, South, East, West,
    //       pub fn opposite(self: Direction) Direction {
    //           return switch (self) {
    //               .North => .South, .South => .North,
    //               .East  => .West,  .West  => .East,
    //           };
    //       }
    //       pub fn isVertical(self: Direction) bool {
    //           return self == .North or self == .South;
    //       }
    //   };

    // TODO 3: Tagged union — sum type
    //   const Value = union(enum) {
    //       int: i64,
    //       float: f64,
    //       boolean: bool,
    //       string: []const u8,
    //   };
    //   const v = Value{ .int = 42 };
    //   switch (v) {
    //       .int     => |n| std.debug.print("int: {d}\n", .{n}),
    //       .float   => |f| std.debug.print("float: {d}\n", .{f}),
    //       .boolean => |b| std.debug.print("bool: {}\n", .{b}),
    //       .string  => |s| std.debug.print("str: {s}\n", .{s}),
    //   }

    // TODO 4: Interfaces via comptime duck typing
    //   fn printLength(container: anytype) void {
    //       // Works for any type with .len field
    //       std.debug.print("Length: {d}\n", .{container.len});
    //   }
    //   printLength([_]i32{ 1, 2, 3 });     // array
    //   printLength("hello");                // string slice
    //   printLength(std.ArrayList(i32){});  // ArrayList (after .items)

    // TODO 5: Comptime interface via @hasDecl/@hasField
    //   fn printAll(comptime T: type, items: []const T) void {
    //       comptime std.debug.assert(@hasDecl(T, "toString"));
    //       for (items) |item| std.debug.print("{s}\n", .{item.toString()});
    //   }

    // TODO 6: Packed structs — exact memory layout
    //   const Flags = packed struct {
    //       read:    bool,
    //       write:   bool,
    //       execute: bool,
    //       _pad:    u5 = 0,
    //   };
    //   const f = Flags{ .read = true, .write = true, .execute = false };
    //   std.debug.print("Flags byte: {d}\n", .{@as(u8, @bitCast(f))});

    // TODO 7: extern structs — C-compatible memory layout
    //   const CPoint = extern struct { x: c_int, y: c_int };
    //   // Use for FFI/interop with C libraries

    // TODO 8: Comptime struct generation — generic type creation
    //   fn Vec(comptime T: type, comptime N: usize) type {
    //       return struct {
    //           data: [N]T,
    //           pub fn get(self: @This(), i: usize) T { return self.data[i]; }
    //           pub fn set(self: *@This(), i: usize, v: T) void { self.data[i] = v; }
    //           pub fn dot(self: @This(), other: @This()) T {
    //               var sum: T = 0;
    //               for (self.data, other.data) |a, b| sum += a * b;
    //               return sum;
    //           }
    //       };
    //   }
    //   const Vec3 = Vec(f32, 3);
    //   var v1 = Vec3{ .data = .{1.0, 2.0, 3.0} };

    std.debug.print("TODO: implement struct/enum/union exercises\n", .{});
}
