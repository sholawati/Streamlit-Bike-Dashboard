import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('/dashboard/main_data.csv')

# Preprocessing ulang (jika belum)
df['dteday'] = pd.to_datetime(df['dteday'])
df.rename(columns={'dteday': 'date', 'yr': 'year', 'mnth': 'month', 'hum': 'humidity', 'cnt': 'total_rentals', 'atemp': 'feels_like', 'weathersit': 'weather'}, inplace=True)
df['season'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
df['weather'] = df['weather'].map({1: 'Clear', 2: 'Mist/Cloudy', 3: 'Light Rain/Snow', 4: 'Heavy Rain/Snow'})
df['year'] = df['year'].map({0: 2011, 1: 2012})

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
