import streamlit as st

st.set_page_config(page_title="About", layout="wide")

# ---------------- STYLE (SAME DESIGN SYSTEM) ----------------
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
    padding-top: 3.5rem;
    padding-bottom: 3.5rem;
}

/* TEXT */
html, body, .stApp, p, div, span, label {
    color: #111111 !important;
    font-weight: 700 !important;
    line-height: 1.7;
}

/* HEADINGS */
h1, h2, h3 {
    color: #000000 !important;
    font-weight: 900 !important;
}

/* TITLE */
.top-title {
    text-align: center;
    font-size: 38px;
    font-weight: 900;
    color: white;
    margin-bottom: 40px;
}

/* CARD */
.card {
    background: rgba(255,255,255,0.85);
    padding: 22px;
    border-radius: 15px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.1);
    margin-bottom: 18px;
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
I am Rea May Villanueva, a Computer Science student passionate about building clean, functional, and user-friendly web applications.
I enjoy turning ideas into real systems using Python and Streamlit.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>🎓 Education</h3>
<p>
Bachelor of Science in Computer Science (3rd Year)
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>🚀 Developer Mindset</h3>
<p>
I focus on simplicity, usability, and clean UI design. I believe good software should not only work — it should feel easy to use.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>🎯 Goals</h3>
<p>
✔ Become a full-stack developer<br>
✔ Improve UI/UX design skills<br>
✔ Build real-world web applications
</p>
</div>
""", unsafe_allow_html=True)
