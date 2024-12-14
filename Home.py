import pandas as pd
import matplotlib as plt
import numpy as np
import streamlit as st
from PIL import Image

st.title('Linear Algebra')
st.image('logo.jpg')

st.header('Image processing')
st.subheader('By Grup 5')

st.subheader('Idustrial Engineering_2024')
st.subheader('Streamlit Application The Result of Project Image Processing Grup 5, Subject Linear Aljebra')

st.sidebar.header('Feedback')

option = st.sidebar.selectbox(
    'Please Select',
    ('Good', 'Not Good','Observation')
)
option = st.sidebar.button('save')



