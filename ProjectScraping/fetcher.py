import time
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

    r = requests.get(url, headers=HEADERS, timeout=HTTP_TIMEOUT)

    if r.status_code == 401:
        raise RuntimeError("TOKEN EXPIRED")

    if r.status_code != 200:
        print(f"[FAIL] {stock_code} status {r.status_code}")
        return

    data = r.json().get("data", {})
    bids = data.get("bids", [])[:10]
    asks = data.get("asks", [])[:10]

    ts = datetime.now()
    rows = []

    for i, b in enumerate(bids, 1):
        rows.append((ts, stock_code, "BID", i, b["price"], b["volume"]))

    for i, a in enumerate(asks, 1):
        rows.append((ts, stock_code, "ASK", i, a["price"], a["volume"]))

    insert_orderbook(rows)
    print(f"[OK] {stock_code}")
