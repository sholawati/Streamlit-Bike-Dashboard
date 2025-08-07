# Streamlit Dashboard Penyewaan Sepeda

Proyek ini merupakan dashboard interaktif berbasis **Streamlit** yang menampilkan analisis tren penyewaan sepeda menggunakan dataset dari Dicoding (`data_1.csv` dan `data_2.csv`).

---

## Struktur Folder

```
submission/
├── dashboard/
│   ├── main_data.csv          # Dataset yang sudah dibersihkan untuk dashboard
│   └── dashboard.py           # Script utama untuk menjalankan Streamlit
├── data/
│   ├── data_1.csv             # Dataset asli
│   └── data_2.csv             # Dataset asli
├── notebook.ipynb            # Notebook untuk analisis eksploratif data (EDA)
├── README.md                 # Petunjuk penggunaan proyek
├── requirements.txt          # Daftar dependensi Python
└── url.txt                   # Link menuju dashboard yang sudah di-deploy
```

---

## Cara Menjalankan Dashboard Secara Lokal

Ikuti langkah-langkah berikut untuk menjalankan dashboard di komputer Anda:

### 1. Clone Repository

Buka terminal/command prompt Anda, lalu jalankan perintah berikut:

```bash
git clone https://github.com/sholawati/Streamlit-Bike-Dashboard.
```

### 2. Masuk ke folder Streamlit-Bike-Dashboard

Masih pada terminal/command prompt Anda, lalu jalankan perintah berikut:

```bash
cd Streamlit-Bike-Dashboard
```

### 3. Install Library yang Dibutuhkan

Masih pada terminal/command prompt Anda, lalu jalankan perintah berikut:

```bash
pip install -r requirements.txt
```

### 4. install streamlit

Masih pada terminal/command prompt Anda, lalu jalankan perintah berikut:

```bash
pip install streamlit
```

### 5. Jalankan Dashboard

Masih pada terminal/command prompt Anda, lalu jalankan perintah berikut:

```bash
streamlit run submission/dashboard/dashboard.py
```

Streamlit akan otomatis membuka tab browser ke alamat lokal seperti `http://localhost:8501`.

---

## Link Deployment

Jika Anda ingin melihat versi online dari dashboard ini (jika sudah di-deploy), silakan buka tautan yang tersedia di file `url.txt`.

---

## Catatan Tambahan

- Pastikan Python sudah terinstall di sistem Anda (disarankan versi 3.9 atau lebih baru).
- Jika ada error terkait `seaborn`, `pandas`, atau `streamlit`, pastikan semua dependensi sudah terinstall dengan benar dari file `requirements.txt`.
- Jika Anda ingin menjalankan ulang notebook analisis, pastikan Jupyter Notebook juga terinstall (`pip install notebook`).
