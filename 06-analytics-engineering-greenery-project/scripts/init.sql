CREATE TABLE IF NOT EXISTS address (
    address_id TEXT PRIMARY KEY,
    address TEXT,
    zipcode INT,
    state TEXT,
    country TEXT
);

COPY address FROM '06-analytics-engineering/greenery/data/data/addresses.csv' DELIMITER ',' CSV HEADER;

-- CREATE TABLE IF NOT EXISTS events (
--     event_id TEXT PRIMARY KEY,
--     session_id TEXT,
--     user_id INT,
--     page_url TEXT,
--     created_at TEXT,
--     event_type TEXT,
--     order_id TEXT,
--     product_id TEXT
-- );
