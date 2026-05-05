(* PROJECT: JSON Parser using Pattern Matching | ocaml json_parser.ml *)

(* TODO 1: Define JSON algebraic data type *)
(*   type json =
       | JNull
       | JBool of bool
       | JNumber of float
       | JString of string
       | JArray of json list
       | JObject of (string * json) list  *)

(* TODO 2: Tokenizer *)
(*   type token =
       | TNull | TTrue | TFalse
       | TNumber of float | TString of string
       | TLBrace | TRBrace | TLBracket | TRBracket
       | TColon | TComma | TEOF
   let tokenize (s: string) : token list =
     (* Use String.index_opt, Scanf.sscanf, or manual character scanning *)  *)

(* TODO 3: Parser — recursive descent *)
(*   let parse_value tokens = (* return (json, remaining_tokens) *)
     let parse_array  tokens = (* parse comma-separated values until ] *)
     let parse_object tokens = (* parse "key": value pairs until } *)
   Each returns (json * token list)  *)

(* TODO 4: Pretty printer *)
(*   let rec pretty_print ?(indent=0) = function
       | JNull         -> "null"
       | JBool true    -> "true"
       | JBool false   -> "false"
       | JNumber n     -> string_of_float n
       | JString s     -> Printf.sprintf "\"%s\"" (String.escaped s)
       | JArray []     -> "[]"
       | JArray items  ->
           let pad = String.make (indent + 2) ' ' in
           let items_str = List.map (fun item -> pad ^ pretty_print ~indent:(indent+2) item) items in
           "[\n" ^ String.concat ",\n" items_str ^ "\n" ^ String.make indent ' ' ^ "]"
       | JObject []    -> "{}"
       | JObject pairs ->
           (* similar to array but "key": value format *)
           ""  *)

(* TODO 5: Test with complex JSON
   let test_json = {|{"name":"Alice","scores":[95,87,92],"active":true,"address":null}|}
   (* parse test_json |> pretty_print |> print_endline  *)  *)

let () = print_endline "TODO: implement JSON parser"
