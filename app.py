import streamlit as st
from src.analysis import return_Top10_global_Sales, return_concentracion_top10, return_Market_Distribution, return_Top_Bloq1, return_Top_Bloq2, return_Top_Publishers, return_Top_Publishers_Genre

st.title("Analisis de videojuegos")

st.subheader("Top 10 juegos globales")
st.dataframe(return_Top10_global_Sales())

st.subheader("Concentracion del top 10 de juegos")
st.dataframe(return_concentracion_top10())

st.subheader("Distribucion de mercado")
st.dataframe(return_Market_Distribution())


st.header("Analisis mercado global")

st.subheader("Mejor plataforma")
st.dataframe(return_Top_Bloq1("Platform"))
st.subheader("Mejor publisher")
st.dataframe(return_Top_Bloq1("Publisher"))
st.subheader("Mejor genero")
st.dataframe(return_Top_Bloq1("Genre"))


st.title("Analisis por region")

st.header("Region NA")

st.subheader("Top plataformas en NA")
st.dataframe(return_Top_Bloq2("Platform","NA_sales"))
st.subheader("Top publishers en NA")
st.dataframe(return_Top_Bloq2("Publishers","NA_sales"))
st.subheader("Top generos en NA")
st.dataframe(return_Top_Bloq2("Genre","Na_sales"))


st.header("Region EU")
st.subheader("Top plataformas en NA")
st.dataframe(return_Top_Bloq2("Platform","EU_sales"))
st.subheader("Top publishers en NA")
st.dataframe(return_Top_Bloq2("Publishers","EU_sales"))
st.subheader("Top generos en NA")
st.dataframe(return_Top_Bloq2("Genre","EU_sales"))

st.header("Region JP")
st.subheader("Top plataformas en JP")
st.dataframe(return_Top_Bloq2("Platform","JP_sales"))
st.subheader("Top publishers en JP")
st.dataframe(return_Top_Bloq2("Publishers","JP_sales"))
st.subheader("Top generos en JP")
st.dataframe(return_Top_Bloq2("Genre","JP_sales"))


st.header("Otras regiones")
st.subheader("Top plataformas en otras regiones")
st.dataframe(return_Top_Bloq2("Platform","Other_sales"))
st.subheader("Top publishers en JP")
st.dataframe(return_Top_Bloq2("Publishers","Other_sales"))
st.subheader("Top generos en JP")
st.dataframe(return_Top_Bloq2("Genre","Other_sales"))


st.header("Analisis de publishers en profundidad")
st.subheader("Top publishers")
st.dataframe(return_Top_Publishers())
st.subheader("Top publishers por genero")
st.dataframe(return_Top_Publishers_Genre())