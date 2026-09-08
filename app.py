import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Ventas", layout="wide")

st.title("Dashboard de Ventas")

# Empresa A
df_A = pd.read_excel("empresaA.xlsx", sheet_name="HojaA")

# Empresa B
df_B = pd.read_excel("empresaB.xlsx", sheet_name="HojaB")

st.subheader("Empresa A")
st.dataframe(df_A)

st.subheader("Empresa B")
st.dataframe(df_B)
