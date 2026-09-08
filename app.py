import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Ventas", layout="wide")

st.title("Dashboard de Ventas")

df = pd.read_csv("ventas_snapshot.csv")

st.subheader("Datos de ventas")
st.dataframe(df)

st.subheader("Gráfico de ventas")
st.bar_chart(df.set_index(df.columns[0]))
