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

# Agrupar y sumar la columna 'Cantidad' por 'Mes' y 'Producto'
ar_prod = ar.groupby(['Mes', 'Producto'], as_index=False)['Cantidad'].sum()
# Renombrar la columna de suma para mayor claridad
ar_prod.rename(columns={'Cantidad': 'Cant_mes_prod'}, inplace=True)

# Agrupar y sumar la columna 'Cantidad' por 'Mes' y 'Producto'
ar_region = ar.groupby(['Mes', 'Region'], as_index=False)['Cantidad'].sum()

# Renombrar la columna de suma para mayor claridad
ar_region.rename(columns={'Cantidad': 'Cant_mes_reg'}, inplace=True)

#Creo una barra lateral para el filtro
st.sidebar.header('Filtros')


# Creo las tabs
tab1, tab2, tab3 = st.tabs(['Base de datos', '📈 Gráfico por mes', '📈 Región'])

# Pestaña 1: Base de datos
with tab1:
    st.subheader('Base de datos')
    st.write(ar)

# Pestaña 2: Gráfico por mes
with tab2:
    st.subheader('📈 Gráfico por mes')
    
    # Aplicar filtros
    filtro_mes = st.sidebar.multiselect('Filtra por Mes:', ar_prod['Mes'].unique())
    filtro_prod = st.sidebar.multiselect('Filtra por Producto:', ar_prod['Producto'].unique())
    
    # Filtrar datos
    if filtro_mes:
        ar_prod = ar_prod[ar_prod['Mes'].isin(filtro_mes)]
    if filtro_prod:
        ar_prod = ar_prod[ar_prod['Producto'].isin(filtro_prod)]
    
    # Crear gráfico
    fig2 = px.bar(ar_prod, x='Producto', y='Cant_mes_prod', color='Mes', title='Cantidad vendida por mes y producto')
    st.plotly_chart(fig2)

# Pestaña 3: Gráfico por región
with tab3:
    st.header('📈 Región')
    
    # Aplicar filtros
    if filtro_mes:
        ar_region = ar_region[ar_region['Mes'].isin(filtro_mes)]
    if filtro_prod:
        ar_region = ar_region[ar_region['Region'].isin(filtro_prod)]
    
    # Crear gráfico
    fig3 = px.line(ar_region, x='Region', y='Cant_mes_reg', color='Mes', title='Cantidad vendida por mes y región')
    st.plotly_chart(fig3)
    