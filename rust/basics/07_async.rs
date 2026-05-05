// =============================================================================
// Rust — Async/Await with Tokio
// =============================================================================
// NOTE: This file requires Cargo. Create a project:
//   cargo new async_practice && cd async_practice
//   Add to Cargo.toml: tokio = { version = "1", features = ["full"] }
//   Copy this code into src/main.rs
//
// Topics: async fn, .await, tokio::spawn, tokio::join!, tokio::select!,
//         tokio::time, channels (mpsc, oneshot), tokio::sync::Mutex.
// Docs: https://tokio.rs/tokio/tutorial
// =============================================================================

// TODO 1: Basic async function
//   async fn fetch_data(url: &str) -> String {
//       tokio::time::sleep(Duration::from_millis(100)).await;
//       format!("data from {url}")
//   }
//   #[tokio::main] async fn main() { let result = fetch_data("url").await; }

// TODO 2: tokio::spawn — concurrent tasks
//   let h1 = tokio::spawn(async { fetch_data("url1").await });
//   let h2 = tokio::spawn(async { fetch_data("url2").await });
//   let (r1, r2) = tokio::join!(h1, h2);   // wait for both

// TODO 3: tokio::select! — first wins / timeout
//   tokio::select! {
//       result = fetch_data("url") => println!("got: {result}"),
//       _ = tokio::time::sleep(Duration::from_secs(2)) => println!("timeout!"),
//   }

// TODO 4: tokio::sync::mpsc — async channels
//   let (tx, mut rx) = tokio::sync::mpsc::channel(32);
//   tokio::spawn(async move { tx.send("hello").await.unwrap() });
//   let msg = rx.recv().await;

// TODO 5: Shared state with tokio::sync::Mutex
//   let counter = Arc::new(tokio::sync::Mutex::new(0u64));
//   let c = counter.clone();
//   tokio::spawn(async move { let mut lock = c.lock().await; *lock += 1; });

// TODO 6: axum hello world (requires axum crate)
//   use axum::{routing::get, Router};
//   async fn handler() -> &'static str { "Hello from axum!" }
//   let app = Router::new().route("/", get(handler));
//   axum::Server::bind(&"0.0.0.0:3000".parse().unwrap()).serve(app.into_make_service()).await

fn main() { println!("Rust async — see Cargo.toml note above, copy to src/main.rs"); }
