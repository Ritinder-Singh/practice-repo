const std = @import("std");
// TOPIC: Data Structures | zig run 04_data_structures.zig

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    // TODO 1: ArrayList — dynamic array
    //   var list = std.ArrayList(i32).init(allocator);
    //   defer list.deinit();
    //   try list.append(1); try list.append(2); try list.append(3);
    //   list.items[0]         // 1
    //   list.items.len        // 3
    //   try list.insert(1, 99);  // insert at index 1
    //   _ = list.orderedRemove(0);  // remove at index 0
    //   list.clearRetainingCapacity();  // clear without dealloc

    // TODO 2: StringHashMap — string keys
    //   var map = std.StringHashMap(i32).init(allocator);
    //   defer map.deinit();
    //   try map.put("alice", 30);
    //   try map.put("bob", 25);
    //   const val = map.get("alice");  // ?i32 — optional
    //   var iter = map.iterator();
    //   while (iter.next()) |entry| {
    //       std.debug.print("{s}: {d}\n", .{entry.key_ptr.*, entry.value_ptr.*});
    //   }

    // TODO 3: AutoHashMap — infer key type
    //   var intMap = std.AutoHashMap(i32, []const u8).init(allocator);
    //   defer intMap.deinit();
    //   try intMap.put(1, "one"); try intMap.put(2, "two");

    // TODO 4: Linked list with allocator
    //   const Node = struct {
    //       value: i32,
    //       next: ?*Node = null,
    //       fn create(allocator: std.mem.Allocator, value: i32) !*Node {
    //           const node = try allocator.create(Node);
    //           node.* = .{ .value = value };
    //           return node;
    //       }
    //   };
    //   var head = try Node.create(allocator, 1);
    //   defer allocator.destroy(head);
    //   head.next = try Node.create(allocator, 2);
    //   defer allocator.destroy(head.next.?);

    // TODO 5: Stack using ArrayList
    //   var stack = std.ArrayList(i32).init(allocator);
    //   defer stack.deinit();
    //   try stack.append(1);    // push
    //   _ = stack.pop();        // pop (returns ?T — null if empty)
    //   stack.getLast()         // peek

    // TODO 6: Queue using TailQueue
    //   var queue = std.TailQueue(i32){};
    //   var node1 = std.TailQueue(i32).Node{ .data = 1 };
    //   queue.append(&node1);
    //   queue.popFirst()  // dequeue

    // TODO 7: MultiArrayList — struct-of-arrays for cache efficiency
    //   const Point = struct { x: f32, y: f32 };
    //   var points = std.MultiArrayList(Point){};
    //   defer points.deinit(allocator);
    //   try points.append(allocator, .{ .x = 1.0, .y = 2.0 });
    //   const xs = points.items(.x);  // []f32 — all x values contiguous in memory

    // TODO 8: BoundedArray — fixed-capacity stack-allocated array
    //   var buf = std.BoundedArray(i32, 10){};
    //   try buf.append(1); try buf.append(2);
    //   buf.slice()  // []i32

    std.debug.print("TODO: implement data structure exercises\n", .{});
    _ = allocator;
}
