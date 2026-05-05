(* TOPIC: Concurrency & Domains | ocaml 07_async.ml *)
(* OCaml 5 introduced Domains for true parallelism (no GIL equivalent) *)
(* For async I/O: Lwt or Eio are the standard libraries *)

(* TODO 1: Domains — OCaml 5 parallel execution *)
(*   let domain = Domain.spawn (fun () ->
       Printf.printf "Hello from domain %d\n" (Domain.self () :> int);
       42)  (* returns value *)
     let result = Domain.join domain
     Printf.printf "Domain returned: %d\n" result  *)

(* TODO 2: Mutex for safe shared state across domains *)
(*   let mutex = Mutex.create ()
     let counter = ref 0
     let increment () =
       Mutex.lock mutex;
       counter := !counter + 1;
       Mutex.unlock mutex
     let domains = Array.init 4 (fun _ -> Domain.spawn (fun () ->
       for _ = 1 to 1000 do increment () done))
     Array.iter Domain.join domains;
     Printf.printf "Counter: %d\n" !counter  (* should be 4000 *)  *)

(* TODO 3: Atomic operations (OCaml 5) *)
(*   let counter = Atomic.make 0
     let domains = Array.init 4 (fun _ -> Domain.spawn (fun () ->
       for _ = 1 to 1000 do
         ignore (Atomic.fetch_and_add counter 1)
       done))
     Array.iter Domain.join domains;
     Printf.printf "Atomic counter: %d\n" (Atomic.get counter)  *)

(* TODO 4: Semaphore — limit concurrent domains *)
(*   let sem = Semaphore.Counting.make 3  (* allow 3 concurrent *)
     let work i =
       Semaphore.Counting.acquire sem;
       Printf.printf "Worker %d running\n" i;
       Unix.sleepf 0.1;
       Semaphore.Counting.release sem
     let ds = Array.init 10 (fun i -> Domain.spawn (fun () -> work i))
     Array.iter Domain.join ds  *)

(* TODO 5: Lwt — cooperative async I/O (install: opam install lwt lwt_unix) *)
(*   (* open Lwt.Infix *)
     let fetch_data () =
       Lwt.bind (Lwt_unix.sleep 1.0) (fun () -> Lwt.return "data fetched")
     let main () =
       let* result = fetch_data () in
       Lwt_io.printlf "Got: %s" result
     let () = Lwt_main.run (main ())  *)

(* TODO 6: Lwt concurrent tasks *)
(*   let task1 = Lwt_unix.sleep 1.0 >>= fun () -> Lwt.return "task1"
     let task2 = Lwt_unix.sleep 0.5 >>= fun () -> Lwt.return "task2"
     let both = Lwt.both task1 task2  (* runs concurrently *)
     let () = Lwt_main.run (Lwt.map (fun (r1, r2) -> Printf.printf "%s %s\n" r1 r2) both)  *)

(* TODO 7: Eio — newer structured concurrency library (OCaml 5+) *)
(*   (* opam install eio_main *)
     open Eio.Std
     let () = Eio_main.run @@ fun env ->
       Switch.run (fun sw ->
         let t1 = Fiber.fork_promise ~sw (fun () -> Eio.Time.sleep env#clock 1.0; "task1") in
         let t2 = Fiber.fork_promise ~sw (fun () -> Eio.Time.sleep env#clock 0.5; "task2") in
         Printf.printf "%s %s\n" (Promise.await t1) (Promise.await t2))  *)

(* TODO 8: Effect handlers (OCaml 5) — basis for Eio's concurrency model *)
(*   type _ Effect.t += Yield : unit Effect.t
     let generator () =
       for i = 1 to 5 do
         Effect.perform Yield;
         Printf.printf "Generated %d\n" i
       done
     (* Effect.Deep.match_with generator () { ... }  *)  *)

let () = print_endline "TODO: implement concurrency exercises (requires OCaml 5)"
