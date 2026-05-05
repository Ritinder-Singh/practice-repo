const std = @import("std");
// PROJECT: CSV Parser | zig run csv_parser.zig
// Memory-efficient zero-copy CSV parser using Zig slices.
//
// TODO 1: Tokenizer — iterate over a []const u8, yield fields
//   - Fields separated by commas; rows by newlines
//   - Return slices into the original buffer (zero-copy)
//   - Handle quoted fields: "hello, world" treated as one field
//
// TODO 2: CsvReader struct
//   const CsvReader = struct {
//       buf: []const u8,
//       pos: usize = 0,
//       pub fn nextRow(self: *CsvReader) ?[]const u8 { ... }
//       pub fn parseRow(row: []const u8, allocator: std.mem.Allocator) ![][]const u8 { ... }
//   };
//
// TODO 3: Stream large files without loading into memory
//   - Read in 4 KB chunks using std.fs.File.reader()
//   - Maintain partial-row state across chunk boundaries
//
// TODO 4: Write CSV — format [][]const u8 back to CSV string
//   - Quote fields containing commas or newlines
//   - Use std.ArrayList(u8) as output buffer

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    // const allocator = gpa.allocator();

    const stdout = std.io.getStdOut().writer();
    try stdout.print("CSV Parser — TODO: implement\n", .{});
}
