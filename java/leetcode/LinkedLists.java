package leetcode;
// TOPIC: Linked List LeetCode Problems | javac LinkedLists.java && java leetcode.LinkedLists

public class LinkedLists {

    // Definition for singly-linked list node
    static class ListNode {
        int val;
        ListNode next;
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }

        // Helper: build list from array — ListNode.of(1, 2, 3, 4, 5)
        static ListNode of(int... vals) {
            // TODO: implement — create head, chain all nodes, return head
            return null;
        }

        // Helper: convert list to string for printing — "1 -> 2 -> 3 -> null"
        @Override public String toString() {
            // TODO: implement — walk list, append val -> val -> ... -> null
            return "";
        }
    }

    // TODO 1: Reverse Linked List — LC #206 — iterative and recursive
    //   ListNode reverseList(ListNode head)
    //   - Iterative: prev=null, curr=head; while curr: next=curr.next, curr.next=prev, prev=curr, curr=next
    //   - Recursive: if head==null || head.next==null return head;
    //                ListNode newHead = reverseList(head.next);
    //                head.next.next = head;  head.next = null;  return newHead;
    //   - Example: 1→2→3→4→5 → 5→4→3→2→1

    // TODO 2: Merge Two Sorted Lists — LC #21 — iterative with dummy node
    //   ListNode mergeTwoLists(ListNode list1, ListNode list2)
    //   - Dummy head: ListNode dummy = new ListNode(0); ListNode curr = dummy;
    //   - While both non-null: compare vals, attach smaller, advance its pointer
    //   - After loop: attach remaining non-null list directly (already sorted)
    //   - Return dummy.next
    //   - Example: 1→2→4 and 1→3→4 → 1→1→2→3→4→4

    // TODO 3: Linked List Cycle Detection — LC #141 — Floyd's tortoise and hare
    //   boolean hasCycle(ListNode head)
    //   - Slow pointer advances 1 step; fast pointer advances 2 steps
    //   - If fast or fast.next is null → no cycle (reached end)
    //   - If slow == fast → cycle detected
    //   - Follow-up LC #142: find START of cycle
    //     After detection, reset slow to head; advance both one step at a time; meeting point = cycle start

    // TODO 4: Remove Nth Node From End of List — LC #19 — two pointer, single pass
    //   ListNode removeNthFromEnd(ListNode head, int n)
    //   - Dummy head points to head (handles removing head node case)
    //   - Advance fast pointer n+1 steps from dummy
    //   - Advance both slow and fast until fast == null
    //   - slow.next = slow.next.next  (skip the target node)
    //   - Return dummy.next
    //   - Example: 1→2→3→4→5, n=2 → 1→2→3→5  (4 is removed)

    // TODO 5: Merge K Sorted Lists — LC #23 — min-heap (PriorityQueue)
    //   ListNode mergeKLists(ListNode[] lists)
    //   - PriorityQueue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
    //   - Add all non-null list heads to pq
    //   - Poll minimum node, attach to result, push polled.next into pq if non-null
    //   - O(N log k) where N = total nodes, k = number of lists
    //   - Alternative: divide and conquer — merge pairs repeatedly, O(N log k) same complexity

    // TODO 6: Reorder List — LC #143 — find middle + reverse + merge
    //   void reorderList(ListNode head)
    //   - Step 1: Find middle using slow/fast pointers
    //   - Step 2: Reverse second half of list
    //   - Step 3: Merge two halves — take one from first, one from (reversed) second, alternate
    //   - In-place, O(1) space — do NOT use extra data structures
    //   - Example: 1→2→3→4→5 → 1→5→2→4→3

    public static void main(String[] args) {
        // TODO: build test lists using ListNode.of(...) and call each method
        // Print before and after using toString()

        // Test TODO 1: Reverse
        // ListNode list = ListNode.of(1, 2, 3, 4, 5);
        // System.out.println("Before: " + list);
        // System.out.println("After:  " + new LinkedLists().reverseList(list));

        // Test TODO 2: Merge two sorted lists
        // Test TODO 3: Cycle detection (manually create cycle with node.next = earlier node)
        // Test TODO 4: Remove Nth from end
        // Test TODO 5: Merge K sorted lists
        // Test TODO 6: Reorder list
    }
}
