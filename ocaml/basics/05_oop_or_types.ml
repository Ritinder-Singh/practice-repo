(* TOPIC: Modules, Signatures & Functors | ocaml 05_oop_or_types.ml *)
(* OCaml uses modules instead of classes for code organization *)

(* TODO 1: Module definition *)
(*   module Geometry = struct
       let pi = Float.pi
       type shape = Circle of float | Square of float
       let area = function
         | Circle r -> pi *. r *. r
         | Square s -> s *. s
       let perimeter = function
         | Circle r -> 2.0 *. pi *. r
         | Square s -> 4.0 *. s
     end
     Geometry.area (Geometry.Circle 5.0)
     let open Geometry in area (Square 3.0)  *)

(* TODO 2: Module signature (interface) — like a type for modules *)
(*   module type STACK = sig
       type 'a t
       val empty : 'a t
       val push  : 'a -> 'a t -> 'a t
       val pop   : 'a t -> ('a * 'a t) option
       val peek  : 'a t -> 'a option
       val is_empty : 'a t -> bool
     end
     module ListStack : STACK = struct
       type 'a t = 'a list
       let empty = []
       let push x s = x :: s
       let pop = function [] -> None | x :: s -> Some (x, s)
       let peek = function [] -> None | x :: _ -> Some x
       let is_empty = function [] -> true | _ -> false
     end  *)

(* TODO 3: Functors — modules parameterized by other modules *)
(*   module type ORDERED = sig
       type t
       val compare : t -> t -> int
     end
     module MakeSet (Ord: ORDERED) = struct
       type elt = Ord.t
       type t = Empty | Node of t * elt * t
       let rec mem x = function
         | Empty -> false
         | Node (l, v, r) ->
           let c = Ord.compare x v in
           if c = 0 then true
           else if c < 0 then mem x l
           else mem x r
     end
     module IntSet = MakeSet(Int)  *)

(* TODO 4: First-class modules — modules as values *)
(*   module type SERIALIZABLE = sig
       type t
       val to_string : t -> string
       val of_string : string -> t option
     end
     let serialize (type a) (module M : SERIALIZABLE with type t = a) (x : a) =
       M.to_string x  *)

(* TODO 5: Include — open and include module contents *)
(*   module ExtendedList = struct
       include List
       let sum = List.fold_left (+) 0
       let product = List.fold_left ( * ) 1
     end  *)

(* TODO 6: OCaml objects (rarely used, but exist) *)
(*   class counter = object
       val mutable count = 0
       method increment = count <- count + 1
       method get = count
       method reset = count <- 0
     end
     let c = new counter in
     c#increment; c#increment;
     Printf.printf "%d\n" c#get  *)

(* TODO 7: Polymorphic variants — more flexible than regular variants *)
(*   type color = [`Red | `Green | `Blue]
     type extended_color = [`Red | `Green | `Blue | `Yellow | `Purple]
     let describe : [< `Red | `Green | `Blue] -> string = function
       | `Red   -> "red"
       | `Green -> "green"
       | `Blue  -> "blue"  *)

(* TODO 8: Lazy values — defer evaluation *)
(*   let expensive = lazy (Printf.printf "Computing...\n"; 42)
     let result = Lazy.force expensive  (* triggers computation *)
     let result2 = Lazy.force expensive (* uses cached result — prints only once *)  *)

let () = print_endline "TODO: implement module exercises"
