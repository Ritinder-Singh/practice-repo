const std = @import("std");
// TOPIC: Advanced Zig | zig run 08_advanced.zig

pub fn main() !void {
    // TODO 1: comptime reflection with @typeInfo
    //   fn printStructFields(comptime T: type) void {
    //       const info = @typeInfo(T);
    //       switch (info) {
    //           .Struct => |s| {
    //               inline for (s.fields) |field| {
    //                   std.debug.print("field: {s} type: {s}\n", .{field.name, @typeName(field.type)});
    //               }
    //           },
    //           else => @compileError("Expected a struct"),
    //       }
    //   }
    //   const Point = struct { x: f32, y: f32 };
    //   printStructFields(Point);

    // TODO 2: @typeName, @TypeOf, @typeInfo
    //   @typeName(i32)         // "i32"
    //   @TypeOf(42)            // comptime_int
    //   @TypeOf(42.0)          // comptime_float
    //   @typeInfo(bool)        // TypeInfo.Bool
    //   @typeInfo(?i32)        // TypeInfo.Optional{ .child = i32 }

    // TODO 3: build.zig overview — Zig's build system is Zig code
    //   // build.zig structure:
    //   // pub fn build(b: *std.Build) void {
    //   //     const exe = b.addExecutable(.{ .name = "myapp", .root_source_file = b.path("src/main.zig") });
    //   //     b.installArtifact(exe);
    //   //     const run_cmd = b.addRunArtifact(exe);
    //   //     const run_step = b.step("run", "Run the application");
    //   //     run_step.dependOn(&run_cmd.step);
    //   // }

    // TODO 4: Packed structs for bit manipulation
    //   const IPv4Header = packed struct(u160) {
    //       version:        u4  = 4,
    //       ihl:            u4  = 5,
    //       dscp:           u6  = 0,
    //       ecn:            u2  = 0,
    //       total_length:   u16 = 0,
    //       identification: u16 = 0,
    //       flags:          u3  = 0,
    //       frag_offset:    u13 = 0,
    //       ttl:            u8  = 64,
    //       protocol:       u8  = 0,
    //       checksum:       u16 = 0,
    //       src:            u32 = 0,
    //       dst:            u32 = 0,
    //   };

    // TODO 5: SIMD vectors
    //   const Vec4f32 = @Vector(4, f32);
    //   const a: Vec4f32 = .{1.0, 2.0, 3.0, 4.0};
    //   const b: Vec4f32 = .{5.0, 6.0, 7.0, 8.0};
    //   const sum = a + b;   // SIMD addition: {6, 8, 10, 12}
    //   const dot = @reduce(.Add, a * b);  // dot product: 70.0

    // TODO 6: C interop
    //   const c = @cImport({ @cInclude("stdio.h"); });
    //   c.printf("Hello from C: %d\n", 42);
    //   // Link C library in build.zig: exe.linkSystemLibrary("c");

    // TODO 7: Allocator abstraction — swap allocators without changing code
    //   // Testing allocator: std.testing.allocator (detects leaks)
    //   // Arena allocator: std.heap.ArenaAllocator (free all at once)
    //   // Fixed buffer: std.heap.FixedBufferAllocator (no heap)
    //   // Stack fallback: std.heap.stackFallback(N, backup)
    //   var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    //   defer arena.deinit();
    //   const alloc = arena.allocator();
    //   // All allocations freed at once when arena.deinit() is called

    // TODO 8: comptime known-size allocations — avoid runtime allocations
    //   fn splitComptime(comptime str: []const u8, comptime delim: u8) []const []const u8 {
    //       comptime {
    //           var count = 1;
    //           for (str) |c| if (c == delim) count += 1;
    //           var parts: [count][]const u8 = undefined;
    //           // ... split logic at comptime
    //           return &parts;
    //       }
    //   }

    std.debug.print("TODO: implement advanced Zig exercises\n", .{});
}
