import pandas as pd
from pathlib import Path

def retornarPath():
    BASE_DIR = Path(__file__).resolve().parent.parent
    path = BASE_DIR / "data" / "vgsales_processed.csv"

df = pd.read_csv(retornarPath())


#Bloque 1: Analisis de Mercado Global

def return_Top10_global_Sales():
    df_top10 = df.sort_values("Global_Sales", ascending = False).head(10)
    return(df_top10[["Platform","Name","Global_Sales"]])

#Retorno de platform, publisher, genre
def return_Top_Platforms(col_name):
    df_top_Platforms = df.groupby(col_name)["Global_Sales"].sum().sort_values(ascending = False)
    return(df_top_Platforms)


#Bloque 2: Analisis por region(global,na,eu,jp)
#Plataformas, publishers, generos
#Region EU
#Region JP
#Region Other_Region

def return_Top_Platforms(col_name,region):
    df_top_Platforms = df.groupby(col_name)[region].sum().sort_values(ascending = False)
    return(df_top_Platforms)


#Bloque 3: Publishers en profundidad

def return_Top3_Publishers():
    df_top3 = df.groupby("Global_Sales")["Genre"].sum().sort_values(ascending = False).head(3)