import streamlit as st
import matplotlib.pyplot as plt 
import plotly.express as  px
import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt


ar ='demo_data.csv'
ar = pd.read_csv(ar)

st.title ('Mi dashboard VF. Ejercicio b')
st.write(ar)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("Productos")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("Mes")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("Region")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

