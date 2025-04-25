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

# Graphviz-1
import graphviz as graphviz
st.title('Graphviz')
# Creating graph object
st.graphviz_chart('''
                  digraph {
                      "Training Data" -> "ML Algorithm"
                      "ML Algorithm" -> "Model"
                      "Model" -> "Result Forecasting"
                      "New Data" -> "Model"
                  }
                  ''')

# Graphviz-2
st.title('Graphviz')
# Creating graphlib graph object
graph = graphviz.Digraph()
graph.edge('Training Data', 'ML Algorithm')
graph.edge('ML Algorithm', 'Model')
graph.edge('Model', 'Result Forecasting')
graph.edge('New Data', 'Model')
st.graphviz_chart(graph)

# Column and Navigation
st.title('Column and Navigation')
# Column
st.text('Columns')
# Defining Columns
col1, col2 = st.columns(2)

# Inserting Elements in column 1
col1.write("First Column")
col1.image("gambar1.jpg")
# Inserting Elements in column 2
col2.write("Second Column")
col2.image("gambar2.jpg")

# Spaced-Out Columns
from PIL import Image
img = Image.open("gambar1.jpg")
st.title("Spaced-Out Columns")
# Defining two Rows
for _ in range(2):
# Defining no. of columns with size
    cols = st.columns((3, 1, 2, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)

# Columns with Padding
from PIL import Image
img = Image.open("gambar2.jpg")
st.title("Padding")
# Defining Padding with columns
col1, padding, col2 = st.columns((10, 2, 10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)

# Grids
from PIL import Image
img = Image.open("gambar1.jpg")
st.title("Grid")
# Defining no of Rows
for a in range(4):
# Defining no. of columns with size
    cols = st.columns((1, 1, 1, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)

# Expanders/Accordions
st.title('Expanders')
# Defining Expanders
with st.expander("Streamlit with Python"):
    st.write("Develop ML Applications in Minutes!!!!")

# Containers
st.title("Container")
with st.container():
    st.write("Element Inside Container")
    # Defining Chart Element
    st.line_chart(np.random.randn(40, 4))
    st.write("Element Outside Container")

st.title("Out of Order Container")
# Defining Containers
container_one = st.container()
container_one.write("Element One Inside Container")
st.write("Element Outside Container")
# Now insert few more elements in the container_one
container_one.write("Element Two Inside Container")
container_one.line_chart(np.random.randn(40, 4))

# Empthy Containers
import time
# Empthy Container
with st.empty():
    for seconds in range(5):
        st.write(f" ⌛️ {seconds} seconds have passed")
        time.sleep(1)
        st.write(" ✅ Times up!")

# Sidebars
st.sidebar.title("Sidebar")
st.sidebar.radio("Are you a New User", ["Yes", "No"])
st.sidebar.slider("Select a Number", 0,10)

st.title("Alert Box")
st.success("Successful")
st.warning("Warning")
st.info("Info")
st.error("Error")
st.exception("It is an exception")