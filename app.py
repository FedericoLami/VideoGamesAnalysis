import streamlit as st
from src.analysis import return_Top10_global_Sales


st.title("Analisis de videojuegos")

st.dataframe(return_Top10_global_Sales())