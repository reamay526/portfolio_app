import streamlit as st

st.set_page_config(page_title="Projects", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #3b1b5a, #ff4fa3, #7a00ff);
    font-family: Arial, sans-serif;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

.block-container {
    padding-top: 2.5rem;
    padding-bottom: 2.5rem;
}

html, body, .stApp, p, div, span, label {
    color: #111111 !important;
    font-weight: 700 !important;
}

h1 {
    text-align: center;
    color: white !important;
    font-weight: 900 !important;
}

.card {
    background: rgba(255, 255, 255, 0.30);
    backdrop-filter: blur(10px);
    padding: 18px;
    border-radius: 14px;
    margin-bottom: 15px;
    text-align: center;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #3b1b5a, #7a00ff);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1>💼 My Projects</h1>", unsafe_allow_html=True)

# ---------------- PROJECT GRID ----------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <h3>🌐 Portfolio App</h3>
    <p>Streamlit Multipage Portfolio</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
    <h3>🧮 Calculator App</h
