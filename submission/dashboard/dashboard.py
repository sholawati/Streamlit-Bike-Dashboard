import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Path aman agar bisa diakses di Streamlit Cloud
current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'main_data.csv')

# Load data
df = pd.read_csv(file_path)

# Sidebar filter
selected_season = st.sidebar.selectbox("Pilih Musim", df['season'].unique())
selected_weather = st.sidebar.selectbox("Pilih Cuaca", df['weather'].unique())

# Filter data
filtered_df = df[(df['season'] == selected_season) & (df['weather'] == selected_weather)]

st.title("Dashboard Penyewaan Sepeda")

# Ringkasan Statistik
st.subheader("Ringkasan Statistik")
st.metric("Total Penyewaan", int(filtered_df['total_rentals'].sum()))
st.metric("Rata-rata Penyewaan", round(filtered_df['total_rentals'].mean(), 2))

# Tren Harian
st.subheader("Grafik Tren Penyewaan")
fig, ax = plt.subplots()
sns.lineplot(x='date', y='total_rentals', data=filtered_df, ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)
