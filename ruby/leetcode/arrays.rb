# frozen_string_literal: true
# TOPIC: Array LeetCode Problems | ruby arrays.rb
# Docs: https://leetcode.com/tag/array/

# TODO 1: Two Sum — LC #1
#   def two_sum(nums, target)
#     # O(n) hash map: complement = target - num; return [map[complement], i] if found
#   end

# TODO 2: Best Time to Buy and Sell Stock — LC #121
#   def max_profit(prices)
#     # Track min_price seen so far; max_profit = max(profit, price - min_price)
#   end

# TODO 3: Container With Most Water — LC #11
#   def max_area(height)
#     # Two pointers: left=0, right=last; move the shorter side inward
#   end

# TODO 4: Product of Array Except Self — LC #238
#   def product_except_self(nums)
#     # Pass 1: prefix products left→right; Pass 2: suffix products right→left; no division
#   end

# TODO 5: Maximum Subarray (Kadane's) — LC #53
#   def max_sub_array(nums)
#     # current_sum = max(num, current_sum + num); track max
#   end

# TODO 6: Rotate Array — LC #189
#   def rotate(nums, k)
#     # Reverse whole array, reverse first k, reverse remaining (in-place)
#   end

# TODO 7: Merge Intervals — LC #56
#   def merge(intervals)
#     # Sort by start; iterate and merge overlapping [a,b] + [c,d] where c <= b → [a, max(b,d)]
#   end

# TODO 8: Find Minimum in Rotated Sorted Array — LC #153
#   def find_min(nums)
#     # Binary search: if nums[mid] > nums[right], min is in right half
#   end
