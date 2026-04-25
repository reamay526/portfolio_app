import streamlit as st

st.set_page_config(page_title="Skills", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
    font-family: Arial;
}

/* MAIN TEXT COLOR (SAFE) */
html, body, .stApp {
    color: #000000 !important;
}

/* CONTAINER */
.block-container {
    padding-top: 3rem;
    max-width: 900px;
    margin: auto;
}

/* CARD STYLE */
.card {
    background: rgba(255,255,255,0.80);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    text-align: center;
}

/* HEADINGS */
h1, h2, h3 {
    text-align: center;
}

/* SIDEBAR (SAFE FIX) */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #3b1b5a, #7a00ff);
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] div {
    color: white !important;
    font-weight: 500;
}

section[data-testid="stSidebar"] div:hover {
    background-color: rgba(255,255,255,0.15);
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("⚡ Skills")

# ---------------- SKILLS CARD ----------------
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

# ---------------- TOOLS CARD ----------------
st.markdown("""
<div class="card">
<h3>🛠 Tools</h3>
<p>GitHub<br>VS Code<br>Streamlit</p>
</div>
""", unsafe_allow_html=True)
