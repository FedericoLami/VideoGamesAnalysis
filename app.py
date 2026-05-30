import streamlit as st
from src.analysis import return_Top10_global_Sales, return_concentracion_top10, return_Market_Distribution, return_Top_Bloq1, return_Top_Bloq2, return_Top_Publishers, return_Top_Publisher_By_Genre

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

st.dataframe(return_Top_Bloq2("Platform","NA_Sales"))
st.dataframe(return_Top_Bloq2("Publisher","NA_Sales"))
st.dataframe(return_Top_Bloq2("Genre","NA_Sales"))

st.dataframe(return_Top_Bloq2("Platform","EU_Sales"))
st.dataframe(return_Top_Bloq2("Publisher","EU_Sales"))
st.dataframe(return_Top_Bloq2("Genre","EU_Sales"))

st.dataframe(return_Top_Bloq2("Platform","JP_Sales"))
st.dataframe(return_Top_Bloq2("Publisher","JP_Sales"))
st.dataframe(return_Top_Bloq2("Genre","JP_Sales"))

st.dataframe(return_Top_Bloq2("Platform","Other_Sales"))
st.dataframe(return_Top_Bloq2("Publisher","Other_Sales"))
st.dataframe(return_Top_Bloq2("Genre","Other_Sales"))

st.header("Analisis de publishers en profundidad")
st.subheader("Top publishers")
st.dataframe(return_Top_Publishers())
st.subheader("Top publishers por genero")
st.dataframe(return_Top_Publisher_By_Genre())