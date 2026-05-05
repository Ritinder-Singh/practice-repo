// TOPIC: Array LeetCode Problems | dart arrays.dart
// Docs: https://leetcode.com/tag/array/

// TODO 1: Two Sum — LC #1
//   List<int> twoSum(List<int> nums, int target)
//   - O(n) HashMap: complement = target - num; return [map[complement], i] if found

// TODO 2: Best Time to Buy and Sell Stock — LC #121
//   int maxProfit(List<int> prices)
//   - Track minPrice seen so far; maxProfit = max(maxProfit, price - minPrice)

// TODO 3: Container With Most Water — LC #11
//   int maxArea(List<int> height)
//   - Two pointers; area = min(h[left], h[right]) * (right - left); advance shorter side

// TODO 4: Product of Array Except Self — LC #238
//   List<int> productExceptSelf(List<int> nums)
//   - Prefix pass left→right, suffix pass right→left; O(n) time, O(1) extra space

// TODO 5: Maximum Subarray (Kadane's) — LC #53
//   int maxSubArray(List<int> nums)
//   - currentSum = max(num, currentSum + num); track global max

// TODO 6: Merge Intervals — LC #56
//   List<List<int>> merge(List<List<int>> intervals)
//   - Sort by start; merge if intervals[i][0] <= prev[1]

// TODO 7: Find Minimum in Rotated Sorted Array — LC #153
//   int findMin(List<int> nums)
//   - Binary search: if nums[mid] > nums[right], min is in right half

void main() {}
