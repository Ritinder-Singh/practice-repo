-- =============================================================================
-- DBMS Foundations — Advanced SQL (PostgreSQL)
-- =============================================================================
-- Topics: CTEs, recursive CTEs, window functions (ROW_NUMBER, RANK, LAG, LEAD,
--         running totals), EXPLAIN ANALYZE, JSONB, transactions, partitioning.
-- Run: psql -d your_db -f advanced.sql
-- Ref: pgexercises.com | https://use-the-index-luke.com
-- Prerequisites: run basics.sql first (creates e-commerce schema).
-- =============================================================================

-- =============================================================================
-- SECTION 1 — Common Table Expressions (CTEs)
-- =============================================================================

-- TODO 1a: Simple CTE — top customers by total spend
-- WITH customer_spending AS (
--     SELECT u.id, u.name, SUM(o.total) AS total_spent
--     FROM users u JOIN orders o ON u.id = o.user_id
--     GROUP BY u.id, u.name
-- )
-- SELECT * FROM customer_spending WHERE total_spent > 1000 ORDER BY total_spent DESC;

-- TODO 1b: Recursive CTE — category hierarchy (unlimited depth)
-- WITH RECURSIVE category_tree AS (
--     SELECT id, name, parent_id, 0 AS depth
--     FROM categories WHERE parent_id IS NULL       -- base case: root categories
--     UNION ALL
--     SELECT c.id, c.name, c.parent_id, ct.depth + 1
--     FROM categories c JOIN category_tree ct ON c.parent_id = ct.id  -- recursive
-- )
-- SELECT repeat('  ', depth) || name AS indented_name, depth FROM category_tree ORDER BY depth, name;

-- TODO 1c: CTE chain — monthly revenue with month-over-month growth
-- WITH monthly AS (
--     SELECT DATE_TRUNC('month', created_at) AS month, SUM(total) AS revenue
--     FROM orders WHERE status != 'cancelled'
--     GROUP BY 1
-- ),
-- with_lag AS (
--     SELECT month, revenue, LAG(revenue) OVER (ORDER BY month) AS prev_revenue
--     FROM monthly
-- )
-- SELECT month, revenue,
--        ROUND(((revenue - prev_revenue) / NULLIF(prev_revenue,0) * 100)::numeric, 2) AS growth_pct
-- FROM with_lag ORDER BY month;

-- =============================================================================
-- SECTION 2 — Window Functions
-- =============================================================================

-- TODO 2a: ROW_NUMBER — rank products by price within each category
-- SELECT name, category_id, price,
--        ROW_NUMBER() OVER (PARTITION BY category_id ORDER BY price DESC) AS rank_in_cat
-- FROM products;

-- TODO 2b: RANK vs DENSE_RANK — demonstrate difference on tied prices
-- SELECT name, price,
--        RANK()       OVER (ORDER BY price DESC) AS rank,
--        DENSE_RANK() OVER (ORDER BY price DESC) AS dense_rank
-- FROM products;

-- TODO 2c: LAG / LEAD — compare each order to previous/next for same user
-- SELECT u.name, o.id, o.total, o.created_at,
--        LAG(o.total)  OVER (PARTITION BY o.user_id ORDER BY o.created_at) AS prev_total,
--        LEAD(o.total) OVER (PARTITION BY o.user_id ORDER BY o.created_at) AS next_total
-- FROM orders o JOIN users u ON o.user_id = u.id;

-- TODO 2d: SUM OVER — running total per user
-- SELECT u.name, o.created_at::date, o.total,
--        SUM(o.total) OVER (PARTITION BY o.user_id ORDER BY o.created_at) AS running_total
-- FROM orders o JOIN users u ON o.user_id = u.id;

-- TODO 2e: NTILE — split customers into 4 quartiles by spend
-- WITH spend AS (SELECT user_id, SUM(total) AS total FROM orders GROUP BY user_id)
-- SELECT user_id, total, NTILE(4) OVER (ORDER BY total DESC) AS quartile FROM spend;

