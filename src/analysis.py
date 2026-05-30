import pandas as pd
from pathlib import Path

def retornarPath():
    BASE_DIR = Path(__file__).resolve().parent.parent
    path = BASE_DIR / "data" / "vgsales_processed.csv"
    return path

df = pd.read_csv(retornarPath())



#Bloque 1: Analisis de Mercado Global

def return_Top10_global_Sales():
    df_top10 = df.sort_values("Global_Sales", ascending = False).head(10)
    return(df_top10[["Platform","Name","Global_Sales"]])

#Retorno de platform, publisher, genre
def return_Top_Bloq1(col_name):
    df_top_Platforms = df.groupby(col_name)["Global_Sales"].sum().sort_values(ascending = False)
    return(df_top_Platforms)


#Bloque 2: Analisis por region(global,na,eu,jp)
#Plataformas, publishers, generos
#Region EU
#Region JP
#Region Other_Region

def return_Top_Bloq2(col_name,region):
    df_top_Platforms = df.groupby(col_name)[region].sum().sort_values(ascending = False)
    return(df_top_Platforms)


#Bloque 3: Publishers en profundidad

def return_Top_Publishers():
    df_top_Publishers = df.groupby("Publisher")["Global_Sales"].sum().sort_values(ascending=False).head(3)
    return df_top_Publishers

def return_Top_Publisher_By_Genre():
    df_top_Publishers = df.groupby(["Publisher","Genre"])["Global_Sales"].sum().reset_index().sort_values("Global_Sales", ascending = False)
    df_top_Publishers["rank"] = df_top_Publishers.groupby("Genre")["Global_Sales"].rank(ascending=False,method="min")
    df_dominantes = df_top_Publishers[df_top_Publishers["rank"] == 1]
    return df_dominantes


#Bloque 4: Estructura del mercado

def return_Market_Distribution():
    total_ventas = df["Global_Sales"].sum()
    total_juegos = len(df)
    df_sorted = df.sort_values("Global_Sales", ascending = False).reset_index(drop = True)
    df_sorted["Ventas_Acumuladas"] = df_sorted["Global_Sales"].cumsum()
    df_sorted["P_Ventas_Acum"] = df_sorted["Ventas_Acumuladas"] / total_ventas * 100
    df_sorted["P_juegos_Acum"] = (df_sorted.index + 1) / total_juegos * 100
    tramos = [1,5,10,25,50]
    resultados = []

    for pct in tramos:
        n_juegos = int(total_juegos * pct / 100)
        ventas_tramo = df_sorted.head(n_juegos)["Global_Sales"].sum()
        resultados.append({
            "top_%": pct,
            "n_juegos": n_juegos,
            "ventas_M": round(ventas_tramo, 2),
            "% del total": round(ventas_tramo / total_ventas * 100, 1)
        })

    return pd.DataFrame(resultados)
    
def return_concentracion_top10():
    df_sorted = df.sort_values("Global_Sales", ascending=False)
    top10 = df_sorted.head(10)
    resto = df_sorted.iloc[10:]

    total = df["Global_Sales"].sum()

    resultado = pd.DataFrame([
        {
            "grupo": "Top 10 juegos",
            "n_juegos": 10,
            "ventas_M": round(top10["Global_Sales"].sum(), 2),
            "% del total": round(top10["Global_Sales"].sum() / total * 100, 1)
        },
        {
            "grupo": "Resto",
            "n_juegos": len(resto),
            "ventas_M": round(resto["Global_Sales"].sum(), 2),
            "% del total": round(resto["Global_Sales"].sum() / total * 100, 1)
        }
    ])
    return resultado