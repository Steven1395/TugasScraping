import requests
from datetime import datetime
from config import API_ORDERBOOK, TOKEN_BEARER, HTTP_TIMEOUT
from db import insert_orderbook

HEADERS = {
    "accept": "application/json",
    "authorization": TOKEN_BEARER,
    "user-agent": "Mozilla/5.0"
}

def fetch_one(stock_code):
    url = API_ORDERBOOK.format(code=stock_code)

    try:
        r = requests.get(url, headers=HEADERS, timeout=HTTP_TIMEOUT)
    except Exception as e:
        print(f"[ERROR] {stock_code} request failed: {e}")
        return

    # === AUTH ERROR ===
    if r.status_code == 401:
        raise RuntimeError("TOKEN EXPIRED")

    # === HTTP ERROR ===
    if r.status_code != 200:
        print(f"[FAIL] {stock_code} status {r.status_code}")
        return

    # === PARSE JSON AMAN ===
    try:
        payload = r.json()
    except Exception:
        print(f"[FAIL] {stock_code} invalid JSON")
        return

    data = payload.get("data")

    # === GUARD PALING PENTING (ANTI CRASH) ===
    if not isinstance(data, dict):
        print(f"[EMPTY] {stock_code}")
        return

    bids = data.get("bids", [])[:10]
    asks = data.get("asks", [])[:10]

    # Kalau bener-bener kosong
    if not bids and not asks:
        print(f"[EMPTY] {stock_code}")
        return

    ts = datetime.now()
    rows = []

    for i, b in enumerate(bids, 1):
        rows.append((ts, stock_code, "BID", i, b["price"], b["volume"]))

    for i, a in enumerate(asks, 1):
        rows.append((ts, stock_code, "ASK", i, a["price"], a["volume"]))

    insert_orderbook(rows)
    print(f"[OK] {stock_code}")
