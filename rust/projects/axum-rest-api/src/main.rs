// =============================================================================
// Axum REST API — Entry Point
// =============================================================================
// TODO: implement routes, handlers, database pool setup
// See README.md for full requirements.
// =============================================================================

// use axum::{routing::{get, post, put, delete}, Router, Extension};
// use sqlx::PgPool;
// use std::net::SocketAddr;

// #[tokio::main]
// async fn main() {
//     dotenv::dotenv().ok();
//     let db_url = std::env::var("DATABASE_URL").expect("DATABASE_URL required");
//     let pool = PgPool::connect(&db_url).await.expect("DB connect failed");
//
//     let app = Router::new()
//         .route("/products", get(list_products).post(create_product))
//         .route("/products/:id", get(get_product).put(update_product).delete(delete_product))
//         .layer(Extension(pool));
//
//     let addr = SocketAddr::from(([0, 0, 0, 0], 3000));
//     println!("Listening on {addr}");
//     axum::Server::bind(&addr).serve(app.into_make_service()).await.unwrap();
// }

fn main() { println!("Copy to a Cargo project — see README.md"); }
