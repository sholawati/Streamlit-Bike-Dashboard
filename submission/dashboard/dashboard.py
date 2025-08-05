import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Konfigurasi dasar
st.set_page_config(page_title="Dashboard Penyewaan Sepeda", layout="wide")
sns.set(style="whitegrid")
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 14

# Load data
df = pd.read_csv('data/data_1.csv')
df['season'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
df['weather'] = df['weathersit'].map({
    1: 'Clear',
    2: 'Mist/Cloudy',
    3: 'Light Rain/Snow',
    4: 'Heavy Rain/Snow'
})
df['dteday'] = pd.to_datetime(df['dteday'])

# Judul utama
st.title("Dashboard Penyewaan Sepeda")

# Sidebar Filter
st.sidebar.header("Filter Data")
selected_season = st.sidebar.multiselect("Pilih Musim", options=df["season"].unique(), default=df["season"].unique())
selected_weather = st.sidebar.multiselect("Pilih Cuaca", options=df["weather"].unique(), default=df["weather"].unique())

# Filter data
filtered_df = df[(df["season"].isin(selected_season)) & (df["weather"].isin(selected_weather))]

# Dropdown untuk jenis visualisasi
option = st.selectbox("Pilih Jenis Analisis", ["Penyewaan per Musim", "Penyewaan berdasarkan Cuaca"])

# Visualisasi
if option == "Penyewaan per Musim":
    st.subheader("Jumlah Penyewaan Sepeda per Musim (dengan Filter)")
    season_df = filtered_df.groupby("season")["cnt"].sum().reset_index().sort_values(by="cnt", ascending=False)
    
    fig, ax = plt.subplots()
    sns.barplot(x="season", y="cnt", data=season_df, palette="Set2", ax=ax)
    ax.set_xlabel("Musim")
    ax.set_ylabel("Jumlah Penyewaan")
    ax.set_title("Jumlah Penyewaan Berdasarkan Musim")
    st.pyplot(fig)

elif option == "Penyewaan berdasarkan Cuaca":
    st.subheader("Jumlah Penyewaan Sepeda berdasarkan Cuaca (dengan Filter)")
    weather_df = filtered_df.groupby("weather")["cnt"].sum().reset_index().sort_values(by="cnt", ascending=False)

    fig, ax = plt.subplots()
    sns.barplot(x="weather", y="cnt", data=weather_df, palette="Set1", ax=ax)
    ax.set_xlabel("Cuaca")
    ax.set_ylabel("Jumlah Penyewaan")
    ax.set_title("Jumlah Penyewaan Berdasarkan Cuaca")
    st.pyplot(fig)

st.markdown("---")
st.markdown("**Catatan:**")
st.markdown("- Filter di sidebar memungkinkan eksplorasi data berdasarkan *musim* dan *cuaca*.")
st.markdown("- Gunakan dropdown untuk memilih jenis visualisasi yang ingin ditampilkan.")
st.markdown("- Warna digunakan untuk menonjolkan perbedaan antar kategori.")
