import streamlit as st
import pandas as pd

df = pd.read_excel('fuente/lista.xlsx')
st.write(df)
suma_cantidad = df['Cantidad'].sum()
suma_conteo = df['Conteo'].sum()
st.write(f'La cantidad total de invitados es: {suma_cantidad}')
st.write(f"El conteo es: {suma_conteo}")

diferencia = suma_cantidad - suma_conteo
st.write(f'faltan por llegar: {diferencia}')