# frozen_string_literal: true
# TOPIC: Linked List LeetCode Problems | ruby linked_lists.rb

class ListNode
  attr_accessor :val, :next
  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

# TODO 1: Reverse Linked List — LC #206
#   def reverse_list(head)
#     # Iterative: prev=nil, curr=head; while curr: next=curr.next; curr.next=prev; prev=curr; curr=next
#   end

# TODO 2: Merge Two Sorted Lists — LC #21
#   def merge_two_lists(list1, list2)
#     # Dummy node; compare heads, advance the smaller one
#   end

# TODO 3: Linked List Cycle — LC #141
#   def has_cycle(head)
#     # Floyd's: slow=head, fast=head; slow=slow.next, fast=fast.next.next; meet if cycle
#   end

# TODO 4: Remove Nth Node From End of List — LC #19
#   def remove_nth_from_end(head, n)
#     # Two pointers n apart; when fast reaches end, slow is at target
#   end

# TODO 5: Merge K Sorted Lists — LC #23
#   def merge_k_lists(lists)
#     # Use min-heap (priority queue); push heads; pop min, add next from that list
#   end

# TODO 6: Reorder List — LC #143
#   def reorder_list(head)
#     # Find middle (slow/fast), reverse second half, merge two halves alternating
#   end
