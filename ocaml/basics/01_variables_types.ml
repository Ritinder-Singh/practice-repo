(* TOPIC: Variables & Types | ocaml 01_variables_types.ml *)
(* Docs: https://ocaml.org/docs/values-and-functions *)

(* TODO 1: let bindings — immutable by default *)
(*   let x = 42 in                         (* local binding *)
     let y : string = "hello" in           (* explicit type annotation *)
     let () = print_endline (string_of_int x ^ " " ^ y)  (* unit binding *)   *)

(* TODO 2: Basic types *)
(*   int    — unboxed, usually 63-bit on 64-bit systems *)
(*   float  — 64-bit IEEE 754; float operators: +. -. *. /. *)
(*   bool   — true | false *)
(*   char   — single character: 'a' *)
(*   string — immutable byte sequence *)
(*   unit   — () ; like void *)
(*   Demonstrate: let ratio = float_of_int 3 /. float_of_int 4 *)

(* TODO 3: ref cells — mutable state *)
(*   let r = ref 0 in         (* create ref *)
     r := !r + 1;             (* update: := assigns, ! dereferences *)
     Printf.printf "%d\n" !r  *)

(* TODO 4: Tuples — ordered, heterogeneous, fixed-size *)
(*   let pair = (1, "hello") in
     let (a, b) = pair in                  (* pattern match to destructure *)
     let fst (x, _) = x in                (* first element *)
     Printf.printf "%d %s\n" a b  *)

(* TODO 5: Lists — singly linked, homogeneous, immutable *)
(*   let nums = [1; 2; 3; 4; 5] in
     let head = List.hd nums in            (* first element *)
     let tail = List.tl nums in            (* rest *)
     let prepended = 0 :: nums in         (* :: cons operator *)
     let doubled = List.map (fun x -> x * 2) nums in
     let sum = List.fold_left (+) 0 nums  *)

(* TODO 6: Option type — represents optional values (no null) *)
(*   let find_first pred lst =
       List.find_opt pred lst               (* returns Some x or None *)
     let safe_div a b = if b = 0 then None else Some (a / b)
     let result = Option.map (fun x -> x + 1) (safe_div 10 2)   *)

(* TODO 7: Records — named field tuples *)
(*   type person = { name: string; age: int; mutable score: int }
     let alice = { name = "Alice"; age = 30; score = 0 }
     alice.score <- 100;                   (* mutate the mutable field *)
     let older = { alice with age = alice.age + 1 }  (* record update syntax *)  *)

(* TODO 8: Variants (Algebraic Data Types) *)
(*   type shape =
       | Circle of float
       | Rectangle of float * float
       | Triangle of float * float * float
     let area = function
       | Circle r      -> Float.pi *. r *. r
       | Rectangle (w, h) -> w *. h
       | Triangle (a, b, c) ->
           let s = (a +. b +. c) /. 2.0 in
           sqrt (s *. (s-.a) *. (s-.b) *. (s-.c))  *)

let () = print_endline "TODO: implement variable/type exercises"
