import streamlit as st

st.set_page_config(page_title="About", layout="wide")

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

/* GLASS CARD (SOFTER + CLEANER) */
.card {
    background: rgba(255, 255, 255, 0.28);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 14px 18px;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.10);
    margin-bottom: 15px;
    border: 1px solid rgba(255, 255, 255, 0.25);
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

st.markdown('<div class="top-title">📘 About Me</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>👩‍💻 Profile</h3>
<p>
I am a BS Computer Science student (3B) at DEBESMSCAT.
I am passionate about software development and creating clean, functional, and user-friendly web applications.
I enjoy turning ideas into real digital solutions using modern technologies.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>🎓 Education</h3>
<p>
Bachelor of Science in Computer Science<br>
3rd Year – Section 3B<br>
DEBESMSCAT
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>💻 Technical Background</h3>
<p>
HTML • CSS • Python • Java • GitHub • VS Code • Streamlit
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>🚀 Interests</h3>
<p>
Focused on web development, UI/UX design, and building interactive applications.
I enjoy learning how systems work and how to improve user experience through clean design.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h3>🎯 Goals</h3>
<p>
✔ Become a professional full-stack developer<br>
✔ Improve UI/UX and web development skills<br>
✔ Build real-world and impactful applications<br>
✔ Strengthen problem-solving and programming skills
</p>
</div>
""", unsafe_allow_html=True)
