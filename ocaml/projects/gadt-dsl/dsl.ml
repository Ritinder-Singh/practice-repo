(* PROJECT: Type-Safe DSL with GADTs (Exclusive) *)
(* GADTs let us encode type information in constructors *)
(* Run: ocaml dsl.ml *)

(* TODO 1: Define the typed expression GADT
   type _ expr =
     | Int   : int  -> int  expr
     | Bool  : bool -> bool expr
     | Add   : int  expr * int  expr -> int  expr
     | Sub   : int  expr * int  expr -> int  expr
     | Mul   : int  expr * int  expr -> int  expr
     | Eq    : int  expr * int  expr -> bool expr
     | Lt    : int  expr * int  expr -> bool expr
     | And   : bool expr * bool expr -> bool expr
     | Not   : bool expr -> bool expr
     | If    : bool expr * 'a expr * 'a expr -> 'a expr  *)

(* TODO 2: Evaluator — notice the return type changes with the GADT
   let rec eval : type a. a expr -> a = function
     | Int n      -> n
     | Bool b     -> b
     | Add (a, b) -> eval a + eval b
     | Sub (a, b) -> eval a - eval b
     | Mul (a, b) -> eval a * eval b
     | Eq  (a, b) -> eval a = eval b
     | Lt  (a, b) -> eval a < eval b
     | And (a, b) -> eval a && eval b
     | Not a      -> not (eval a)
     | If  (c, t, f) -> if eval c then eval t else eval f  *)

(* TODO 3: Pretty printer — also typed
   let rec pp : type a. a expr -> string = function
     | Int n      -> string_of_int n
     | Bool b     -> string_of_bool b
     | Add (a, b) -> Printf.sprintf "(%s + %s)" (pp a) (pp b)
     | ...  *)

(* TODO 4: Test that ill-typed expressions don't compile
   let _ = eval (Add (Int 1, Bool true))  (* TYPE ERROR: bool expr ≠ int expr *)
   let _ = eval (If (Int 1, Int 2, Int 3))  (* TYPE ERROR: int expr ≠ bool expr for condition *)  *)

(* TODO 5: Extend with Let binding (harder)
   type _ expr +=
     | Var : string -> 'a expr
     | Let : string * 'a expr * 'b expr -> 'b expr
   (* Requires an environment: (string * any) list — tricky to type-safely *)  *)

let () =
  (* Test after implementation: *)
  (* let expr = If (Eq (Add (Int 2, Int 3), Int 5), Bool true, Bool false) in
     Printf.printf "%s = %b\n" (pp expr) (eval expr)  *)
  print_endline "TODO: implement GADT DSL"
