# Streamlit Dashboard Penyewaan Sepeda

Ini adalah proyek dashboard interaktif berbasis Streamlit untuk menampilkan analisis tren penyewaan sepeda dari dataset `data_1.csv`.

## Struktur Folder

submission/
├── dashboard/
│ ├── main_data.csv # Dataset yang sudah dibersihkan
│ └── dashboard.py # Script Streamlit
├── data/
│ ├── data_1.csv # Dataset asli
│ └── data_2.csv # Dataset asli
├── notebook.ipynb # Notebook analisis
├── README.md # Instruksi ini
├── requirements.txt # Daftar pustaka yang dibutuhkan
└── url.txt # Link dashboard

## Cara Menjalankan Dashboard Secara Lokal

1. **Clone repository:**

```bash
git clone https://github.com/sholawati/Streamlit-Bike-Dashboard.git
cd Streamlit-Bike-Dashboard/submission
```

2. **Install library yang dibutuhkan:**

```bash
pip install -r requirements.txt
```

3. **Jalankan Streamlit:**

```bash
streamlit run dashboard/dashboard.py
```
