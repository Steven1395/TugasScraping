from pathlib import Path
from fetcher import fetch_one
import time

BASE_DIR = Path(__file__).resolve().parent
STOCK_FILE = BASE_DIR / "saham.txt"

def load_stocks():
    with open(STOCK_FILE, encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def format_time(seconds):
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return f"{h}j {m}m {s}d"

def main():
    stocks = load_stocks()
    total = len(stocks)

    print(f"Mulai ambil {total} emiten...")
    start_time = time.time()

    for i, code in enumerate(stocks, 1):
        fetch_one(code)

        elapsed = time.time() - start_time
        avg = elapsed / i
        est_total = avg * total
        remaining = est_total - elapsed

        print(
            f"[{i}/{total}] "
            f"Elapsed: {format_time(elapsed)} | "
            f"ETA: {format_time(remaining)}"
        )

    end_time = time.time()
    total_time = end_time - start_time

    print("\nSELESAI.")
    print(f"Total waktu: {format_time(total_time)}")
    print(f"Rata-rata per emiten: {total_time/total:.2f} detik")

if __name__ == "__main__":
    main()
