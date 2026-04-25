import streamlit as st

st.set_page_config(page_title="Projects", layout="wide")

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

/* CONTAINER */
.block-container {
    padding-top: 3rem;
    max-width: 900px;
    margin: auto;
}

/* CARD STYLE (MATCH ALL PAGES) */
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
st.title("💼 Projects")

# ---------------- MAIN PROJECT ----------------
st.markdown("""
<div class="card">
<h3>🌐 Portfolio App</h3>
<p>Multipage Streamlit portfolio website</p>
</div>
""", unsafe_allow_html=True)

# ---------------- OTHER PROJECTS ----------------
st.markdown("""
<div class="card">
<h3>🧩 Other Projects</h3>
<p>✔ Simple Python apps<br>
✔ UI practice projects<br>
✔ School systems</p>
</div>
""", unsafe_allow_html=True)
