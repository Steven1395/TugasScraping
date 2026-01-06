import streamlit as st
import pandas as pd
import mysql.connector
import sys
import os

# =============================================================
# 1. PATH HACK (Agar bisa baca config.py di folder induk)
# =============================================================
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

try:
    from config import DB_CONFIG
except ImportError:
    st.error("File config.py tidak ditemukan! Pastikan dashboard.py berada di dalam sub-folder ProjectScraping.")

# =============================================================
# 2. KONFIGURASI HALAMAN
# =============================================================
st.set_page_config(page_title="Stockbit Scraper Dashboard", layout="wide")

def get_data():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        # Mengambil 20.000 baris terbaru
        query = "SELECT * FROM orderbook_history ORDER BY TIMESTAMP DESC LIMIT 20000"
        df = pd.read_sql(query, conn)
        conn.close()
        
        # Force semua kolom jadi huruf kecil agar tidak KeyError
        df.columns = [c.lower() for c in df.columns]
        return df
    except Exception as e:
        st.error(f"Gagal koneksi ke database: {e}")
        return pd.DataFrame()

# =============================================================
# 3. SIDEBAR (Kontrol & Filter)
# =============================================================
st.sidebar.title("🎮 Control Panel")

if st.sidebar.button('🔄 Refresh Data'):
    st.rerun()

df = get_data()

# Filter Pencarian Saham
st.sidebar.markdown("---")
st.sidebar.subheader("🔍 Cari Saham")
if not df.empty:
    list_saham = ["SEMUA"] + sorted(df['stock_code'].unique().tolist())
    selected_stock = st.sidebar.selectbox("Pilih Kode Saham:", list_saham)
else:
    selected_stock = "SEMUA"

# =============================================================
# 4. MAIN DASHBOARD
# =============================================================
st.title("📊 Saham Orderbook Dashboard")
st.markdown(f"Menampilkan data real-time hasil scraping")

if not df.empty:
    # Logic Filter
    if selected_stock != "SEMUA":
        display_df = df[df['stock_code'] == selected_stock]
    else:
        display_df = df

    # --- ROW 1: METRICS ---
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Baris di DB", len(df))
    col2.metric("Jumlah Emiten Terdeteksi", df['stock_code'].nunique())
    col3.metric("Data Terbaru Pada", str(df['timestamp'].iloc[0]))

    # --- ROW 2: VISUALISASI ---
    st.markdown("---")
    if selected_stock == "SEMUA":
        st.subheader("🔥 Top 10 Saham dengan Volume BID Terbesar")
        # Agregasi volume per saham
        top_bid = df[df['type'] == 'BID'].groupby('stock_code')['lot'].sum().sort_values(ascending=False).head(10)
        st.bar_chart(top_bid)
    else:
        st.subheader(f"📈 Visualisasi Antrean: {selected_stock}")
        # Grafik harga vs volume untuk saham tertentu
        stock_data = display_df.head(20) # Ambil 10 bid & 10 ask terbaru
        st.bar_chart(data=stock_data, x='price', y='lot', color='type')

    # --- ROW 3: TABEL DATA ---
    st.markdown("---")
    st.subheader(f"📜 Detail Antrean ({selected_stock})")
    st.dataframe(display_df.head(100), use_container_width=True)
    
else:
    st.warning("Database masih kosong atau koneksi bermasalah. Pastikan XAMPP nyala dan main.py sudah dijalankan.")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Steven's Project - Pangkalan Data 2024")