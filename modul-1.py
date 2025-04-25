import streamlit as st
st.title ('Praktikum 2 Edisi Belajar Streamlit!')
#Text Element
st.text('Saya Sahrul Firdaus')
st.text('Dengan NIM 0110223114')
st.text('Halo Saya Achmad Rifa\'i Ramadhan')
st.text('Dengan NIM 0110223138')
st.text('Dan Saya Adalah Saepulloh')
st.text('Dengan NIM 0110222183')


st.title('Ini Cara Membuat Judul')
st.header('Ini Cara Membuat Header')
st.subheader('Ini Cara Membuat Sub-Header')
st.caption('Ini cara Membuat Caption')


#Displaying plain Text
st.text('Hi,\nOrang Sukses \t!!!!!')
st.text('Selamat Datang di')
st.text("""Dunia Steamlit Sahrul""")

#Displaying Markdown
st.markdown('# Hi,\n***Orang Sukses*** \t!!!!!')
st.markdown('## Selamat Datang di')
st.markdown("""### Dunia Steamlit Sahrul""")


#Displaying Latex
# Displaying Latex
st.latex(r'''cos2\theta = 1 - 2sin^2\theta''')
st.latex("""(a+b)^2 = a^2 + b^2 + 2ab""")
st.latex(r'''\frac{\partial u}{\partial t} 
= h^2 \left( \frac{\partial^2 u}{\partial x^2} 
+ \frac{\partial^2 u}{\partial y^2} 
+ \frac{\partial^2 u}{\partial z^2} \right)''')

# Displaying Python Code
st.subheader("""Python Code""")
code = '''def hello():
print("Hello, Streamlit!")'''
st.code(code, language='python')

# Displaying Java Code
st.subheader("""Java Code""")
st.code("""public class GFG {
public static void main(String args[])
{
  System.out.println("Hello World");
}
}""", language='javascript')

st.subheader("""JavaScript Code""")
st.code(""" <p id="demo"></p>
<script>
try {
adddlert("Welcome guest!");
}
catch(err) {
document.getElementById("demo").innerHTML = err.message;
}
</script> """)


st.header('Belajar Dataframe')
import streamlit as st
import pandas as pd
import numpy as np
# defining random values in a dataframe using pandas and numpy
# of a pd.DataFrame
df=pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col %d' % i for i in range(10)))
st.dataframe(df)

st.subheader('Dataframe dengan highlight')
import streamlit as st
import pandas as pd
import numpy as np
# defining random values in a dataframe using pandas and numpy
# of a pd.DataFrame
df=pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col %d' % i for i in range(10)))
# highlighting maximum value in dataframe
st.dataframe(df.style.highlight_max(axis=0))

st.header('Table')
import streamlit as st
import pandas as pd
import numpy as np
# defining random values in a dataframe using pandas and numpy
# of a pd.DataFrame
df=pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col %d' % i for i in range(10)))
# displaying in table
st.table(df)

st.header('Metrics')
import streamlit as st
# defining metrics
st.metric(label="Temperature", value='31 C', delta=1.2)

import streamlit as st
x, y, z = st.columns(3)
# defining metrics
x.metric("Rainfall", "100 cm", "10 cm")
y.metric(label="Populatin", value= "8.2 Million", delta= "1 Billions", delta_color='inverse')
z.metric(label="Customer",value= 100, delta=10, delta_color="off")
st.metric(label="Speed", value=None, delta=0)
st.metric("Trees","91456", "-1132649")



st.header('The write( ) Function as a Superfunction')
import pandas as pd
import numpy as np

df=pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col %d' % i for i in range(10)))

st.write("Here is our data: ", df, "Data is in dataframe format:\n ", "\nThis is a Super function")

import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
# defining random data for Chart
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])

chart= alt.Chart(df).mark_bar().encode(
    x='x', y='y', tooltip=['x', 'y'])

# writing Chart in st.write() function
st.write(chart)


st.header('Magic')
# Function with Magic
"Adding 5 & 4 =", 5 + 4
#displaying Variable 'a' and its value
a= 5
'a', a
"""
# Magic Feature
Markdown working without defining its function explicitly
"""

# Dataframe using Magic
import pandas as pd
df = pd.DataFrame({'col1': [1,2]})
'dataframe',df


