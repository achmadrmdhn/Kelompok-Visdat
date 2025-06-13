# Pie Chart
import streamlit as st
import matplotlib.pyplot as plt

#Data partisipasi siswa
kegiatan = ['Olahraga', 'Seni', "Musik", "Debat"]
persentase = [35, 25, 20, 20]

#Fungsi untuk membuat pie chart
def plot_pie_chart(labels, data):
    fig, ax = plt.subplots()
    ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.set_title('Persentase Partisipasi Siswa dalam Kegiatan Ekstrakurikuler')
    st.pyplot(fig)

#Streamlit interface
st.title("Visualisasi Data Kegiatan Ekstrakurikuler")
st.subheader("Pie Chart Sederhana")
plot_pie_chart(kegiatan, persentase)

#Fungsi untuk pie chart dengan kustomisasi
def plot_customized_pie(labels, data):
    colors = ['gold', 'lightblue', 'lightgreen', 'coral']
    explode = [0.1, 0, 0, 0] # Menonjolkan "Olahraga"
    fig, ax = plt.subplots()
    ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=explode, shadow=True)
    ax.set_title('Kustomisasi Pie Chart')
    st.pyplot(fig)

#Streamlit interface untuk kustomisasi
st.subheader("Kustomisasi Pie Chart")
plot_customized_pie(kegiatan, persentase)

#Fungsi untuk multiple chart
def plot_multiple_pie():
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))

    # Data Kelompok 1
    kegiatan_1 = ['Olahraga', 'Seni']
    persentase_1 = [40, 60]

    # Data kelompok 2
    kegiatan_2 = ['Musik', 'Debat']
    persentase_2 = [50, 50]

    #Pie chart untuk kelompok 1
    axs[0].pie(persentase_1, labels=kegiatan_1, autopct='%1.1f%%', startangle=140, colors=['gold', "lightblue"])
    axs[0].set_title('Grup 1')

    #Pie chart untuk kelompok 2
    axs[1].pie(persentase_2, labels=kegiatan_2, autopct='%1.1f%%', startangle=140, colors=['lightgreen', 'coral'])
    axs[1].set_title('Grup 2')

    st.pyplot(fig)

#Streamlit Interface untuk multiple pie chart
st.subheader("Multiple Pie Chart")
plot_multiple_pie()


# Area Chart
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#Data Penjualan Bulanan
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
shoes = [500, 600, 700, 800, 650, 700, 850, 900, 750, 800, 950, 1000]
sandals = [300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850]
socks = [200, 250, 300, 350, 300, 400, 450, 500, 600, 700, 750, 800]

#Fungsi untuk Membuat Area Chart
def plot_area_chart(selected_products):
    plt.figure(figsize=(10, 6))

    #Memilih produk yang akan divisualisasikan
    if 'Sepatu' in selected_products:
        plt.fill_between(months, shoes, color="blue", alpha=0.5, label="Sepatu")

    if 'Sandal' in selected_products:
        plt.fill_between(months, sandals, color="green", alpha=0.5, label="Sandal")

    if 'Kaos Kaki' in selected_products:
        plt.fill_between(months, socks, color="orange", alpha=0.5, label="Kaos Kaki")

    plt.title("Area Chart: Penjualan Bulanan")
    plt.xlabel("Bulan")
    plt.ylabel("Unit Terjual")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.legend()
    st.pyplot(plt)

#Aplikasi Streamlit
def main():
    st.title("Visualisasi Penjualan Bulanan")
    st.sidebar.title("Pengaturan Grafik")

    # Filter Produk
    st.sidebar.markdown("### Pilih Produk")
    products = ['Sepatu', 'Sandal', 'Kaos Kaki']
    selected_products = st.sidebar.multiselect("Produk yang akan ditampilkan:", products, default=products)

    st.markdown("### Area Chart Penjualan")
    plot_area_chart(selected_products)

if __name__ == "__main__":
    main()