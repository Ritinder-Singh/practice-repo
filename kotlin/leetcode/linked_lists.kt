package leetcode
// TOPIC: Linked List Problems | kotlinc linked_lists.kt -include-runtime -d out.jar && java -jar out.jar

class ListNode(var `val`: Int, var next: ListNode? = null)

// Helper: build a linked list from vararg ints, e.g. listOf(1, 2, 3)
fun buildList(vararg vals: Int): ListNode? {
    val dummy = ListNode(0)
    var cur = dummy
    for (v in vals) { cur.next = ListNode(v); cur = cur.next!! }
    return dummy.next
}

// Helper: print a linked list as [1 -> 2 -> 3 -> null]
fun printList(head: ListNode?) {
    val sb = StringBuilder("[")
    var cur = head
    while (cur != null) { sb.append(cur.`val`); if (cur.next != null) sb.append(" -> "); cur = cur.next }
    sb.append("]")
    println(sb)
}

fun main() {
    // TODO 1: LC #206 — Reverse Linked List
    //   - Input: 1 -> 2 -> 3 -> 4 -> 5 → Output: 5 -> 4 -> 3 -> 2 -> 1
    //   - Strategy A (iterative): three pointers prev/curr/next, rewire links
    //   - Strategy B (recursive): reverse(head.next), make head.next.next = head
    //   - fun reverseList(head: ListNode?): ListNode?
    //   - Test: buildList(1,2,3,4,5).let { printList(reverseList(it)) }

    // TODO 2: LC #21 — Merge Two Sorted Lists
    //   - Input: l1 = 1->2->4, l2 = 1->3->4 → Output: 1->1->2->3->4->4
    //   - Strategy: dummy head, compare l1.val vs l2.val, advance the smaller
    //   - fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode?
    //   - Append remaining nodes after one list is exhausted

    // TODO 3: LC #141 — Linked List Cycle
    //   - Input: list with a cycle → Output: true
    //   - Strategy: Floyd's cycle detection — slow pointer moves 1, fast moves 2
    //   - fun hasCycle(head: ListNode?): Boolean
    //   - If fast catches slow → cycle; if fast reaches null → no cycle
    //   - Follow-up LC #142: find the start of the cycle

    // TODO 4: LC #19 — Remove Nth Node From End of List
    //   - Input: 1->2->3->4->5, n=2 → Output: 1->2->3->5
    //   - Strategy: two-pointer — advance fast pointer n steps first, then move both
    //   - fun removeNthFromEnd(head: ListNode?, n: Int): ListNode?
    //   - Use dummy head to handle edge case of removing the first node

    // TODO 5: LC #23 — Merge K Sorted Lists
    //   - Input: lists = [[1,4,5],[1,3,4],[2,6]] → Output: 1->1->2->3->4->4->5->6
    //   - Strategy A: min-heap (PriorityQueue) — always pop smallest node, O(n log k)
    //   - Strategy B: divide-and-conquer — merge pairs repeatedly, O(n log k)
    //   - fun mergeKLists(lists: Array<ListNode?>): ListNode?
    //   - PriorityQueue comparator: compareBy { it.`val` }

    // TODO 6: LC #143 — Reorder List
    //   - Input: 1->2->3->4->5 → Output: 1->5->2->4->3
    //   - Strategy: 3 steps:
    //     1. Find middle with slow/fast pointers
    //     2. Reverse the second half
    //     3. Merge the two halves by interleaving
    //   - fun reorderList(head: ListNode?)
    //   - In-place, O(n) time, O(1) space
}
