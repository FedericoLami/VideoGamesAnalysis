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

def return_Top_Publishers_Genre():
    df_top_Publishers = df.groupby("Publishers")["Genre"].sum().sort_values(ascending = False).head(3)
    return df_top_Publishers

def return_Top_Publishers_Genre():
    df_pg = df.groupby(["Publisher","Genre"])["Global_Sales"].sum().reset_index()
    df_pg["rank"] = df_pg.groupby("Genre")["Global_Sales"].rank(ascending=False,method="min")
    df_dominantes = df_pg[df_pg["rank"] == 1]
    df_result = df_dominantes.groupby("Genre").size()
    return df_result[df_result>1]


