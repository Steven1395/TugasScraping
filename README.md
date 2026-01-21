# Tugas Scraping Stockbit

Project ini bertujuan untuk melakukan pengambilan data orderbook saham dari API Stockbit, menyimpan data tersebut ke dalam database MySQL, serta menampilkan hasilnya melalui dashboard sederhana.

## Metode yang Digunakan

Metode yang digunakan adalah HTTP API Scraping (REST API), bukan web scraping berbasis HTML.

### Alur Kerja Program

1. Program mengirim request ke API Stockbit menggunakan Bearer Token
2. API mengembalikan data dalam format JSON
3. Data orderbook (BID & ASK) disimpan ke database MySQL
4. Data dapat ditampilkan kembali melalui dashboard

### Alasan Pemilihan Metode

1. Lebih stabil dibanding scraping HTML
2. Data bersifat real-time / near real-time
3. Struktur data lebih terstruktur (JSON)


## Cara Menjalankan Program
1. Mendapatkan Bearer Token
    - Tutorial pencarian Bearer Token tersedia di folder Lain-lain
    - Token diambil melalui Network tab (DevTools browser)

2. Konfigurasi Token
    - Paste Bearer Token ke dalam file config.py

3. Menjalankan Program Scraping
    - jalankan "main.py"

## Dashboard Sederhana

Dashboard dibuat untuk menampilkan hasil scraping yang sudah tersimpan di database.

### Cara Menjalankan Dashboard

1. Masuk ke folder project:

cd TugasScraping/ProjectScraping

2. Jalankan dashboard:

streamlit run dashboard.py

## Kesimpulan

Program berhasil melakukan scraping data orderbook saham dari Stockbit, menyimpannya ke database, dan menampilkannya kembali melalui dashboard.
Perbedaan struktur data dan orderbook kosong merupakan kondisi normal dari API, bukan kesalahan implementasi.

