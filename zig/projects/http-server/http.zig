const std = @import("std");
// HTTP parsing utilities for the pure-Zig HTTP server.

// TODO 1: Request type
//   pub const Method = enum { GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS };
//   pub const Request = struct {
//       method:  Method,
//       path:    []const u8,
//       version: []const u8,
//       headers: std.StringHashMap([]const u8),
//       body:    []const u8,
//   };

// TODO 2: parseRequest — parse raw bytes into Request
//   pub fn parseRequest(raw: []const u8, allocator: std.mem.Allocator) !Request {
//       // Split on \r\n to get lines
//       // First line: method SP path SP version
//       // Remaining lines until blank line: headers
//       // Remainder: body
//   }

// TODO 3: Response builder
//   pub const Response = struct {
//       status:  u16,
//       headers: std.ArrayList(u8),
//       body:    []const u8,
//       pub fn write(self: Response, writer: anytype) !void {
//           // "HTTP/1.1 {status} {reason}\r\n"
//           // headers + "\r\n\r\n"
//           // body
//       }
//   };

// TODO 4: Content-Type helpers
//   pub fn mimeType(path: []const u8) []const u8
//   — ".html" → "text/html", ".json" → "application/json", etc.
