# ===== KONFIGURASI UTAMA =====

TOKEN_BEARER = "Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IjU3MDc0NjI3LTg4MWItNDQzZC04OTcyLTdmMmMzOTNlMzYyOSIsInR5cCI6IkpXVCJ9.eyJkYXRhIjp7InVzZSI6Ind1dDYxMiIsImVtYSI6ImFrdW5iaXNuaXNzdGV2ZW5AZ21haWwuY29tIiwiZnVsIjoiV3V0Iiwic2VzIjoiMGozdk4zTzFQT0lVMnBFdSIsImR2YyI6IjYwNWNmYTQ3YzM2OTAxYzI3MjcxNTNlNWQyMjI1MzQ1IiwidWlkIjo1ODg1ODcxLCJjb3UiOiJJRCJ9LCJleHAiOjE3NjcwNjAxMDksImlhdCI6MTc2Njk3MzcwOSwiaXNzIjoiU1RPQ0tCSVQiLCJqdGkiOiJjZWFkNmYzZC04YzE5LTRmNzYtOTUzZS1hNmY0ZGE0MWFiZDMiLCJuYmYiOjE3NjY5NzM3MDksInZlciI6InYxIn0.Q3WtXwS3BQJjvz6G98gSBbN8qRR2Gqtzb9PZNqlmTmotzZkv_5nkOq6I2_sUa_Mq3Pc2ZM5PiUREGihyQNsYfBdCgENP1xtM7EXIR9331xk5Vc-1LrKsimlPdxJiTy2c6K35cfuV1kd7JgARnErMb0hnteGAYkuyerNh0hh9vgilti7XxSO9ei7LJJYQxbfIvw-M0G3p-XoxPeJQ738Sc9clOFmzhrOSFTLhpmdsgEzKGwAHmbIhybKfMUH4ITBbyiXB-4wKFjgS-psAedyDJyyMD-mPvSX6aPIFBlQ1WcnKLOgM0oGfRmg_Bl8ad6a2dCGvDrrsCGTfeFeMksxFLQ"

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
