import streamlit as st
import matplotlib.pyplot as plt

# Data dummy
suhu = [20, 22, 24, 26, 28, 30, 32, 34, 36]
penjualan = [50, 60, 70, 90, 100, 110, 130, 150, 180]

# Judul aplikasi
st.title('Visualisasi Hubungan Penjualan Es Krim dengan Suhu')

# Scatter plot menggunakan Matplotlib
fig, ax = plt.subplots()
ax.scatter(suhu, penjualan, color="blue")
ax.set_title('Hubungan Penjualan Es Krim dan Suhu')
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel('Penjualan Es Krim')
# Tampilkan di Streamlit
st.pyplot(fig)

# Kustomisasi scatter plot
fig, ax = plt.subplots()
ax.scatter(suhu, penjualan, color='orange', s=100, edgecolor='black', alpha=0.7)
ax.set_title('Hubungan Penjualan Es Krim dan Suhu (Kustom)')
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel('Penjualan Es Krim')
ax.grid(True)
# Tampilkan di Streamlit
st.pyplot(fig)

# Data tambahan untuk kategori hari
penjualan_kerja = [50, 60, 70, 80, 90, 100, 110, 120, 130]
penjualan_akhir_pekan = [60, 70, 80, 100, 110, 120, 140, 160, 200]

# Multiple scatter plot
fig, ax = plt.subplots()
ax.scatter(suhu, penjualan_kerja, color='green', label='Hari Kerja', s=80)
ax.scatter(suhu, penjualan_akhir_pekan, color='purple', label='Akhir Pekan', s=80)
ax.set_title('Penjualan Es Krim Berdasarkan Hari')
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel('Penjualan Es Krim')
ax.legend()
# Tampilkan di Streamlit
st.pyplot(fig)

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Data dummy
data = {
    'Suhu': [20, 22, 24, 26, 28, 30, 32, 34, 36],
    'Penjualan Cokelat': [50, 60, 70, 80, 90, 100, 110, 120, 130],
    'Penjualan Vanila': [60, 70, 80, 90, 100, 110, 120, 130, 140],
    'Penjualan Stroberi': [40, 50, 60, 70, 80, 90, 100, 110, 120],
    'Kelembapan': [60, 65, 70, 75, 80, 85, 90, 95, 100]
}

# Konversi data ke Dataframe
df = pd.DataFrame(data)

# Judul aplikasi
st.title("Analisis Penjualan Es Krim Berdasarkan Suhu")

# Jenis es krim
jenis_eskrim = st.selectbox('Pilih Jenis Es Krim:', ['Cokelat', 'Vanila', 'Stroberi'])

# Menentukan kolom penjualan berdasarkan pilihan
if jenis_eskrim == 'Cokelat':
    penjualan = df['Penjualan Cokelat']
elif jenis_eskrim == 'Vanila':
    penjualan = df['Penjualan Vanila']
else:
    penjualan = df['Penjualan Stroberi']

# Tampilkan tabel data
st.subheader('Data Penjualan dan Suhu')
st.dataframe(df)

# Membuat Scatter Plot
fig, ax = plt.subplots()
scatter = ax.scatter(df["Suhu"], penjualan, c=df["Kelembapan"], s=100, cmap='coolwarm', alpha=0.7)
ax.set_title(f'Hasil Penjualan {jenis_eskrim} vs Suhu dan Kelembapan')
ax.set_xlabel('Suhu (°C)')
ax.set_ylabel(f'Penjualan Es Krim {jenis_eskrim}')
fig.colorbar(scatter, label='Kelembapan (%)')

# Tampilkan scatter plot di Streamlit
st.pyplot(fig)

# Ringkasan hubungan
st.subheader("Analisis Hubungan")
st.write(f'Grafik menunjukkan hubungan antara suhu, kelembapan, dan penjualan es krim jenis **{jenis_eskrim}**.')