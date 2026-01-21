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
        print(f"[ERROR] {stock_code} request error: {e}")
        return

    # === 1. CEK AUTH ===
    if r.status_code == 401:
        raise RuntimeError("TOKEN EXPIRED - Ambil token baru di Chrome!")

    if r.status_code != 200:
        print(f"[FAIL] {stock_code} HTTP {r.status_code}")
        return

    # === 2. PARSE DATA (Sesuai Raw JSON) ===
    try:
        payload = r.json()
        data = payload.get("data", {})
        
        # KEY ASLI: 'bid' dan 'offer'
        raw_bids = data.get("bid", [])[:10]
        raw_offers = data.get("offer", [])[:10]
    except Exception as e:
        print(f"[FAIL] {stock_code} parse error: {e}")
        return

    ts = datetime.now()
    rows = []

    # === 3. MAPPING BID (BELI) ===
    for i, b in enumerate(raw_bids, 1):
        try:
            # Konversi string ke int karena JSON Stockbit itu string
            price = int(b["price"])
            volume = int(b["volume"])
            rows.append((ts, stock_code, "BID", i, price, volume))
        except (KeyError, ValueError):
            continue

    # === 4. MAPPING OFFER (JUAL) ===
    for i, o in enumerate(raw_offers, 1):
        try:
            price = int(o["price"])
            volume = int(o["volume"])
            rows.append((ts, stock_code, "ASK", i, price, volume))
        except (KeyError, ValueError):
            continue

    # === 5. INSERT KE DATABASE ===
    if rows:
        insert_orderbook(rows)
        print(f"[OK] {stock_code} - {len(rows)} baris masuk DB")
    else:
        print(f"[KOSONG] {stock_code} - Tidak ada antrian saat ini")