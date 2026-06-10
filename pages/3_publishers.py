import streamlit as st
import plotly.express as px
from src.analysis import return_Top_Publishers, return_Top_Publisher_By_Genre

st.set_page_config(page_title="Publishers", layout="wide")

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
st.markdown('<div class="page-title">Publishers</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Top publishers por ventas globales · Publisher líder por género</div>', unsafe_allow_html=True)

# ── Top 3 Publishers ──────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Ranking</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Top 3 publishers por ventas globales</div>', unsafe_allow_html=True)

df_top = return_Top_Publishers().reset_index()
df_top.columns = ["Publisher", "Ventas"]

fig_top = px.bar(
    df_top, x="Ventas", y="Publisher", orientation='h',
    color="Ventas",
    color_continuous_scale=[[0, "#1a1f35"], [0.5, "#3949ab"], [1, "#7986cb"]],
    labels={"Ventas": "Ventas (M)", "Publisher": ""},
)
fig_top.update_traces(
    texttemplate="%{x:.1f}M", textposition="outside",
    textfont=dict(color="#8b8fa8", size=12),
    hovertemplate="<b>%{y}</b><br>Ventas: %{x:.2f}M<extra></extra>"
)
fig_top.update_layout(
    height=220,
    margin=dict(l=0, r=60, t=10, b=10),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    coloraxis_showscale=False,
    xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
    yaxis=dict(autorange="reversed", tickfont=dict(color="#e8eaf0", size=13)),
    bargap=0.35,
)
st.plotly_chart(fig_top, use_container_width=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Publisher líder por género ─────────────────────────────────────────────────
st.markdown('<div class="section-label">Por género</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Publisher líder en cada género</div>', unsafe_allow_html=True)

df_genre = return_Top_Publisher_By_Genre()[["Genre", "Publisher", "Global_Sales"]]
df_genre = df_genre.sort_values("Global_Sales", ascending=False)

fig_genre = px.bar(
    df_genre, x="Global_Sales", y="Genre", orientation='h',
    color="Global_Sales",
    color_continuous_scale=[[0, "#1a1f35"], [0.5, "#3949ab"], [1, "#7986cb"]],
    hover_data={"Publisher": True, "Global_Sales": ":.2f"},
    labels={"Global_Sales": "Ventas (M)", "Genre": ""},
    text="Publisher",
)
fig_genre.update_traces(
    textposition="inside",
    textfont=dict(color="#ffffff", size=11),
    hovertemplate="<b>%{y}</b><br>Publisher: %{customdata[0]}<br>Ventas: %{x:.2f}M<extra></extra>"
)
fig_genre.update_layout(
    height=480,
    margin=dict(l=0, r=20, t=10, b=10),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    coloraxis_showscale=False,
    xaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
    yaxis=dict(autorange="reversed", tickfont=dict(color="#e8eaf0", size=12)),
    bargap=0.3,
)
st.plotly_chart(fig_genre, use_container_width=True)