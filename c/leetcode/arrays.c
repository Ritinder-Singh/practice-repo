#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// TOPIC: Arrays — LeetCode | gcc -o out arrays.c && ./out

int main(void) { printf("Arrays LeetCode — TODO: implement\n"); return 0; }

// TODO 1: Two Sum — LeetCode #1
//   int *twoSum(int *nums, int numsSize, int target, int *returnSize)
//   Use a hash map (open-addressed) or sort + two-pointer. O(n).

// TODO 2: Best Time to Buy and Sell Stock — LeetCode #121
//   int maxProfit(int *prices, int pricesSize)
//   Track minPrice; update maxProfit = max(maxProfit, price - minPrice). O(n).

// TODO 3: Product of Array Except Self — LeetCode #238
//   int *productExceptSelf(int *nums, int n, int *returnSize)
//   Prefix pass then suffix pass, multiply into output array. No division. O(n).

// TODO 4: Maximum Subarray — LeetCode #53
//   int maxSubArray(int *nums, int numsSize)
//   Kadane's: curr = max(nums[i], curr + nums[i]); best = max(best, curr). O(n).

// TODO 5: Merge Intervals — LeetCode #56
//   int **merge(int **intervals, int n, int *colSizes, int *returnSize)
//   Sort by start (qsort); merge overlapping intervals. O(n log n).

// TODO 6: Find Minimum in Rotated Sorted Array — LeetCode #153
//   int findMin(int *nums, int numsSize)
//   Binary search: if nums[mid] > nums[right] → min in right half. O(log n).

// TODO 7: Search in Rotated Sorted Array — LeetCode #33
//   int search(int *nums, int numsSize, int target)
//   Binary search with rotation check: determine which half is sorted. O(log n).

// TODO 8: 3Sum — LeetCode #15
//   int **threeSum(int *nums, int n, int *returnSize, int **returnColSizes)
//   Sort; fix one element, two-pointer for remaining two. Skip duplicates. O(n²).
