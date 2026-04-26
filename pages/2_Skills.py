import streamlit as st

st.set_page_config(page_title="Skills", layout="wide")

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

/* TEXT */
html, body, .stApp, p, div, span, label {
    color: #111111 !important;
    font-weight: 700 !important;
}

/* TITLE */
h1 {
    text-align: center;
    color: white !important;
    font-weight: 900 !important;
}

/* GLASS CARD (MATCH ABOUT PAGE) */
.card {
    background: rgba(255, 255, 255, 0.30);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 14px 18px;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.10);
    margin-bottom: 15px;
    border: 1px solid rgba(255, 255, 255, 0.25);
    text-align: center;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #3b1b5a, #7a00ff);
}

section[data-testid="stSidebar"] * {
    color: white !important;
    font-weight: 700 !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<h1>⚡ My Skills</h1>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>💻 Programming Skills</h3>
</div>
""", unsafe_allow_html=True)

st.write("Python")
st.progress(85)

st.write("HTML")
st.progress(88)

st.write("CSS")
st.progress(87)

st.markdown("""
<div class="card">
<h3>🛠 Development Tools</h3>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("✔ GitHub")

with col2:
    st.markdown("✔ VS Code")

with col3:
    st.markdown("✔ Streamlit")

st.markdown("""
<div class="card">
<h3>🚀 Focus Areas</h3>
<p>
Web Development • UI Design • Clean Code • Problem Solving
</p>
</div>
""", unsafe_allow_html=True)
