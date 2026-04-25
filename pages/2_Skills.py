import streamlit as st

st.set_page_config(page_title="Skills", layout="wide")

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

/* CARD STYLE (MATCH HOME + ABOUT) */
.card {
    background: rgba(255,255,255,0.80);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    text-align: center;
}

/* CENTER HEADINGS */
h1, h2, h3 {
    text-align: center;
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
