import streamlit as st
import pandas as pd
import numpy as np

st.title("Kelompok Syafi'i")
st.text("Sahrul Firdaus - 0110223114\nAchmad Rifa'i Ramadhan - 0110223138\nSaepulloh - 0110222183")

# Bar
st.title('Area')
# Defining dataframe with its values
df = pd.DataFrame(
    np.random.randn(40, 4),
    columns = ["C1", "C2", "C3", "C4"])
# Bar Chart
st.bar_chart(df)

# Line
st.title('Area')
# Defining dataframe with its values
df = pd.DataFrame(
    np.random.randn(40, 4),
    columns = ["C1", "C2", "C3", "C4"])
# Bar Chart
st.line_chart(df)

# Area
st.title('Area')
# Defining dataframe with its values
df = pd.DataFrame(
    np.random.randn(40, 4),
    columns = ["C1", "C2", "C3", "C4"])
# Bar Chart
st.area_chart(df)

# Map
st.title('Map')
# Defining Latitude and Longitude
locate_map = pd.DataFrame(
    np.random.randn(50, 2)/[10, 10] + [15.4589, 75.0078],
    columns = ['latitude', 'longitude']
)
# Map Function
st.map(locate_map)

# Graphviz
import graphviz as graphviz
st.title()