import matplotlib.pyplot as plt
import numpy as np
s = np.random.logistic(10,5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
"chart", chart


#Image
st.write('Displaying an Images')
st.image('jeruk.jpg')
st.write('Image Courtesy: unplash.com')

import streamlit as st

# Image Courtesy
st.write("Displaying Multiple Images")

# Listing out animal images
animal_images = [
    'jeruk.jpg',
    'jeruk.jpg',
    'jeruk.jpg',
    'jeruk.jpg',
]
# Displaying Multiple images with width 150
st.image(animal_images, width=150)
# Image Courtesy
st.write("Image Courtesy: Unsplash")


# # Background Image
import streamlit as st
import base64

# Function to set Image as Background
def add_local_background_image(image_file):
    with open(image_file, "rb") as image:
        encoded_string = base64.b64encode(image.read())
        st.write("Image Courtesy: unplash")

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string.decode()}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Calling the function
add_local_background_image("jeruk.jpg")

# Optional text
st.write("Background Image")

#Resizing an Image
import streamlit as st
from PIL import Image

# Membuka gambar asli dari path lokal
original_image = Image.open("jeruk.jpg")

# Menampilkan gambar asli
st.title("Original Image")
st.image(original_image)

# Mengubah ukuran gambar ke 600x400
resized_image = original_image.resize((600, 400))

# Menampilkan gambar yang telah diubah ukurannya
st.title("Resized Image")
st.image(resized_image)



st.title('Creating a Button')
# Defining a Button
button = st.button('Click Here')
if button:
    st.write('You have clicked the Button')
else:
    st.write('You have not clicked the Button')


st.title('Creating Radio Buttons')
# Defining Radio Button
gender = st.radio(
    "Select your gender:",
    ('Male', 'Female', 'Others')
)
if gender == 'Male':
    st.write("You have selected Male.")
elif gender == 'Female':
    st.write("You have selected Female.")
else:
    st.write("You have selected Others.")



st.title('Creating Checkboxes')
st.write('Select your Hobbies:')

# Defining Checkboxes
check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

# Optional: Showing selected hobbies
if check_1:
    st.write("You selected Books.")
if check_2:
    st.write("You selected Movies.")
if check_3:
    st.write("You selected Sports.")
    
    

st.title('Creating Dropdown')
# Creating Dropdown
hobby = st.selectbox(
    'Choose your hobby:',
    ('Books', 'Movies', 'Sports')
)


st.title('Multi-Select')
# Defining Multi_Select with Pre-Selection
hobbies = st.multiselect(
    'What are your Hobbies',
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
    ['Reading', 'Playing']
)


st.title("Download Button")
# Creating Download Button
down_btn = st.download_button(
label = "Download Image",
data = open("jeruk.jpg", "rb"),
file_name = "gambar1.jpg",
mime = "gambar2.jpg"
)


import time
st.title('Progress Bar')
# Defining Progress Bar
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)
st.write('Download Complete')


import time
st.title('Spinner')
# Defining Spinner
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientists')


st.title("Text Box")
# Creating Text Box
name = st.text_input("Enter your Name")
st.write("Your Name is ", name)


# Creating Text Area
input_text = st.text_area("Enter your Review")
# Printing entered text
st.write("""You entered: \n""", input_text)


# Create number input
st.number_input("Enter your Number")
num = st.number_input("Enter your Number", 0, 10, 5, 2)
st.write("Min. Value is 0, \n Max. value is 10")
st.write("Default Value is 5, \n Step Size value is 2")
st.write("Total value after adding Number entered with step values is:", num)


st.title("Time")
# Defining Time Function
st.time_input("Select Yout Time")


st.title("Date")
# Defining Date Function
st.date_input("Select Date")

import datetime
st.title("Date")
# Defining Time Function
st.date_input("Select Your Date", value = datetime.date(1989, 12, 25),
min_value = datetime.date(1987, 1, 1),
max_value = datetime.date(2005, 12, 1))

st.title("Select Color")
# Defining color picker
color_code = st.color_picker("Select your color")
st.header(color_code)


import pandas as pd
st.title("CSV Data")
data_file = st.file_uploader("Upload CSV", type=["csv"])
details = st.button("Check Details")
if details:
    if data_file is not None:
        file_details = {"file_name":data_file.name, "file_type":data_file.type,
        "file_size":data_file.size}
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV File is Uploaded")


my_form = st.form(key='form')
a  = my_form.text_input(label = 'Enter any text')
# Defining submit button
submit_button = my_form.form_submit_button(label = 'Submit')

st.write(a)