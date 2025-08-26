import streamlit as st
from PIL import Image

st.title("Mi primera App!")
st.write("Easy")
image = Image.opne('gato.jpg')
st.image(image, caption = 'Interfaces multimodales')
