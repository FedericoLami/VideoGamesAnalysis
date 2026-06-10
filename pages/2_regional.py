import streamlit as st
import plotly.express as px
from src.analysis import return_Top_Bloq2

st.set_page_config(page_title="Análisis Regional", layout="wide")

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
st.markdown('<div class="page-title">Análisis Regional</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Comparativa de ventas por región · Plataformas · Géneros · Publishers</div>', unsafe_allow_html=True)

# ── Selector de región ────────────────────────────────────────────────────────
region_map = {
    "Norteamérica (NA)": "NA_Sales",
    "Europa (EU)": "EU_Sales",
    "Japón (JP)": "JP_Sales",
    "Otras regiones": "Other_Sales",
}

region_label = st.selectbox("Seleccioná una región", list(region_map.keys()))
region_col = region_map[region_label]

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Gráficos ──────────────────────────────────────────────────────────────────
st.markdown(f'<div class="section-label">{region_label}</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Top 10 por categoría</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

def make_bar(series, label):
    df = series.reset_index()
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
        yaxis=dict(autorange="reversed", tickfont=dict(color="#e8eaf0", size=12)),
        bargap=0.3,
    )
    return fig

with col1:
    st.markdown('<div class="section-label">Plataformas</div>', unsafe_allow_html=True)
    st.plotly_chart(make_bar(return_Top_Bloq2("Platform", region_col), "Plataforma"), use_container_width=True)

with col2:
    st.markdown('<div class="section-label">Géneros</div>', unsafe_allow_html=True)
    st.plotly_chart(make_bar(return_Top_Bloq2("Genre", region_col), "Género"), use_container_width=True)

with col3:
    st.markdown('<div class="section-label">Publishers</div>', unsafe_allow_html=True)
    st.plotly_chart(make_bar(return_Top_Bloq2("Publisher", region_col), "Publisher"), use_container_width=True)