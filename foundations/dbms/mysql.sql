-- =============================================================================
-- MySQL — Specifics Beyond Generic SQL
-- =============================================================================
-- Topics: MySQL-specific syntax, engines, indexes, JSON columns,
--         full-text search, replication concepts, performance tuning.
-- Run: mysql -u root -p < mysql.sql
-- Ref: Resume — MySQL (Databases)
-- =============================================================================


-- =============================================================================
-- 1. STORAGE ENGINES
-- =============================================================================

-- InnoDB (default) — ACID, foreign keys, row-level locking
CREATE TABLE orders (
    id          BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id     BIGINT UNSIGNED NOT NULL,
    total       DECIMAL(10, 2) NOT NULL,
    status      ENUM('pending', 'paid', 'shipped', 'cancelled') DEFAULT 'pending',
    created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at  DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_user_id (user_id),
    INDEX idx_status_created (status, created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- MyISAM — no transactions, table-level lock, faster full-text search (legacy)
-- MEMORY — data in RAM, lost on restart, used for temp tables


-- =============================================================================
-- 2. MYSQL-SPECIFIC DATA TYPES
-- =============================================================================

CREATE TABLE users (
    id          BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,

    -- String types
    username    VARCHAR(50) NOT NULL UNIQUE,        -- variable length, max 50
    bio         TEXT,                               -- up to 65KB
    notes       MEDIUMTEXT,                         -- up to 16MB
    avatar_blob MEDIUMBLOB,                         -- binary up to 16MB

    -- Numeric
    score       TINYINT UNSIGNED,                   -- 0-255
    balance     DECIMAL(12, 4),                     -- exact, good for money

    -- Date/time — MySQL has no TIMESTAMPTZ (no timezone awareness)
    created_at  DATETIME(6) DEFAULT CURRENT_TIMESTAMP(6),  -- microsecond precision
    birth_date  DATE,

    -- JSON (MySQL 5.7.8+)
    metadata    JSON,

    -- Flags
    is_active   TINYINT(1) DEFAULT 1,               -- MySQL bool convention
    role        ENUM('user', 'admin', 'moderator') DEFAULT 'user'

) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- =============================================================================
-- 3. JSON COLUMN OPERATIONS (MySQL 5.7+)
-- =============================================================================

INSERT INTO users (username, metadata) VALUES
  ('ritinder', '{"skills": ["Python", "Go"], "level": "senior", "tags": ["backend"]}');

-- Extract value
SELECT JSON_EXTRACT(metadata, '$.level') AS level FROM users;
SELECT metadata->>'$.level' AS level FROM users;          -- shorthand (MySQL 5.7.13+)

-- Modify JSON
UPDATE users
SET metadata = JSON_SET(metadata, '$.level', 'staff', '$.location', 'India')
WHERE username = 'ritinder';

-- Query on JSON field (use generated column + index for performance)
ALTER TABLE users
  ADD COLUMN skill_count INT AS (JSON_LENGTH(metadata->'$.skills')) STORED,
  ADD INDEX idx_skill_count (skill_count);

-- JSON_CONTAINS, JSON_OVERLAPS (MySQL 8.0+)
SELECT * FROM users WHERE JSON_CONTAINS(metadata->'$.skills', '"Python"');


-- =============================================================================
-- 4. FULL-TEXT SEARCH
-- =============================================================================

CREATE TABLE articles (
    id      INT AUTO_INCREMENT PRIMARY KEY,
    title   VARCHAR(255),
    body    TEXT,
    FULLTEXT INDEX ft_content (title, body)
) ENGINE=InnoDB;

-- Natural language mode (relevance ranked)
SELECT title, MATCH(title, body) AGAINST ('machine learning AI' IN NATURAL LANGUAGE MODE) AS score
FROM articles
WHERE MATCH(title, body) AGAINST ('machine learning AI' IN NATURAL LANGUAGE MODE)
ORDER BY score DESC;

-- Boolean mode (+ required, - exclude, * wildcard)
SELECT title FROM articles
WHERE MATCH(title, body) AGAINST ('+Python -JavaScript learn*' IN BOOLEAN MODE);


-- =============================================================================
-- 5. INDEXES — MYSQL-SPECIFIC
-- =============================================================================

-- Composite index — order matters: most selective OR most filtered first
CREATE INDEX idx_status_user_created ON orders (status, user_id, created_at);
-- Good for: WHERE status = 'paid' AND user_id = 42 ORDER BY created_at

-- Covering index — query resolved from index alone (no table lookup)
CREATE INDEX idx_covering ON orders (user_id, status, total);
-- SELECT status, total FROM orders WHERE user_id = 42  ← uses only the index

-- Prefix index (for long strings)
CREATE INDEX idx_email_prefix ON users (username(10));

-- EXPLAIN to verify index usage
EXPLAIN SELECT * FROM orders WHERE status = 'paid' AND user_id = 42;
-- Look for: type=ref (good), key= (which index used), Extra=Using index (covering)


-- =============================================================================
-- 6. PERFORMANCE PATTERNS
-- =============================================================================

-- LIMIT with large offsets is slow — use keyset pagination instead
-- BAD:
SELECT * FROM orders ORDER BY id LIMIT 10 OFFSET 100000;

-- GOOD (keyset/cursor pagination):
SELECT * FROM orders WHERE id > 100000 ORDER BY id LIMIT 10;

-- INSERT IGNORE — skip on duplicate key (no error)
INSERT IGNORE INTO users (username) VALUES ('ritinder');

-- ON DUPLICATE KEY UPDATE — upsert
INSERT INTO users (username, score) VALUES ('ritinder', 100)
ON DUPLICATE KEY UPDATE score = score + 100;

-- REPLACE INTO — delete + reinsert (slower, avoid for tables with FKs)
-- REPLACE INTO users (id, username) VALUES (1, 'ritinder');

-- Batch inserts — much faster than individual INSERTs
INSERT INTO orders (user_id, total, status) VALUES
  (1, 99.99, 'pending'),
  (2, 149.99, 'paid'),
  (3, 49.99, 'pending');


-- =============================================================================
-- 7. TRANSACTIONS
-- =============================================================================

START TRANSACTION;

UPDATE users SET balance = balance - 100 WHERE id = 1;
UPDATE users SET balance = balance + 100 WHERE id = 2;

-- Check invariant before committing
SELECT balance FROM users WHERE id = 1;
-- If balance < 0: ROLLBACK;

COMMIT;

-- Savepoints for nested logic
START TRANSACTION;
SAVEPOINT before_risky_op;
-- ... risky statements ...
ROLLBACK TO before_risky_op;  -- partial rollback
COMMIT;


-- =============================================================================
-- 8. USEFUL MYSQL-SPECIFIC FUNCTIONS
-- =============================================================================

SELECT
  NOW(),                              -- current datetime
  CURDATE(),                          -- current date
  UNIX_TIMESTAMP(),                   -- epoch seconds
  FROM_UNIXTIME(1700000000),          -- epoch → datetime
  DATE_FORMAT(NOW(), '%Y-%m-%d'),     -- format
  DATEDIFF(NOW(), '2025-01-01'),      -- days between
  TIMESTAMPDIFF(HOUR, created_at, NOW()) AS hours_old FROM users LIMIT 1;

-- String functions
SELECT
  CONCAT_WS(' ', 'Ritinder', 'Singh'),  -- join with separator
  GROUP_CONCAT(username ORDER BY id SEPARATOR ', ') FROM users;  -- aggregate to string

-- Window functions (MySQL 8.0+)
SELECT
  username,
  score,
  RANK() OVER (ORDER BY score DESC) AS rank,
  LAG(score) OVER (ORDER BY score DESC) AS prev_score
FROM users;


-- =============================================================================
-- 9. REPLICATION CONCEPTS (interview knowledge)
-- =============================================================================
-- Primary-Replica (master-slave): writes go to primary, replicated async to replicas
-- Read replicas: route SELECT queries to replicas to scale reads
-- GTID replication: Global Transaction IDs — easier failover than binary log positions
-- Semi-sync replication: at least one replica must ACK before primary commits (durability)
-- Binlog formats: ROW (exact changes), STATEMENT (SQL), MIXED


-- =============================================================================
-- 10. SHOW & DEBUG COMMANDS
-- =============================================================================

-- SHOW PROCESSLIST;          -- running queries
-- SHOW ENGINE INNODB STATUS; -- lock waits, deadlocks
-- SHOW INDEX FROM orders;    -- index details
-- SHOW VARIABLES LIKE 'innodb_buffer_pool_size';
-- SELECT * FROM information_schema.INNODB_TRX;  -- active transactions
-- ANALYZE TABLE orders;      -- update optimizer statistics
-- OPTIMIZE TABLE orders;     -- reclaim space after many deletes
