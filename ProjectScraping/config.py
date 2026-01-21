# ===== KONFIGURASI UTAMA =====

TOKEN_BEARER = "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjU3MDc0NjI3LTg4MWItNDQzZC04OTcyLTdmMmMzOTNlMzYyOSIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7InVzZSI6Ind1dDYxMiIsImVtYSI6ImFrdW5iaXNuaXNzdGV2ZW5AZ21haWwuY29tIiwiZnVsIjoiV3V0Iiwic2VzIjoiSVc4Qlg5bTVQOHEzY29WcCIsImR2YyI6IjYwNWNmYTQ3YzM2OTAxYzI3MjcxNTNlNWQyMjI1MzQ1IiwidWlkIjo1ODg1ODcxLCJjb3UiOiJTRyJ9LCJleHAiOjE3NjkwMDc1MjYsImlhdCI6MTc2ODkyMTEyNiwiaXNzIjoiU1RPQ0tCSVQiLCJqdGkiOiI5ZTdlOTA2ZC1lZmQyLTQxYzQtOTQ5MC1iNzFjMmRhYjYxN2MiLCJuYmYiOjE3Njg5MjExMjYsInZlciI6InYxIn0.AEP7JbKXqR4QLct1bYpIAaJPSir2oNCFskmriE83o7jkzD4-W096gBiChwhKzhTI9yWAVcPqPKhBU9QkKKwsfIqOyJLyVzRQJfwG1HhAhZxaa9PtL85KMtYoNKSejLZYcJeSeakvx4QN6lMAylUqdiu7xVEwtYVbIEVeDDckve7T1rQmY2tnCidwIhQBEPYWZjcqHvr622QTbLBiVBGr_GxSpuJs-C38_4dx1aEOxu5f0Usk66l5459UacJSYmExFH4GCEfHvnguGHiS85KU8KGnCvN1StDRv44Xa8pBpAiJB1bIAtuMOtJJIA9gNscUZq2ahpSrmIY52-oh3RONkw"

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
