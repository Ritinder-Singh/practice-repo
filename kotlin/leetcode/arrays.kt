package leetcode
// TOPIC: Array Problems | kotlinc arrays.kt -include-runtime -d out.jar && java -jar out.jar
// Docs: https://kotlinlang.org/docs/arrays.html

fun main() {
    // TODO 1: LC #1 — Two Sum
    //   - Input: nums = [2,7,11,15], target = 9 → Output: [0,1]
    //   - Strategy: HashMap complement lookup — O(n) time, O(n) space
    //   - fun twoSum(nums: IntArray, target: Int): IntArray
    //   - Store seen values: map[complement] = index; check map.containsKey(nums[i])

    // TODO 2: LC #121 — Best Time to Buy and Sell Stock
    //   - Input: prices = [7,1,5,3,6,4] → Output: 5
    //   - Strategy: track minPrice so far, maxProfit = max(maxProfit, price - minPrice)
    //   - fun maxProfit(prices: IntArray): Int
    //   - Single pass O(n), no extra space

    // TODO 3: LC #238 — Product of Array Except Self
    //   - Input: nums = [1,2,3,4] → Output: [24,12,8,6]
    //   - Strategy: prefix product pass left→right, then suffix pass right→left
    //   - fun productExceptSelf(nums: IntArray): IntArray
    //   - No division allowed, O(n) time, O(1) extra space (output array doesn't count)

    // TODO 4: LC #11 — Container With Most Water
    //   - Input: height = [1,8,6,2,5,4,8,3,7] → Output: 49
    //   - Strategy: two-pointer — start at both ends, move the shorter side inward
    //   - fun maxArea(height: IntArray): Int
    //   - O(n) time, O(1) space

    // TODO 5: LC #53 — Maximum Subarray (Kadane's Algorithm)
    //   - Input: nums = [-2,1,-3,4,-1,2,1,-5,4] → Output: 6 (subarray [4,-1,2,1])
    //   - Strategy: currentSum = max(num, currentSum + num); track maxSum
    //   - fun maxSubArray(nums: IntArray): Int
    //   - O(n) time — classic DP/greedy

    // TODO 6: LC #56 — Merge Intervals
    //   - Input: intervals = [[1,3],[2,6],[8,10],[15,18]] → Output: [[1,6],[8,10],[15,18]]
    //   - Strategy: sort by start time, merge overlapping intervals greedily
    //   - fun merge(intervals: Array<IntArray>): Array<IntArray>
    //   - O(n log n) for sort, O(n) merge pass

    // TODO 7: LC #189 — Rotate Array
    //   - Input: nums = [1,2,3,4,5,6,7], k = 3 → Output: [5,6,7,1,2,3]
    //   - Strategy A (extra array): place each element at (i+k) % n position
    //   - Strategy B (in-place, 3 reverses): reverse all, reverse [0..k-1], reverse [k..n-1]
    //   - fun rotate(nums: IntArray, k: Int)
    //   - Strategy B: O(n) time, O(1) space
}