-- =============================================================================
-- SECTION 3 — EXPLAIN ANALYZE
-- =============================================================================

-- TODO 3: Compare query plans before and after adding an index.
--   Step 1: run EXPLAIN ANALYZE on a JOIN query
--   Step 2: create index on the join column
--   Step 3: run again, compare actual time and plan type (Seq Scan vs Index Scan)
--
-- EXPLAIN ANALYZE
-- SELECT u.name, COUNT(o.id) FROM users u LEFT JOIN orders o ON u.id = o.user_id GROUP BY u.id;
--
-- CREATE INDEX IF NOT EXISTS idx_orders_user_id ON orders(user_id);
--
-- EXPLAIN ANALYZE  -- run again after index
-- SELECT u.name, COUNT(o.id) FROM users u LEFT JOIN orders o ON u.id = o.user_id GROUP BY u.id;

-- =============================================================================
-- SECTION 4 — JSONB (PostgreSQL only)
-- =============================================================================

-- TODO 4a: Add JSONB column and query operators
-- ALTER TABLE products ADD COLUMN IF NOT EXISTS metadata JSONB DEFAULT '{}';
--
-- UPDATE products SET metadata = '{"brand":"Apple","specs":{"ram":"16GB","storage":"512GB"}}'
-- WHERE name ILIKE '%macbook%';
--
-- -- Operators: -> (returns JSON), ->> (returns text), @> (contains), ? (key exists)
-- SELECT name, metadata->>'brand' AS brand FROM products WHERE metadata @> '{"brand":"Apple"}';
-- SELECT name FROM products WHERE metadata ? 'specs';
--
-- -- GIN index for JSONB performance
-- CREATE INDEX IF NOT EXISTS idx_products_metadata ON products USING GIN(metadata);

-- =============================================================================
-- SECTION 5 — Transactions & Isolation
-- =============================================================================

-- TODO 5a: Multi-step transaction (order placement)
-- BEGIN;
--   -- 1. Create order
--   INSERT INTO orders (user_id, total, status) VALUES (1, 99.99, 'pending') RETURNING id;
--   -- 2. Deduct stock (use id from above)
--   UPDATE products SET stock = stock - 1 WHERE id = 1 AND stock > 0;
--   -- If UPDATE affects 0 rows (out of stock): ROLLBACK; else COMMIT
-- COMMIT;

-- TODO 5b: SAVEPOINT for partial rollback
-- BEGIN;
--   SAVEPOINT before_items;
--   INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (1, 1, 2, 29.99);
--   -- Simulate error: bad product_id
--   INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (1, 99999, 1, 9.99);
-- ROLLBACK TO before_items;  -- undo only the failed inserts
-- COMMIT;                     -- commit rest of transaction

-- TODO 5c: Demonstrate READ COMMITTED vs REPEATABLE READ isolation
-- Session 1: BEGIN; SELECT balance FROM accounts WHERE id=1;  -- sees 100
-- Session 2: UPDATE accounts SET balance=200 WHERE id=1; COMMIT;
-- Session 1 (READ COMMITTED):   SELECT again → sees 200 (non-repeatable read)
-- Session 1 (REPEATABLE READ):  SELECT again → still sees 100 (protected)
-- SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;

-- =============================================================================
-- SECTION 6 — Full-Text Search (PostgreSQL tsvector)
-- =============================================================================

-- TODO 6: Build a full-text search on products name+description
-- ALTER TABLE products ADD COLUMN IF NOT EXISTS search_vector tsvector;
-- UPDATE products SET search_vector = to_tsvector('english', name || ' ' || COALESCE(description,''));
-- CREATE INDEX IF NOT EXISTS idx_products_fts ON products USING GIN(search_vector);
--
-- -- Search query
-- SELECT name FROM products
-- WHERE search_vector @@ plainto_tsquery('english', 'wireless headphones');
--
-- -- Ranked results
-- SELECT name, ts_rank(search_vector, query) AS rank
-- FROM products, plainto_tsquery('english', 'laptop computer') query
-- WHERE search_vector @@ query
-- ORDER BY rank DESC;
