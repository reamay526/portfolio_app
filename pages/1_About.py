import streamlit as st

st.set_page_config(page_title="About", layout="wide")

# ---------------- STYLE (KEEP YOUR GLASS DESIGN) ----------------
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
    line-height: 1.6;
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
    margin-bottom: 25px;
}

/* GLASS CARD */
.card {
    background: rgba(255, 255, 255, 0.35);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    padding: 10px 14px;
    border-radius: 12px;
    box-shadow: 0 6px 15px rgba(0,0,0,0.08);
    margin-bottom: 10px;
    border: 1px solid rgba(255, 255, 255, 0.25);
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="top-title">📘 About Me</div>', unsafe_allow_html=True)

# ---------------- CONTENT (REVISED) ----------------

st.markdown("""
<div class="card">
<h3>👩‍💻 Profile</h3>
<p>
I am Rea May Villanueva, a Computer Science student focused on building modern, clean, and user-friendly web applications.
I enjoy transforming ideas into functional digital solutions using Python and Streamlit.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>🎓 Education</h3>
<p>
Bachelor of Science in Computer Science (3rd Year)<br>
Focused on software development, web technologies, and UI/UX design.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>🚀 Passion & Focus</h3>
<p>
I am passionate about designing simple yet effective user interfaces and building functional systems that solve real-world problems.
My focus is on web development, Python programming, and improving user experience design.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>🎯 Goals</h3>
<p>
✔ Become a professional full-stack developer<br>
✔ Master UI/UX and modern web design<br>
✔ Build real-world, impactful applications<br>
✔ Continuously improve programming skills
</p>
</div>
""", unsafe_allow_html=True)
