import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from src.analysis import return_Top10_global_Sales, return_Top_Bloq1


st.set_page_config(page_title="Mercado Global", layout="wide")

# ── Estilos ──────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Space+Grotesk:wght@500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0f1117;
    color: #e8eaf0;
}

.page-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.4rem;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: -0.5px;
    margin-bottom: 0.2rem;
}

.page-subtitle {
    font-size: 1rem;
    color: #8b8fa8;
    margin-bottom: 2.5rem;
}

.section-label {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #5c6bc0;
    margin-bottom: 0.4rem;
}

.section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 1.5rem;
}

.divider {
    border: none;
    border-top: 1px solid #1e2130;
    margin: 2.5rem 0;
}

.rank-badge {
    display: inline-block;
    background: #1a1f35;
    color: #5c6bc0;
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: 0.75rem;
    padding: 2px 8px;
    border-radius: 4px;
    margin-right: 6px;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<div class="page-title">Mercado Global</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Ventas globales · Plataformas · Géneros · Publishers</div>', unsafe_allow_html=True)

# ── Top 10 juegos ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Ranking</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Top 10 juegos por ventas globales</div>', unsafe_allow_html=True)

df_top10 = return_Top10_global_Sales().reset_index(drop=True)
df_top10.index = df_top10.index + 1

fig_top10 = go.Figure()
fig_top10.add_trace(go.Bar(
    x=df_top10["Global_Sales"],
    y=df_top10["Name"],
    orientation='h',
    marker=dict(
        color=df_top10["Global_Sales"],
        colorscale=[[0, "#1a1f35"], [0.4, "#3949ab"], [1, "#7986cb"]],
        line=dict(width=0)
    ),
    text=[f"{v:.1f}M" for v in df_top10["Global_Sales"]],
    textposition='outside',
    textfont=dict(color="#8b8fa8", size=12),
    hovertemplate="<b>%{y}</b><br>Ventas: %{x:.2f}M<extra></extra>"
))

fig_top10.update_layout(
    height=420,
    margin=dict(l=0, r=60, t=10, b=10),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
    yaxis=dict(
        autorange="reversed",
        tickfont=dict(color="#e8eaf0", size=13),
        tickprefix="  ",
    ),
    bargap=0.35,
)

st.plotly_chart(fig_top10, use_container_width=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Top Plataformas / Géneros / Publishers ────────────────────────────────────
st.markdown('<div class="section-label">Distribución</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Ventas por categoría</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

COLOR_SEQ = ["#3949ab", "#5c6bc0", "#7986cb", "#9fa8da", "#c5cae9",
             "#283593", "#1a237e", "#3d5afe", "#536dfe", "#8c9eff"]

def make_bar(df_series, label):
    df = df_series.reset_index()
    df.columns = ["categoria", "ventas"]
    df = df.head(10)
    fig = px.bar(
        df, x="ventas", y="categoria", orientation='h',
        color="ventas",
        color_continuous_scale=[[0, "#1a1f35"], [0.5, "#3949ab"], [1, "#7986cb"]],
        labels={"ventas": "Ventas (M)", "categoria": ""},
    )
    fig.update_traces(
        texttemplate="%{x:.1f}M", textposition="outside",
        textfont=dict(color="#8b8fa8", size=11),
        hovertemplate=f"<b>%{{y}}</b><br>{label}: %{{x:.2f}}M<extra></extra>"
    )
    fig.update_layout(
        height=340,
        margin=dict(l=0, r=50, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        coloraxis_showscale=False,
        xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
        yaxis=dict(
            autorange="reversed",
            tickfont=dict(color="#e8eaf0", size=12),
        ),
        bargap=0.3,
    )
    return fig

with col1:
    st.markdown('<div class="section-label">Plataformas</div>', unsafe_allow_html=True)
    st.plotly_chart(make_bar(return_Top_Bloq1("Platform"), "Plataforma"), use_container_width=True)

with col2:
    st.markdown('<div class="section-label">Géneros</div>', unsafe_allow_html=True)
    st.plotly_chart(make_bar(return_Top_Bloq1("Genre"), "Género"), use_container_width=True)

with col3:
    st.markdown('<div class="section-label">Publishers</div>', unsafe_allow_html=True)
    st.plotly_chart(make_bar(return_Top_Bloq1("Publisher"), "Publisher"), use_container_width=True)