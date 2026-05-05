(* TOPIC: Dynamic Programming LeetCode Problems | ocaml dynamic_programming.ml *)

(* TODO 1: Climbing Stairs — LC #70
   let climb_stairs n =
     (* dp.(i) <- dp.(i-1) + dp.(i-2) using Array *)  *)

(* TODO 2: Coin Change — LC #322
   let coin_change coins amount =
     (* dp array; dp.(0)=0, dp.(i) = min over all coins *)  *)

(* TODO 3: Longest Increasing Subsequence — LC #300
   let length_of_lis nums =
     (* dp.(i) = max LIS ending at i; O(n²) or O(n log n) *)  *)

(* TODO 4: Longest Common Subsequence — LC #1143
   let longest_common_subsequence text1 text2 =
     (* 2D dp array *)  *)

(* TODO 5: 0/1 Knapsack (classic)
   let knapsack weights values capacity =
     (* 2D dp or 1D with backward iteration *)  *)

(* TODO 6: Decode Ways — LC #91
   let num_decodings s =
     (* dp.(i) = ways to decode s[0..i-1] *)  *)

(* TODO 7: Word Break — LC #139
   let word_break s word_dict =
     (* dp.(i) = can s[0..i-1] be segmented *)  *)

let () = print_endline "TODO: implement DP problems"
