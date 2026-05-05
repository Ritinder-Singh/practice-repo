(* TOPIC: Linked List LeetCode Problems | ocaml linked_lists.ml *)

(* Definition for linked list nodes *)
(* type 'a node = { mutable value: 'a; mutable next: 'a node option } *)

(* TODO 1: Reverse Linked List — LC #206
   let reverse_list head =
     (* Iterative: prev=None, curr=head; swap pointers *)  *)

(* TODO 2: Merge Two Sorted Lists — LC #21
   let merge_two_lists list1 list2 =
     (* Recursive: compare heads, advance smaller *)  *)

(* TODO 3: Linked List Cycle — LC #141
   let has_cycle head =
     (* Floyd's tortoise and hare *)  *)

(* TODO 4: Remove Nth Node From End — LC #19
   let remove_nth_from_end head n =
     (* Two pointers n apart *)  *)

(* TODO 5: Merge K Sorted Lists — LC #23
   let merge_k_lists lists =
     (* Min-heap approach using custom priority queue *)  *)

(* TODO 6: Reorder List — LC #143
   let reorder_list head =
     (* Find middle, reverse second half, merge alternating *)  *)

let () = print_endline "TODO: implement linked list problems"
