#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
// TOPIC: Arrays — LeetCode | g++ -std=c++20 -o out arrays.cpp && ./out

int main() { std::cout << "Arrays LeetCode — TODO: implement\n"; return 0; }

// TODO 1: Two Sum — LeetCode #1
//   vector<int> twoSum(vector<int>& nums, int target)
//   unordered_map<int,int>: store complement → index. O(n).

// TODO 2: Best Time to Buy and Sell Stock — LeetCode #121
//   int maxProfit(vector<int>& prices)
//   Track minPrice; maxProfit = max(maxProfit, price - minPrice). O(n).

// TODO 3: Product of Array Except Self — LeetCode #238
//   vector<int> productExceptSelf(vector<int>& nums)
//   Prefix pass then suffix pass. No division. O(n) O(1) extra.

// TODO 4: Maximum Subarray — LeetCode #53
//   int maxSubArray(vector<int>& nums)
//   Kadane's algorithm. O(n).

// TODO 5: Merge Intervals — LeetCode #56
//   vector<vector<int>> merge(vector<vector<int>>& intervals)
//   Sort by start; merge overlapping. O(n log n).

// TODO 6: Find Minimum in Rotated Sorted Array — LeetCode #153
//   int findMin(vector<int>& nums)
//   Binary search comparing mid vs right. O(log n).

// TODO 7: Container With Most Water — LeetCode #11
//   int maxArea(vector<int>& height)
//   Two pointers at ends; move shorter side inward. O(n).

// TODO 8: Trapping Rain Water — LeetCode #42
//   int trap(vector<int>& height)
//   Two pointers; track maxLeft, maxRight; accumulate water. O(n) O(1).
