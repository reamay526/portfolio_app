import streamlit as st

st.set_page_config(page_title="About", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
    font-family: Arial;
}

/* TEXT COLOR */
html, body, .stApp {
    color: #000000 !important;
}

/* CENTER CONTAINER */
.block-container {
    padding-top: 3rem;
    max-width: 900px;
    margin: auto;
}

/* CARD STYLE (MATCH HOME FEEL) */
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
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("📘 About Me")

# ---------------- CARD 1 ----------------
st.markdown("""
<div class="card">
<p>I enjoy learning programming and building simple applications.</p>
</div>
""", unsafe_allow_html=True)

# ---------------- CARD 2 ----------------
st.markdown("""
<div class="card">
<h3>🎓 Education</h3>
<p>BS Computer Science</p>
</div>
""", unsafe_allow_html=True)

# ---------------- CARD 3 ----------------
st.markdown("""
<div class="card">
<h3>🎯 Goals</h3>
<p>✔ Improve coding skills<br>
✔ Build useful projects<br>
✔ Become a full-stack developer</p>
</div>
""", unsafe_allow_html=True)
