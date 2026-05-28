import streamlit as st
from src.analysis import return_Top10_global_Sales, return_concentracion_top10


st.title("Analisis de videojuegos")
st.dataframe(return_Top10_global_Sales())

st.subheader("Concentracion del top 10 de juegos")
st.dataframe(return_concentracion_top10())