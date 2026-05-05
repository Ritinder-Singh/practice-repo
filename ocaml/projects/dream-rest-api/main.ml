(* PROJECT: Dream REST API | requires: opam install dream ppx_deriving_yojson *)
(* Build: dune build && dune exec ./bin/main.exe *)

(* TODO 1: Define user type with yojson deriving
   type user = { id: int; name: string; email: string } [@@deriving yojson]
   let users : user list ref = ref [
     { id = 1; name = "Alice"; email = "alice@example.com" };
     { id = 2; name = "Bob"; email = "bob@example.com" };
   ]  *)

(* TODO 2: GET /users handler
   let get_users _req =
     let json = `List (List.map user_to_yojson !users) in
     Dream.json (Yojson.Safe.to_string json)  *)

(* TODO 3: GET /users/:id handler
   let get_user req =
     let id = int_of_string (Dream.param req "id") in
     match List.find_opt (fun u -> u.id = id) !users with
     | None   -> Dream.respond ~status:`Not_Found {|{"error":"User not found"}|}
     | Some u -> Dream.json (Yojson.Safe.to_string (user_to_yojson u))  *)

(* TODO 4: POST /users handler
   let create_user req =
     let%lwt body = Dream.body req in
     let data = Yojson.Safe.from_string body in
     (* validate and create user *)  *)

(* TODO 5: Main router setup
   let () = Dream.run ~port:3000 @@
     Dream.logger @@
     Dream.router [
       Dream.get  "/users"     get_users;
       Dream.get  "/users/:id" get_user;
       Dream.post "/users"     create_user;
     ]  *)

let () = print_endline "TODO: uncomment after installing Dream"
