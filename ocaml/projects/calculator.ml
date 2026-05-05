(* PROJECT: OCaml Calculator | ocaml calculator.ml *)

(* TODO 1 (Mini): REPL with simple expression parsing
   let rec repl () =
     print_string ">> ";
     match input_line stdin with
     | exception End_of_file -> ()
     | "exit" -> ()
     | line ->
       (try
         let tokens = String.split_on_char ' ' (String.trim line) in
         match tokens with
         | [a; op; b] ->
           let a = float_of_string a and b = float_of_string b in
           let result = match op with
             | "+" -> a +. b | "-" -> a -. b
             | "*" -> a *. b | "/" -> if b = 0.0 then raise Division_by_zero else a /. b
             | _ -> failwith ("Unknown op: " ^ op)
           in Printf.printf "%g\n" result
         | _ -> print_endline "Usage: a op b"
       with exn -> Printf.printf "Error: %s\n" (Printexc.to_string exn));
       repl ()  *)

(* TODO 2 (Intermediate): Recursive descent parser with ADT
   type expr =
     | Num of float
     | Add of expr * expr
     | Sub of expr * expr
     | Mul of expr * expr
     | Div of expr * expr
     | Neg of expr

   (* Tokenizer: string -> string list *)
   (* parse_expr, parse_term, parse_factor *)
   (* eval: expr -> float *)  *)

(* TODO 3 (Advanced): Variables via Hashtbl
   let vars : (string, float) Hashtbl.t = Hashtbl.create 16
   (* Parse "let x = 5 + 3" → Hashtbl.replace vars "x" (eval expr) *)
   (* Reference variable: look up in vars table *)  *)

let () =
  print_endline "TODO: implement OCaml calculator";
  (* Uncomment: repl () *)
