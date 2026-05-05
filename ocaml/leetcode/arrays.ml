(* TOPIC: Array LeetCode Problems | ocaml arrays.ml *)

(* TODO 1: Two Sum — LC #1
   let two_sum nums target =
     (* O(n) using Hashtbl: tbl maps value → index *)
     (* let tbl = Hashtbl.create 16 in List.iteri ... *)  *)

(* TODO 2: Best Time to Buy and Sell Stock — LC #121
   let max_profit prices =
     (* Track min price; max_profit = max(profit, price - min_price) *)
     (* List.fold_left with (min_price, max_profit) as accumulator *)  *)

(* TODO 3: Container With Most Water — LC #11
   let max_area height =
     (* Two pointer; convert to array for O(1) access *)  *)

(* TODO 4: Product of Array Except Self — LC #238
   let product_except_self nums =
     (* Prefix products then suffix products; no division *)  *)

(* TODO 5: Maximum Subarray (Kadane's) — LC #53
   let max_sub_array nums =
     (* List.fold_left with (current_sum, max_sum) accumulator *)  *)

(* TODO 6: Merge Intervals — LC #56
   let merge intervals =
     (* List.sort then merge overlapping *)  *)

(* TODO 7: Find Minimum in Rotated Sorted Array — LC #153
   let find_min nums =
     (* Binary search on array; if nums[mid] > nums[right] min is right *)  *)

let () = print_endline "TODO: implement array problems"
