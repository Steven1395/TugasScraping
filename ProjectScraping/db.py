import mysql.connector
from config import DB_CONFIG

# Fungsi ini yang dipanggil oleh fetcher.py
def insert_orderbook(rows):
    try:
        # Membuka koneksi baru setiap kali insert
        conn = mysql.connector.connect(**DB_CONFIG)
        cur = conn.cursor()
        q = """
        INSERT INTO orderbook_history
        (timestamp, stock_code, type, urutan, price, lot)
        VALUES (%s,%s,%s,%s,%s,%s)
        """
        cur.executemany(q, rows)
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"[DB ERROR] {e}")

# Class DBWriter untuk penggunaan buffer jika dibutuhkan di masa depan
class DBWriter:
    def __init__(self):
        self.conn = mysql.connector.connect(**DB_CONFIG)
        self.cur = self.conn.cursor()
        self.buffer = []

    def add_rows(self, rows):
        self.buffer.extend(rows)

    def flush(self):
        if not self.buffer:
            return
        q = """
        INSERT INTO orderbook_history
        (timestamp, stock_code, type, urutan, price, lot)
        VALUES (%s,%s,%s,%s,%s,%s)
        """
        self.cur.executemany(q, self.buffer)
        self.conn.commit()
        self.buffer.clear()

    def close(self):
        self.flush()
        self.cur.close()
        self.conn.close()