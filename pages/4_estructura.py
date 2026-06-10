import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from src.analysis import return_Market_Distribution, return_concentracion_top10

st.set_page_config(page_title="Estructura del Mercado", layout="wide")

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
    margin-bottom: 2rem;
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
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<div class="page-title">Estructura del Mercado</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Distribución de ventas por tramo · Concentración top 10 vs el resto</div>', unsafe_allow_html=True)

# ── Concentración top 10 ──────────────────────────────────────────────────────
st.markdown('<div class="section-label">Concentración</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Top 10 juegos vs el resto del mercado</div>', unsafe_allow_html=True)

df_conc = return_concentracion_top10()

col1, col2 = st.columns([1, 1])

with col1:
    fig_donut = go.Figure(data=[go.Pie(
        labels=df_conc["grupo"],
        values=df_conc["ventas_M"],
        hole=0.6,
        marker=dict(colors=["#5c6bc0", "#1a1f35"]),
        textinfo="label+percent",
        textfont=dict(color="#e8eaf0", size=13),
        hovertemplate="<b>%{label}</b><br>Ventas: %{value:.0f}M<br>%{percent}<extra></extra>"
    )])
    fig_donut.update_layout(
        height=320,
        margin=dict(l=0, r=0, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
    )
    st.plotly_chart(fig_donut, use_container_width=True)

with col2:
    st.dataframe(
        df_conc,
        use_container_width=True,
        hide_index=True,
    )

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Distribución por tramo ────────────────────────────────────────────────────
st.markdown('<div class="section-label">Distribución</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">¿Qué porcentaje de juegos concentra qué porcentaje de ventas?</div>', unsafe_allow_html=True)

df_dist = return_Market_Distribution()

fig_dist = px.bar(
    df_dist,
    x="top_%",
    y="% del total",
    text="% del total",
    color="% del total",
    color_continuous_scale=[[0, "#1a1f35"], [0.5, "#3949ab"], [1, "#7986cb"]],
    labels={"top_%": "Top % de juegos", "% del total": "% de ventas globales"},
)
fig_dist.update_traces(
    texttemplate="%{y}%",
    textposition="outside",
    textfont=dict(color="#8b8fa8", size=12),
    hovertemplate="<b>Top %{x}% de juegos</b><br>Concentra el %{y}% de las ventas<extra></extra>"
)
fig_dist.update_layout(
    height=360,
    margin=dict(l=0, r=0, t=30, b=10),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    coloraxis_showscale=False,
    xaxis=dict(tickvals=df_dist["top_%"], ticktext=[f"Top {v}%" for v in df_dist["top_%"]], tickfont=dict(color="#e8eaf0")),
    yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
    bargap=0.3,
)
st.plotly_chart(fig_dist, use_container_width=True)