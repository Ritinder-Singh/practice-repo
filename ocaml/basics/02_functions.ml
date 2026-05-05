(* TOPIC: Functions | ocaml 02_functions.ml *)
(* Docs: https://ocaml.org/docs/values-and-functions *)

(* TODO 1: Basic function definitions — all functions are curried by default *)
(*   let add x y = x + y                   (* curried: add : int -> int -> int *)
     let add5 = add 5                       (* partial application: int -> int *)
     let double = ( * ) 2                   (* operator as function *)  *)

(* TODO 2: Anonymous functions *)
(*   let square = fun x -> x * x
     let apply f x = f x
     let result = apply (fun x -> x + 1) 41  *)

(* TODO 3: Recursive functions — must use let rec *)
(*   let rec factorial n =
       if n <= 1 then 1 else n * factorial (n - 1)
     let rec fib n =
       if n <= 1 then n else fib (n-1) + fib (n-2)  *)

(* TODO 4: Higher-order functions — implement from scratch *)
(*   let rec my_map f = function
       | [] -> []
       | x :: xs -> f x :: my_map f xs
     let rec my_filter p = function
       | [] -> []
       | x :: xs -> if p x then x :: my_filter p xs else my_filter p xs
     let rec my_fold_left f acc = function
       | [] -> acc
       | x :: xs -> my_fold_left f (f acc x) xs  *)

(* TODO 5: Labeled arguments — ~label: *)
(*   let greet ~name ~greeting = greeting ^ ", " ^ name ^ "!"
     greet ~name:"Alice" ~greeting:"Hello"
     greet ~greeting:"Hi" ~name:"Bob"    (* can reorder labeled args *)  *)

(* TODO 6: Optional arguments — ?label *)
(*   let connect ?(port=80) host =
       Printf.sprintf "Connecting to %s:%d" host port
     connect "example.com"               (* uses default port 80 *)
     connect ~port:443 "secure.com"      *)

(* TODO 7: Function composition *)
(*   let ( >> ) f g x = g (f x)          (* pipe: x |> f |> g *)
     let ( << ) f g x = f (g x)          (* compose: f ∘ g *)
     let process = String.trim >> String.lowercase_ascii >> String.length  *)

(* TODO 8: Tail recursion — avoids stack overflow for large n *)
(*   let factorial n =
       let rec go acc n = if n <= 1 then acc else go (acc * n) (n - 1) in
       go 1 n
     (* OCaml optimizes tail-recursive calls; non-tail fib would stack overflow for large n *)  *)

let () = print_endline "TODO: implement function exercises"
