-- =============================================================================
-- DBMS Foundations — SQL Basics
-- =============================================================================
-- Topics: DDL (CREATE, ALTER, DROP), DML (SELECT, INSERT, UPDATE, DELETE),
--         JOINs, WHERE, GROUP BY, HAVING, ORDER BY, subqueries, indexes.
-- Run: psql -d your_db -f basics.sql  (PostgreSQL)
--      sqlite3 practice.db < basics.sql  (SQLite)
-- Docs: https://www.postgresql.org/docs/current/tutorial.html
-- =============================================================================

-- -----------------------------------------------------------------------------
-- TODO 1: Create a Schema — E-Commerce Database
-- -----------------------------------------------------------------------------
-- Design and create tables for an e-commerce system:
--   users(id, email, name, created_at)
--   products(id, name, price, stock, category_id)
--   categories(id, name, parent_id)    -- self-referential for subcategories
--   orders(id, user_id, total, status, created_at)
--   order_items(id, order_id, product_id, quantity, unit_price)
--   addresses(id, user_id, street, city, country, is_default)
--
-- Apply: primary keys, foreign keys, NOT NULL, UNIQUE, CHECK constraints
-- Apply: DECIMAL(10,2) for prices, proper ENUM or VARCHAR for status

-- CREATE TABLE users (
--     id SERIAL PRIMARY KEY,
--     email VARCHAR(255) NOT NULL UNIQUE,
--     name VARCHAR(100) NOT NULL,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );
-- ... create remaining tables

-- -----------------------------------------------------------------------------
-- TODO 2: Insert Sample Data
-- -----------------------------------------------------------------------------
-- Insert at least:
--   5 categories (including 2 subcategories)
--   10 products across different categories
--   5 users
--   3 orders per user (15 total)
--   2-4 order items per order

-- INSERT INTO categories (name, parent_id) VALUES
-- ('Electronics', NULL),
-- ('Phones', 1),      -- subcategory of Electronics
-- ('Laptops', 1),
-- ('Clothing', NULL),
-- ('Shoes', 4);

-- -----------------------------------------------------------------------------
-- TODO 3: Basic SELECT Queries
-- -----------------------------------------------------------------------------
-- TODO 3a: Find all products in the 'Electronics' category (including subcategories)
-- TODO 3b: Find users who registered in the last 30 days
-- TODO 3c: Find all orders with status = 'completed' ordered by total DESC
-- TODO 3d: Find the most expensive product in each category

-- SELECT * FROM products WHERE price > 100 ORDER BY price DESC;

-- -----------------------------------------------------------------------------
-- TODO 4: JOINs
-- -----------------------------------------------------------------------------
-- TODO 4a: INNER JOIN — List all orders with user name and total
-- SELECT u.name, o.id, o.total, o.status
-- FROM orders o
-- INNER JOIN users u ON o.user_id = u.id;

-- TODO 4b: LEFT JOIN — List all users and their order count (include users with no orders)
-- SELECT u.name, COUNT(o.id) as order_count
-- FROM users u
-- LEFT JOIN orders o ON u.id = o.user_id
-- GROUP BY u.id, u.name;

-- TODO 4c: Multi-table JOIN — List order items with product names and order info
-- SELECT o.id as order_id, u.name as customer, p.name as product,
--        oi.quantity, oi.unit_price
-- FROM order_items oi
-- JOIN orders o ON oi.order_id = o.id
-- JOIN users u ON o.user_id = u.id
-- JOIN products p ON oi.product_id = p.id;

-- -----------------------------------------------------------------------------
-- TODO 5: Aggregations — GROUP BY, HAVING
-- -----------------------------------------------------------------------------
-- TODO 5a: Total revenue per category
-- SELECT c.name, SUM(oi.quantity * oi.unit_price) as revenue
-- FROM order_items oi
-- JOIN products p ON oi.product_id = p.id
-- JOIN categories c ON p.category_id = c.id
-- GROUP BY c.id, c.name
-- ORDER BY revenue DESC;

-- TODO 5b: Users who have spent more than $500 total
-- SELECT u.name, SUM(o.total) as total_spent
-- FROM users u
-- JOIN orders o ON u.id = o.user_id
-- GROUP BY u.id, u.name
-- HAVING SUM(o.total) > 500
-- ORDER BY total_spent DESC;

-- TODO 5c: Number of orders per status
-- SELECT status, COUNT(*) as count FROM orders GROUP BY status;

-- -----------------------------------------------------------------------------
-- TODO 6: Subqueries
-- -----------------------------------------------------------------------------
-- TODO 6a: Find products that have never been ordered
-- SELECT * FROM products
-- WHERE id NOT IN (SELECT DISTINCT product_id FROM order_items);

-- TODO 6b: Find the user with the highest single order value
-- SELECT * FROM users
-- WHERE id = (SELECT user_id FROM orders ORDER BY total DESC LIMIT 1);

-- TODO 6c: Find products priced above the average
-- SELECT * FROM products WHERE price > (SELECT AVG(price) FROM products);

-- -----------------------------------------------------------------------------
-- TODO 7: Indexes
-- -----------------------------------------------------------------------------
-- Create appropriate indexes for the queries above.
-- Think about: WHERE clause columns, JOIN columns, ORDER BY columns.

-- CREATE INDEX idx_orders_user_id ON orders(user_id);
-- CREATE INDEX idx_orders_status ON orders(status);
-- CREATE INDEX idx_order_items_order_id ON order_items(order_id);
-- CREATE INDEX idx_order_items_product_id ON order_items(product_id);
-- CREATE INDEX idx_products_category_id ON products(category_id);
-- CREATE UNIQUE INDEX idx_users_email ON users(email);

-- -----------------------------------------------------------------------------
-- TODO 8: UPDATE and DELETE
-- -----------------------------------------------------------------------------
-- TODO 8a: Apply a 10% discount to all products in 'Clothing' category
-- UPDATE products
-- SET price = price * 0.9
-- WHERE category_id = (SELECT id FROM categories WHERE name = 'Clothing');

-- TODO 8b: Mark all orders older than 1 year as 'archived'
-- UPDATE orders SET status = 'archived'
-- WHERE created_at < NOW() - INTERVAL '1 year';

-- TODO 8c: Delete users who have never placed an order (CAUTION: use WHERE)
-- DELETE FROM users
-- WHERE id NOT IN (SELECT DISTINCT user_id FROM orders);
