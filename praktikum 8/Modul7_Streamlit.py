import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Penjualan Smartphone Berdasarkan Merek")
st.subheader("Horizontal Bar Chart Sederhana")

#Data Penjualan Smartphone
brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D']
sales = [350, 420, 300, 280]

#Membuat Horizontal Bar Chart
fig, ax = plt.subplots()
y = np.arange(len(brands)) # Posisi untuk batang

ax.barh(y, sales, color='skyblue')
ax.set_yticks(y)
ax.set_yticklabels(brands)
ax.set_xlabel("Total Sales (in Units)")
ax.set_title('Smartphone Sales by Brand')

#Tampilkan di Streamlit
st.pyplot(fig)


import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#Data Penjualan Smartphone (assuming 'brands' and 'sales' are defined as in the previous Streamlit example)
brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D']
sales = [350, 420, 300, 280]

#Warna berbeda untuk setiap batang
colors = ['blue', 'green', 'orange', 'red']

fig, ax = plt.subplots()

ax.barh(y, sales, color=colors)

#Menambahkan nilai pada batang
for i, v in enumerate(sales):
    ax.text(v + 10, i, str(v), color='black', va='center') # Posisi teks

ax.set_yticks(y)
ax.set_yticklabels(brands)
ax.set_xlabel('Total Sales (in Units)')
ax.set_title('Customized Smartphone Sales by Brand')

#Tampilkan di Streamlit
st.pyplot(fig)


import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.subheader("Multiple Horizontal Bar Chart")

#Date Penjualan
brands = ['Brand A', 'Brand B', 'Brand C', 'Brand D']
q1_sales = [350, 400, 300, 250]
q2_sales = [370, 420, 310, 280]

bar_width = 0.4 # Lebar batang
y = np.arange(len(brands))

fig, ax = plt.subplots()

#Membuat Multiple Horizontal Bar Chart
ax.barh(y - bar_width / 2, q1_sales, height=bar_width, label='Q1 Sales', color='skyblue')
ax.barh(y + bar_width / 2, q2_sales, height=bar_width, label='Q2 Sales', color='salmon')

#Penyesuaian tampilan
ax.set_yticks(y)
ax.set_yticklabels(brands)
ax.set_xlabel('Total Sales (in Units)')
ax.set_title('Smartphone Sales by Brand (Multiple Periods)')
ax.legend()

#Tampilkan di Streamlit
st.pyplot(fig)


import matplotlib.pyplot as plt
import numpy as np

#Data penjualan smartphone
brands = ["Samsung", "Iphone", "Vivo", "Oppo"]
sales_2023 = [500, 700, 300, 400]
sales_2024 = [550, 750, 350, 450]
sales_2025 = [600, 800, 400, 500]

y_pos = np.arange(len(brands))

plt.barh(brands, sales_2023, color='skyblue', label='2023')
plt.barh(brands, sales_2024, left=sales_2023, color='salmon', label='2024')

plt.title('Penjualan Smartphone Stacked (2023 & 2024)')
plt.xlabel('Jumlah Penjualan')
plt.ylabel('Merek')
plt.legend()
plt.show()


import matplotlib.pyplot as plt
import numpy as np

#Dato penjuaton smartphone
brands = ["Samsung", "Iphone", "Vivo", "Oppo"]
sales_2023 = [500, 700, 300, 400]
sales_2024 = [550, 750, 350, 450]
sales_2025 = [600, 800, 400, 500]

y_pos = np.arange(len(brands))

plt.barh(brands, sales_2023, color='lightcoral', edgecolor='black', label='2023')
plt.barh(brands, sales_2024, left=sales_2023, color='lightskyblue', edgecolor='black', label='2024')

plt.title('Penjualan Smartphone (Kustom Stacked)')
plt.xlabel('Jumlah Penjualan')
plt.ylabel('Merek')
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.legend()
plt.show()


import matplotlib.pyplot as plt
import numpy as np

#Data penjualan smartphone
brands = ["Samsung", "Iphone", "Vivo", "Oppo"]
sales_2023 = [500, 700, 300, 400]
sales_2024 = [550, 750, 350, 450]
sales_2025 = [600, 800, 400, 500]

y_pos = np.arange(len(brands))

plt.barh(y_pos, sales_2023, color='skyblue', label="2023")
plt.barh(y_pos, sales_2024, left=sales_2023, color='salmon', label='2024')
plt.barh(y_pos, sales_2025, left=np.array(sales_2023) + np.array(sales_2024), color='lightgreen', label='2025') # Changed 'line' to 'lightgreen' as 'line' is not a standard color

plt.yticks(y_pos, brands)
plt.title('Penjualan Smartphone 2023-2025 (Multiple Stacked)')
plt.xlabel("Jumlah Penjualan")
plt.ylabel('Merek')
plt.legend()
plt.show()



import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#Contoh data penjualan
brands = ['Brand A', 'Brand B', 'Brand C']
sales_2022 = [350, 450, 300]
sales_2023 = [400, 500, 320]

def create_stacked_bar_chart():
    fig, ax = plt.subplots(figsize=(10, 6))
    y = np.arange(len(brands))

    ax.barh(y, sales_2022, label='2022', color='skyblue')
    ax.barh(y, sales_2023, left=sales_2022, label='2023', color='orange')

    ax.set_yticks(y)
    ax.set_yticklabels(brands)
    ax.set_xlabel('Sales')
    ax.set_title('Smartphone Sales by Brand')
    ax.legend()
    return fig

#Rendar chart di Streamlit
st.title("Smartphone Sales Visualization")
st.pyplot(create_stacked_bar_chart())


import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

#Contoh data penjualan (assuming brands, sales_2022, sales_2023 are defined as in the previous Streamlit example)
brands = ['Brand A', 'Brand B', 'Brand C']
sales_2022 = [350, 450, 300]
sales_2023 = [400, 500, 320]

def create_custom_stacked_bar_chart():
    fig, ax = plt.subplots(figsize=(10, 6)) # Corrected figsize from (18,6) to (10,6) to prevent excessive width
    y = np.arange(len(brands))

    ax.barh(y, sales_2022, label='2022', color='blue', edgecolor='black', hatch='//')
    ax.barh(y, sales_2023, left=sales_2022, label='2023', color='green', edgecolor='black', hatch='\\')

    ax.set_yticks(y)
    ax.set_yticklabels(brands)
    ax.set_xlabel('Sales')
    ax.set_title('Customized Smartphone Sales by Brand')
    ax.legend()

    #Tambahkan anotasi
    for i in range(len(brands)):
        ax.text(sales_2022[i] / 2, i, f"{sales_2022[i]}", va='center', color='white') # Corrected '1' to 'i' for y-position
        ax.text(sales_2022[i] + sales_2023[i]/2, i, f"{sales_2023[i]}", va='center', color='black') # Corrected '1' to 'i' for y-position

    return fig

st.pyplot(create_custom_stacked_bar_chart())

