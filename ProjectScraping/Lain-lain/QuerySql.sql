-- 1. Buat Databasenya dulu
CREATE DATABASE IF NOT EXISTS stock_db;

-- 2. Masuk ke database tersebut
USE stock_db;

-- 3. Buat Tabel untuk menyimpan data Orderbook
DROP TABLE IF EXISTS orderbook_history;

CREATE TABLE orderbook_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    TIMESTAMP DATETIME NOT NULL,
    stock_code VARCHAR(10) NOT NULL,
    TYPE VARCHAR(5) NOT NULL, -- 'BID' atau 'ASK'
    urutan INT NOT NULL,      -- INI BARU: Penanda antrian ke-1, ke-2, dst
    price INT NOT NULL,
    lot INT NOT NULL
);


CREATE TABLE scrape_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    TIMESTAMP DATETIME,
    stock_code VARCHAR(10),
    STATUS VARCHAR(20),
    message VARCHAR(255)
);
