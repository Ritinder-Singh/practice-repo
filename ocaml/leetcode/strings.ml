(* TOPIC: String LeetCode Problems | ocaml strings.ml *)

(* TODO 1: Longest Substring Without Repeating Characters — LC #3
   let length_of_longest_substring s =
     (* Sliding window with Hashtbl of char → last index *)  *)

(* TODO 2: Valid Anagram — LC #242
   let is_anagram s t =
     (* Sort both strings and compare; or count char frequencies *)  *)

(* TODO 3: Group Anagrams — LC #49
   let group_anagrams strs =
     (* Key = sorted chars string; group via Hashtbl *)  *)

(* TODO 4: Longest Palindromic Substring — LC #5
   let longest_palindrome s =
     (* Expand around center for each index *)  *)

(* TODO 5: Minimum Window Substring — LC #76
   let min_window s t =
     (* Sliding window; need and have Hashtbls *)  *)

(* TODO 6: Encode/Decode Strings — LC #271
   let encode strs =
     (* String.concat with length-prefix: "4#word" format *)
   let decode s = () (* parse length prefix *)  *)

(* TODO 7: Find All Anagrams in a String — LC #438
   let find_anagrams s p =
     (* Fixed sliding window of size String.length p *)  *)

let () = print_endline "TODO: implement string problems"
