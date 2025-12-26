# ===== KONFIGURASI UTAMA =====

TOKEN_BEARER = "Bearer PASTE_TOKEN_VALID_DISINI"

API_ORDERBOOK = "https://exodus.stockbit.com/company-price-feed/v2/orderbook/companies/{code}"

# Rate limit (AMAN & REALISTIS)
REQ_PER_SEC = 6
MAX_WORKERS = 8

# HTTP
HTTP_TIMEOUT = 10

# DB MySQL
DB_CONFIG = {
    "user": "root",
    "password": "",
    "host": "localhost",
    "database": "stock_db",
}
