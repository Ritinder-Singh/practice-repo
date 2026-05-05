(* TOPIC: Loops & Control Flow | ocaml 03_loops_control_flow.ml *)

(* TODO 1: Imperative for loop — only ascending, no return value *)
(*   for i = 1 to 10 do
       Printf.printf "%d " i
     done;
     for i = 10 downto 1 do  (* downto for descending *)
       Printf.printf "%d " i
     done  *)

(* TODO 2: while loop — mutable state required *)
(*   let i = ref 0 in
     while !i < 10 do
       Printf.printf "%d " !i;
       i := !i + 1
     done  *)

(* TODO 3: Functional recursion — preferred over loops in OCaml *)
(*   let rec range a b =
       if a > b then [] else a :: range (a+1) b
     let rec iterate f n x =
       if n = 0 then x else iterate f (n-1) (f x)  *)

(* TODO 4: Pattern matching — exhaustive, no fallthrough *)
(*   let describe n = match n with
       | 0 -> "zero"
       | 1 -> "one"
       | n when n < 0 -> "negative"
       | n when n mod 2 = 0 -> "positive even"
       | _ -> "positive odd"
     (* Match with tuples: *)
     let sign_pair (a, b) = match (a > 0, b > 0) with
       | (true, true) -> "both positive"
       | (false, false) -> "both negative"
       | _ -> "mixed"  *)

(* TODO 5: if expressions — always returns a value *)
(*   let abs x = if x >= 0 then x else -x
     let max_val a b = if a > b then a else b
     (* Note: if without else returns unit, so branches must match types *)  *)

(* TODO 6: List.iter and List.iteri — side-effect loops over lists *)
(*   List.iter (Printf.printf "%d ") [1;2;3;4;5];
     List.iteri (fun i x -> Printf.printf "[%d]=%d " i x) [10;20;30]  *)

(* TODO 7: Sequence operations with |> (pipe operator) *)
(*   [1;2;3;4;5;6;7;8;9;10]
     |> List.filter (fun x -> x mod 2 = 0)
     |> List.map (fun x -> x * x)
     |> List.fold_left (+) 0
     |> Printf.printf "Sum of even squares: %d\n"  *)

(* TODO 8: Recursion with accumulator — FizzBuzz *)
(*   let fizzbuzz n =
       let rec go i =
         if i > n then ()
         else begin
           (match (i mod 3, i mod 5) with
             | (0, 0) -> print_endline "FizzBuzz"
             | (0, _) -> print_endline "Fizz"
             | (_, 0) -> print_endline "Buzz"
             | _      -> print_int i; print_newline ());
           go (i + 1)
         end
       in go 1  *)

let () = print_endline "TODO: implement control flow exercises"
