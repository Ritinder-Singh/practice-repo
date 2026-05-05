(* TOPIC: Data Structures | ocaml 04_data_structures.ml *)

(* TODO 1: List — fundamental functional data structure *)
(*   [1; 2; 3] |> List.length          (* 3 *)
     [1; 2; 3] |> List.rev             (* [3;2;1] *)
     [1;2] @ [3;4]                      (* append: O(n) *)
     List.nth [10;20;30] 1             (* 20 — O(n) *)
     List.sort compare [3;1;2]         (* [1;2;3] *)
     List.sort_uniq compare [3;1;2;1]  (* [1;2;3] *)  *)

(* TODO 2: Array — fixed-size, O(1) access, mutable *)
(*   let arr = [|1; 2; 3; 4; 5|]
     arr.(2)                            (* 3 — 0-indexed *)
     arr.(2) <- 99                      (* mutate *)
     Array.length arr                  (* 5 *)
     Array.map (fun x -> x * 2) arr
     Array.sort compare arr  *)

(* TODO 3: Hashtbl — mutable hash table *)
(*   let h = Hashtbl.create 16 in       (* initial size hint *)
     Hashtbl.add h "alice" 30;
     Hashtbl.add h "bob" 25;
     Hashtbl.find h "alice";           (* 30; raises Not_found if absent *)
     Hashtbl.find_opt h "carol";       (* None *)
     Hashtbl.mem h "bob";             (* true *)
     Hashtbl.remove h "bob";
     Hashtbl.iter (fun k v -> Printf.printf "%s: %d\n" k v) h  *)

(* TODO 4: Stack from stdlib *)
(*   let s = Stack.create () in
     Stack.push 1 s; Stack.push 2 s; Stack.push 3 s;
     Stack.pop s;                      (* 3 — LIFO *)
     Stack.top s;                      (* 2 — peek without removing *)
     Stack.is_empty s  *)

(* TODO 5: Queue from stdlib *)
(*   let q = Queue.create () in
     Queue.push 1 q; Queue.push 2 q;
     Queue.pop q;                      (* 1 — FIFO *)
     Queue.peek q;                     (* 2 *)  *)

(* TODO 6: Custom linked list type *)
(*   type 'a node = { value: 'a; mutable next: 'a node option }
     type 'a linked_list = { mutable head: 'a node option; mutable length: int }
     let create () = { head = None; length = 0 }
     let push_front lst v =
       let node = { value = v; next = lst.head } in
       lst.head <- Some node;
       lst.length <- lst.length + 1  *)

(* TODO 7: Map module — purely functional balanced BST map *)
(*   module StringMap = Map.Make(String)
     let m = StringMap.empty
           |> StringMap.add "alice" 30
           |> StringMap.add "bob" 25
     StringMap.find "alice" m             (* 30 *)
     StringMap.mem "carol" m             (* false *)
     StringMap.bindings m                (* association list *)  *)

(* TODO 8: Set module — purely functional balanced BST set *)
(*   module IntSet = Set.Make(Int)
     let s = IntSet.of_list [3; 1; 4; 1; 5; 9; 2; 6]
     IntSet.mem 4 s                      (* true *)
     IntSet.min_elt s                    (* 1 *)
     IntSet.inter (IntSet.of_list [1;2;3]) (IntSet.of_list [2;3;4])  *)

let () = print_endline "TODO: implement data structure exercises"
