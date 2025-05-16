import streamlit as st
import matplotlib.pyplot as plt

# Data sample
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10, 20, 15, 25, 30, 45, 40, 50, 60, 55, 65, 70]
product_B_sales = [5, 10, 8, 15, 18, 20, 22, 30, 25, 35, 40, 45]

# streamlit layout
st.title("Visualisasi Penjualan Produk")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih Tipe Visualisasi", ("Line Chart", "Kustomisasi Line Plot", "Garis Berbeda Menunjukkan Trend", "Subplot"))

def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales)
    ax.set_title('Penjualan Produk A Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    st.pyplot(fig)


def customize_line_plot():
    fig, ax =plt.subplots()
    ax.plot(months, product_A_sales, label = 'Product A', color='blue', linestyle ='--', marker ='o')
    ax.plot(months, product_B_sales, label = 'Product B', color='red', linestyle ='-', marker ='x')
    ax.set_title('Penjualan Produk Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

def trends_lines_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label = 'Product A Trend', color='blue', linestyle ='--')
    ax.plot(months, product_B_sales, label = 'Product B Trend', color='red', linestyle ='-')
    ax.set_title('Tren Penjualan Produk Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

def subplot():
    fig,ax = plt.subplots(2,1, figsize=(10,8))

    #plot untuk produk A
    ax[0].plot(months, product_A_sales, label = 'Product A', color='blue', marker ='o')
    ax[0].set_title('Penjualan Produk A Per Bulan')
    ax[0].set_xlabel('Bulan')
    ax[0].set_ylabel('Jumlah Penjualan')
    ax[0].legend()
    ax[0].grid(True)
    #plot untuyk produk B
    ax[1].plot(months, product_B_sales, label = 'Product B', color='red', marker ='x')
    ax[1].set_title('Penjualan Produk B Per Bulan')
    ax[1].set_xlabel('Bulan')
    ax[1].set_ylabel('Jumlah Penjualan')
    ax[1].legend()
    ax[1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)

if option == "Line Chart":
    line_plot()
elif option == "Kustomisasi Line Plot":
    customize_line_plot()
elif option == "Garis Berbeda Menunjukkan Trend":
    trends_lines_plot()
elif option == "Subplot":
    subplot()