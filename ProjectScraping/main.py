import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from fetcher import fetch_one
from config import MAX_WORKERS, REQ_PER_SEC

def load_stocks():
    with open("saham.txt") as f:
        return [x.strip() for x in f if x.strip()]

def main():
    stocks = load_stocks()
    delay = 1 / REQ_PER_SEC

    print(f"Mulai ambil {len(stocks)} emiten...")

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as exe:
        futures = []
        for s in stocks:
            futures.append(exe.submit(fetch_one, s))
            time.sleep(delay)

        for f in as_completed(futures):
            try:
                f.result()
            except Exception as e:
                print("[ERROR]", e)

    print("SELESAI.")

if __name__ == "__main__":
    main()
