import streamlit as st
from src.analysis import return_Top10_global_Sales, return_concentracion_top10, return_Market_Distribution, return_Top_Bloq1, return_Top_Bloq2, return_Top_Publishers, return_Top_Publishers_Genre

st.title("Analisis de videojuegos")

st.subheader("Top 10 juegos globales")
st.dataframe(return_Top10_global_Sales())

st.subheader("Concentracion del top 10 de juegos")
st.dataframe(return_concentracion_top10())

st.subheader("Distribucion de mercado")
st.dataframe(return_Market_Distribution())


st.title("Analisis mercado global")

st.title("Mejor plataforma")
st.dataframe(return_Top_Bloq1("Platform"))
st.title("Mejor publisher")
st.dataframe(return_Top_Bloq1("Publisher"))
st.title("Mejor genero")
st.dataframe(return_Top_Bloq1("Genre"))


st.title("Analisis por region")

st.title("Region NA")
st.dataframe(return_Top_Bloq2())
st.title("Region EU")
st.dataframe(return_Top_Bloq2())
st.title("Region JP")
st.dataframe(return_Top_Bloq2())
st.title("Otras regiones")


st.title("Analisis de publishers en profundidad")
st.title("Top publishers")
st.dataframe(return_Top_Publishers())
st.title("Top publishers por genero")
st.dataframe(return_Top_Publishers_Genre())