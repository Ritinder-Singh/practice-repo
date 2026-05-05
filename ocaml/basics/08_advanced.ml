(* TOPIC: Advanced OCaml | ocaml 08_advanced.ml *)

(* TODO 1: Polymorphic functions and type variables *)
(*   let identity x = x                   (* 'a -> 'a *)
     let swap (a, b) = (b, a)             (* 'a * 'b -> 'b * 'a *)
     let const x _ = x                   (* 'a -> 'b -> 'a *)
     let ( |> ) x f = f x               (* 'a -> ('a -> 'b) -> 'b *)  *)

(* TODO 2: GADT introduction — Generalized Algebraic Data Types *)
(*   type _ expr =
       | Int   : int  -> int  expr
       | Bool  : bool -> bool expr
       | Add   : int  expr * int  expr -> int  expr
       | Eq    : int  expr * int  expr -> bool expr
       | If    : bool expr * 'a expr * 'a expr -> 'a expr
     let rec eval : type a. a expr -> a = function
       | Int n    -> n
       | Bool b   -> b
       | Add(a,b) -> eval a + eval b
       | Eq(a,b)  -> eval a = eval b
       | If(c,t,f)-> if eval c then eval t else eval f  *)

(* TODO 3: PPX (preprocessor extensions) — metaprogramming *)
(*   (* [@@deriving show, eq, ord] auto-generates print/compare functions *)
     (* Requires: opam install ppx_deriving *)
     type point = { x: float; y: float } [@@deriving show, eq]
     let p = { x = 1.0; y = 2.0 } in
     Printf.printf "%s\n" (show_point p)
     Printf.printf "%b\n" (equal_point p { x = 1.0; y = 2.0 })  *)

(* TODO 4: Phantom types — encode state in type parameter *)
(*   type locked
     type unlocked
     type 'state door = Door of int
     let lock   : unlocked door -> locked   door = fun (Door id) -> Door id
     let unlock : locked   door -> unlocked door = fun (Door id) -> Door id
     let open_door : unlocked door -> string = fun (Door id) -> Printf.sprintf "Door %d opened" id
     (* open_door (lock (Door 1)) -- would be a TYPE ERROR  *)  *)

(* TODO 5: Recursive modules *)
(*   module rec Tree : sig
       type t = Leaf | Node of t * int * t
       val size : t -> int
       val mem  : int -> t -> bool
     end = struct
       type t = Leaf | Node of t * int * t
       let rec size = function Leaf -> 0 | Node(l,_,r) -> 1 + Tree.size l + Tree.size r
       let rec mem x = function
         | Leaf -> false
         | Node(l, v, r) -> v = x || Tree.mem x l || Tree.mem x r
     end  *)

(* TODO 6: Local abstract types — type hiding in function scope *)
(*   let create_stack () : (module sig
       val push : int -> unit
       val pop  : unit -> int option
     end) =
       let data = ref [] in
       (module struct
         let push x = data := x :: !data
         let pop () = match !data with [] -> None | x::xs -> data := xs; Some x
       end)  *)

(* TODO 7: Memoization using Hashtbl *)
(*   let memoize f =
       let cache = Hashtbl.create 16 in
       fun x ->
         match Hashtbl.find_opt cache x with
         | Some v -> v
         | None ->
           let v = f x in
           Hashtbl.add cache x v;
           v
     let rec fib_unmemo n = if n <= 1 then n else fib_unmemo(n-1) + fib_unmemo(n-2)
     let fib = memoize (fun n -> fib_unmemo n)  *)

(* TODO 8: Effect handlers (OCaml 5) — resumable exceptions *)
(*   type _ Effect.t += Ask : string -> string Effect.t
     let program () =
       let name = Effect.perform (Ask "What is your name?") in
       Printf.printf "Hello, %s!\n" name
     let () =
       Effect.Deep.match_with program () {
         retc = (fun () -> ());
         exnc = raise;
         effc = fun (type a) (eff: a Effect.t) ->
           match eff with
           | Ask prompt ->
             Some (fun (k: (a, _) Effect.Deep.continuation) ->
               Printf.printf "%s " prompt;
               let answer = input_line stdin in
               Effect.Deep.continue k answer)
           | _ -> None
       }  *)

let () = print_endline "TODO: implement advanced OCaml exercises"
