import streamlit as st

st.set_page_config(page_title="Análisis de Videojuegos", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Space+Grotesk:wght@500;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0f1117;
    color: #e8eaf0;
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 3rem;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: -1px;
    margin-bottom: 0.4rem;
}

.hero-subtitle {
    font-size: 1rem;
    color: #8b8fa8;
    margin-bottom: 2.5rem;
}

.metric-card {
    background: #13161f;
    border: 1px solid #1e2130;
    border-radius: 12px;
    padding: 1.3rem 1.6rem;
    margin-bottom: 1rem;
    min-height: 110px;
}

.metric-label {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #5c6bc0;
    margin-bottom: 0.4rem;
}

.metric-value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    color: #ffffff;
}

.metric-sub {
    font-size: 0.78rem;
    color: #8b8fa8;
    margin-top: 0.2rem;
}

.divider {
    border: none;
    border-top: 1px solid #1e2130;
    margin: 2rem 0;
}

.section-label {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 2.5px;
    text-transform: uppercase;
    color: #5c6bc0;
    margin-bottom: 0.3rem;
}

.section-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 1.2rem;
}

.nav-card {
    background: #13161f;
    border: 1px solid #1e2130;
    border-radius: 12px;
    padding: 1.3rem 1.6rem;
    min-height: 100px;
}

.nav-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.95rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 0.4rem;
    white-space: nowrap;
}

.nav-desc {
    font-size: 0.82rem;
    color: #8b8fa8;
    line-height: 1.5;
}
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown('<div class="hero-title">Análisis de Videojuegos</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">16.598 juegos · 31 plataformas · 4 regiones · datos hasta 2016</div>', unsafe_allow_html=True)

# ── Métricas: 3 columnas x 2 filas ───────────────────────────────────────────
row1 = st.columns(3)
row2 = st.columns(3)

metrics_row1 = [
    ("Juegos", "16.598", "en el dataset"),
    ("Ventas globales", "8.920M", "unidades vendidas"),
    ("Año pico", "2009", "más lanzamientos"),
]

metrics_row2 = [
    ("Juego #1", "Wii Sports", "82.7M unidades"),
    ("Publisher top", "Nintendo", "por ventas globales"),
    ("Género top", "Action", "por ventas globales"),
]

for col, (label, value, sub) in zip(row1, metrics_row1):
    with col:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
                <div class="metric-sub">{sub}</div>
            </div>
        """, unsafe_allow_html=True)

for col, (label, value, sub) in zip(row2, metrics_row2):
    with col:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
                <div class="metric-sub">{sub}</div>
            </div>
        """, unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Navegación ────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Explorar</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Secciones del análisis</div>', unsafe_allow_html=True)

nav_items = [
    ("🌍 Mercado Global", "Top 10 juegos, plataformas, géneros y publishers a nivel mundial."),
    ("📍 Análisis Regional", "Comparativa de ventas en NA, EU, JP y otras regiones."),
    ("🏢 Publishers", "Top publishers y qué género domina cada uno."),
    ("📊 Estructura", "Distribución de ventas y concentración del mercado."),
]

nav_cols = st.columns(4)
for col, (title, desc) in zip(nav_cols, nav_items):
    with col:
        st.markdown(f"""
            <div class="nav-card">
                <div class="nav-title">{title}</div>
                <div class="nav-desc">{desc}</div>
            </div>
        """, unsafe_allow_html=True)