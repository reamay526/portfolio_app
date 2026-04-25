import streamlit as st

st.set_page_config(page_title="Projects", layout="wide")

st.markdown("""
<style>

/* BACKGROUND (FIXED + CLEAN) */
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #ff4fa3, #7a00ff);
    font-family: Arial;
}

/* REMOVE WHITE HEADER + GAP */
[data-testid="stHeader"] {
    background: transparent !important;
}

.block-container {
    background: transparent !important;
    padding-top: 3rem;
    max-width: 900px;
    margin: auto;
}

/* TEXT COLOR */
html, body, .stApp {
    color: #000000 !important;
}

/* CARD STYLE */
.card {
    background: rgba(255,255,255,0.85);
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

/* SIDEBAR */
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
st.title("💼 Projects")

# ---------------- PROJECT 1 ----------------
st.markdown("""
<div class="card">
<h3>🌐 Portfolio App</h3>
<p>Multipage Streamlit portfolio website</p>
</div>
""", unsafe_allow_html=True)

# ---------------- PROJECT 2 ----------------
st.markdown("""
<div class="card">
<h3>🧩 Other Projects</h3>
<p>✔ Simple Python apps<br>
✔ UI practice projects<br>
✔ School systems</p>
</div>
""", unsafe_allow_html=True)
