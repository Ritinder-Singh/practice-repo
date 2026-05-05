const std = @import("std");
// TOPIC: Error Handling | zig run 06_error_handling.zig
// Docs: https://ziglang.org/documentation/master/#Errors

pub fn main() !void {
    // TODO 1: Error sets — declare possible errors
    //   const FileError = error {
    //       NotFound,
    //       PermissionDenied,
    //       UnexpectedEof,
    //   };
    //   fn openConfig() FileError![]const u8 {
    //       return error.NotFound;
    //   }

    // TODO 2: try — propagate error upward
    //   fn processConfig() !void {
    //       const data = try openConfig();  // returns error if openConfig fails
    //       std.debug.print("Config: {s}\n", .{data});
    //   }
    //   // Equivalent to:
    //   // const data = openConfig() catch |err| return err;

    // TODO 3: catch — handle or provide default
    //   const value = std.fmt.parseInt(i32, "abc", 10) catch 0;
    //   // catch with capture:
    //   const result = riskyOp() catch |err| blk: {
    //       std.debug.print("Error: {}\n", .{err});
    //       break :blk defaultValue;
    //   };

    // TODO 4: errdefer — cleanup only on error path
    //   fn createResource(allocator: std.mem.Allocator) !*Resource {
    //       const r = try allocator.create(Resource);
    //       errdefer allocator.destroy(r);  // only runs if subsequent error occurs
    //       try r.init();                   // if this fails, errdefer frees r
    //       return r;
    //   }

    // TODO 5: anyerror — accept any error type
    //   fn handleAny() anyerror!void { try riskyOp(); }
    //   // anyerror is a superset of all error sets; use sparingly

    // TODO 6: switch on error — exhaustive error handling
    //   const result = openFile("config.txt");
    //   switch (result) {
    //       .Ok  => |f| processFile(f),
    //       .Err => |err| switch (err) {
    //           error.NotFound       => std.debug.print("File not found\n", .{}),
    //           error.PermissionDenied => std.debug.print("Access denied\n", .{}),
    //           else => return err,  // re-raise unknown errors
    //       },
    //   }

    // TODO 7: Error return traces — enable with ReleaseSafe or Debug mode
    //   // Zig automatically captures error return traces in Debug/ReleaseSafe
    //   // Access via: std.debug.dumpCurrentStackTrace(null);

    // TODO 8: @errorName and error casting
    //   const err = error.NotFound;
    //   std.debug.print("Error name: {s}\n", .{@errorName(err)});
    //   // Convert error to int and back: @intFromError, @errorFromInt

    std.debug.print("TODO: implement error handling exercises\n", .{});
}
