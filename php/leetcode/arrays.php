<?php
declare(strict_types=1);
// TOPIC: Array LeetCode Problems | php arrays.php

// TODO 1: Two Sum — LC #1
//   function twoSum(array $nums, int $target): array
//   // O(n) hash map: $complement = $target - $num; return [$map[$complement], $i] if found

// TODO 2: Best Time to Buy and Sell Stock — LC #121
//   function maxProfit(array $prices): int
//   // Track min price; $maxProfit = max($maxProfit, $price - $minPrice)

// TODO 3: Container With Most Water — LC #11
//   function maxArea(array $height): int
//   // Two pointers; advance the shorter side

// TODO 4: Product of Array Except Self — LC #238
//   function productExceptSelf(array $nums): array
//   // Prefix + suffix product arrays; no division

// TODO 5: Maximum Subarray (Kadane's) — LC #53
//   function maxSubArray(array $nums): int
//   // $current = max($num, $current + $num); track max

// TODO 6: Merge Intervals — LC #56
//   function merge(array $intervals): array
//   // usort by start; merge if $intervals[$i][0] <= $prev[1]

// TODO 7: Find Minimum in Rotated Sorted Array — LC #153
//   function findMin(array $nums): int
//   // Binary search: if $nums[$mid] > $nums[$right], min is in right half
