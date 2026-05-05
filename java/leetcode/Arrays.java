package leetcode;
// TOPIC: Array LeetCode Problems | javac Arrays.java && java leetcode.Arrays

public class Arrays {

    // TODO 1: Two Sum — LC #1 — O(n) HashMap approach
    //   int[] twoSum(int[] nums, int target)
    //   - One pass: store each num's index in HashMap while checking if (target - num) exists
    //   - Return indices (not values); each input has exactly one solution; don't use same element twice
    //   - Example: nums=[2,7,11,15], target=9 → [0,1]  (2+7=9)

    // TODO 2: Best Time to Buy and Sell Stock — LC #121 — single pass
    //   int maxProfit(int[] prices)
    //   - Track minPrice so far (initialized to Integer.MAX_VALUE)
    //   - At each price: update minPrice, update maxProfit = max(maxProfit, price - minPrice)
    //   - Buy low, sell high; must buy before selling; return 0 if no profit possible
    //   - Example: prices=[7,1,5,3,6,4] → 5  (buy at 1, sell at 6)

    // TODO 3: Container With Most Water — LC #11 — two pointer
    //   int maxArea(int[] height)
    //   - Left pointer at 0, right pointer at end; area = min(height[l], height[r]) * (r - l)
    //   - Move the pointer with the SHORTER height inward (moving taller can only decrease area)
    //   - Example: height=[1,8,6,2,5,4,8,3,7] → 49

    // TODO 4: Product of Array Except Self — LC #238 — prefix/suffix, O(1) extra space
    //   int[] productExceptSelf(int[] nums)
    //   - Pass 1 (left to right): result[i] = product of all elements to the LEFT of i
    //   - Pass 2 (right to left): multiply result[i] by running suffix product from the right
    //   - No division allowed; output array does not count as extra space
    //   - Example: nums=[1,2,3,4] → [24,12,8,6]

    // TODO 5: Maximum Subarray (Kadane's Algorithm) — LC #53
    //   int maxSubArray(int[] nums)
    //   - currentSum = max(nums[i], currentSum + nums[i])  — reset if sum goes negative
    //   - maxSum = max(maxSum, currentSum)  — track global best
    //   - At least one element must be chosen; handles all-negative arrays
    //   - Example: nums=[-2,1,-3,4,-1,2,1,-5,4] → 6  (subarray [4,-1,2,1])

    // TODO 6: Rotate Array — LC #189 — in-place reverse trick, O(1) space
    //   void rotate(int[] nums, int k)
    //   - Normalize: k = k % nums.length
    //   - Step 1: reverse entire array
    //   - Step 2: reverse first k elements
    //   - Step 3: reverse remaining n-k elements
    //   - Helper: void reverse(int[] nums, int left, int right)
    //   - Example: nums=[1,2,3,4,5,6,7], k=3 → [5,6,7,1,2,3,4]

    // TODO 7: Merge Intervals — LC #56 — sort then merge
    //   int[][] merge(int[][] intervals)
    //   - Sort by start time: Arrays.sort(intervals, (a, b) -> a[0] - b[0])
    //   - Iterate: if current start <= last merged end → merge (update end to max of both ends)
    //              else → add current interval as new entry in result
    //   - Use List<int[]> result, convert to array at end: result.toArray(new int[0][])
    //   - Example: [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]

    public static void main(String[] args) {
        // TODO: instantiate the class and call each method with test cases
        // Print expected vs actual output for each problem
    }
}
