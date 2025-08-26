import streamlit as st
from PIL import Image

st.title("Mi primera App 2025!")
st.write("Easy")
image = Image.opne('gato.jpg')
st.image(image, caption = 'Un gato')
