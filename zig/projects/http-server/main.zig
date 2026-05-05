const std = @import("std");
// PROJECT: HTTP Server (main) | zig build run
// Pure Zig HTTP/1.1 server using std.net — no external deps.
//
// TODO 1: TCP listener
//   const addr = try std.net.Address.parseIp("127.0.0.1", 8080);
//   var server = try addr.listen(.{ .reuse_address = true });
//   defer server.deinit();
//   while (true) {
//       const conn = try server.accept();
//       _ = try std.Thread.spawn(.{}, handleConn, .{conn});
//   }
//
// TODO 2: Request parsing (delegate to http.zig)
//   - Read raw bytes from conn.stream.reader()
//   - Parse request line: "GET /path HTTP/1.1"
//   - Parse headers: "Key: Value\r\n"
//
// TODO 3: Router — match method + path → handler
//   - GET /        → index handler (200 OK, HTML body)
//   - GET /health  → {"status":"ok"} JSON
//   - 404 fallback
//
// TODO 4: Graceful shutdown
//   - Catch SIGINT, stop accepting, wait for in-flight requests

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();
    _ = allocator;

    const stdout = std.io.getStdOut().writer();
    try stdout.print("HTTP Server — TODO: implement\n", .{});
}
