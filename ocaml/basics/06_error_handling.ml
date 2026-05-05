(* TOPIC: Error Handling | ocaml 06_error_handling.ml *)

(* TODO 1: Exceptions — define and raise *)
(*   exception Not_found_custom of string
     exception Database_error of { code: int; message: string }
     let find_user id =
       if id <= 0 then raise (Not_found_custom (Printf.sprintf "Invalid id: %d" id))
       else if id > 100 then raise Not_found
       else { name = "User"; id }  *)

(* TODO 2: try...with — catch exceptions *)
(*   let safe_divide a b =
       try a / b
       with Division_by_zero -> 0
     let result =
       try find_user (-1)
       with
       | Not_found_custom msg -> Printf.printf "Custom: %s\n" msg; default_user
       | Not_found -> Printf.printf "Standard not found\n"; default_user
       | exn -> Printf.printf "Unknown: %s\n" (Printexc.to_string exn); raise exn  *)

(* TODO 3: Result type — explicit error without exceptions *)
(*   type ('ok, 'err) result = Ok of 'ok | Error of 'err
     (* OCaml stdlib has this built in as Result.t *)
     let safe_div a b : (int, string) result =
       if b = 0 then Error "Division by zero"
       else Ok (a / b)
     let (>>=) r f = match r with Error e -> Error e | Ok v -> f v
     safe_div 10 2 >>= fun x -> safe_div x 3  *)

(* TODO 4: Option for simple missing values *)
(*   let safe_head = function [] -> None | x :: _ -> Some x
     let find_in_list pred lst = List.find_opt pred lst
     let result = safe_head [1;2;3]
                  |> Option.map (fun x -> x * 2)
                  |> Option.value ~default:0  *)

(* TODO 5: Printing exceptions *)
(*   try failwith "something went wrong"
     with exn ->
       Printf.printf "Exception: %s\n" (Printexc.to_string exn);
       Printexc.print_backtrace stdout  (* requires OCAMLRUNPARAM=b *)  *)

(* TODO 6: Domains and exceptions (OCaml 5+) *)
(*   (* Exceptions in a Domain don't propagate to parent automatically *)
     let d = Domain.spawn (fun () ->
       try failwith "domain error"
       with exn -> Printf.printf "Caught in domain: %s\n" (Printexc.to_string exn))
     in Domain.join d  *)

(* TODO 7: Fun.protect — ensure cleanup even with exceptions *)
(*   Fun.protect
       ~finally:(fun () -> Printf.printf "Cleanup\n")
       (fun () ->
         Printf.printf "Working\n";
         failwith "oops")  (* finally runs even when exception occurs *)  *)

(* TODO 8: Error handling best practices in OCaml *)
(*   (* 1. Use Option/Result for expected failures (file not found, parse error) *)
     (* 2. Use exceptions for truly exceptional cases (programming errors, Out_of_memory) *)
     (* 3. Prefer Result.t for library APIs — forces callers to handle errors *)
     (* 4. Use let* (monadic bind) with Result for chaining: *)
     (*    let ( let* ) = Result.bind
          let compute () =
            let* x = safe_div 10 5 in
            let* y = safe_div 20 4 in
            Ok (x + y)  *)  *)

let () = print_endline "TODO: implement error handling exercises"
