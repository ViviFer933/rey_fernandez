import streamlit as st
import matplotlib.pyplot as plt 
import plotly.express as  px
import numpy as np
import pandas as pd
import seaborn as sns

ar ='dashboard_simple_data.csv'
ar = pd.read_csv(ar)


st.title ('Mi dashboard VF')
st.write(ar)

#Creo una barra lateral para el filtro
st.sidebar.header('Filtros')


#Creo un filtro para categoria
filtro_cat = st.sidebar.multiselect('Filtra por Categoria:',ar['Categoria'].unique())
#Creo un filtro para fecha
filtro_fec = st.sidebar.multiselect('Filtra por Fecha:',ar['Fecha'].unique())
df_filtrado=ar.copy()

if filtro_cat:
  df_filtrado = df_filtrado[df_filtrado['Categoria'].isin(filtro_cat)]
  
if filtro_fec:
   df_filtrado = df_filtrado[df_filtrado['Fecha'].isin(filtro_fec)] 

#Creo un grafico de barras
st.subheader('Grafico de barras')
fig2=px.bar(df_filtrado,x='Categoria',y='Fecha', color = 'Categoria', title='cantidad por fecha')
#Mostrar el grafico en Streamlit
st.plotly_chart(fig2)



