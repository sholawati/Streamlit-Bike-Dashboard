import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- Load Data ---
file_path = os.path.join(os.path.dirname(__file__), 'main_data.csv')
df = pd.read_csv(file_path)

# --- Sidebar Filters ---
st.sidebar.title("Filter Data")

# Filter Musim
seasons = df['season'].unique().tolist()
selected_season = st.sidebar.selectbox("Pilih Musim", ['All'] + seasons)

# Filter Cuaca
weathers = df['weather'].unique().tolist()
selected_weather = st.sidebar.selectbox("Pilih Cuaca", ['All'] + weathers)

# Terapkan Filter
df_filtered = df.copy()
if selected_season != 'All':
    df_filtered = df_filtered[df_filtered['season'] == selected_season]
if selected_weather != 'All':
    df_filtered = df_filtered[df_filtered['weather'] == selected_weather]

# --- Judul Dashboard ---
st.title("📊 Dashboard Penyewaan Sepeda")
st.markdown("Analisis jumlah penyewaan sepeda berdasarkan musim dan cuaca.")

# --- Ringkasan Statistik ---
st.subheader("📈 Ringkasan Statistik")
total = df_filtered['total_rentals'].sum()
rata2 = df_filtered['total_rentals'].mean()
tertinggi = df_filtered['total_rentals'].max()

col1, col2, col3 = st.columns(3)
col1.metric("Total Penyewaan", f"{total:,}")
col2.metric("Rata-rata Harian", f"{rata2:,.2f}")
col3.metric("Tertinggi", f"{tertinggi:,}")

# --- Grafik Tren Penyewaan ---
st.subheader("📅 Tren Penyewaan Sepeda")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=df_filtered, x='date', y='total_rentals', ax=ax)
ax.set_title("Tren Penyewaan Harian")
ax.set_xlabel("Tanggal")
ax.set_ylabel("Total Penyewaan")
plt.xticks(rotation=45)
st.pyplot(fig)
