import streamlit as st

st.set_page_config(page_title="About", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #ff4fa3, #7a00ff);
    font-family: Arial, sans-serif;
}

/* HEADER */
[data-testid="stHeader"] {
    background: transparent !important;
}

/* CONTAINER */
.block-container {
    padding-top: 2.5rem;
    padding-bottom: 2.5rem;
}

/* TEXT */
html, body, .stApp, p, div, span, label {
    color: #111111 !important;
    font-weight: 700 !important;
    line-height: 1.5;
}

/* HEADINGS */
h1, h2, h3 {
    color: #000000 !important;
    font-weight: 900 !important;
    margin-bottom: 5px;
}

/* TITLE */
.top-title {
    text-align: center;
    font-size: 38px;
    font-weight: 900;
    color: white;
    margin-bottom: 25px;
}

/* CARD (VERY SMALL HEIGHT) */
.card {
    background: rgba(255,255,255,0.90);
    padding: 8px 14px;      /* 🔥 very small padding */
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    margin-bottom: 8px;     /* 🔥 tight spacing */
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

# ---------------- TITLE ----------------
st.markdown('<div class="top-title">📘 About Me</div>', unsafe_allow_html=True)

# ---------------- CONTENT ----------------

st.markdown("""
<div class="card">
<h3>👩‍💻 Who I Am</h3>
<p>
Rea May Villanueva — Computer Science student passionate about clean web apps using Python & Streamlit.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>🎓 Education</h3>
<p>
BS Computer Science (3rd Year)
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>🚀 Developer Mindset</h3>
<p>
I value simplicity, usability, and clean UI design.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>🎯 Goals</h3>
<p>
✔ Full-stack developer<br>
✔ UI/UX improvement<br>
✔ Real-world applications
</p>
</div>
""", unsafe_allow_html=True)
