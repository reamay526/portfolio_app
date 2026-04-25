import streamlit as st

st.set_page_config(page_title="About", layout="wide")

st.markdown("""
<style>

/* BACKGROUND FIX */
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #ff4fa3, #7a00ff);
    font-family: Arial;
}

/* REMOVE TOP WHITE BAR */
[data-testid="stHeader"] {
    background: transparent !important;
}

/* CONTAINER */
.block-container {
    background: transparent !important;
    padding-top: 3rem;
    max-width: 900px;
    margin: auto;
}

/* TEXT */
html, body, .stApp {
    color: #000000 !important;
}

/* CARD STYLE */
.card {
    background: rgba(255,255,255,0.88);
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

section[data-testid="stSidebar"] * {
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
st.title("📘 About Me")

# ---------------- INTRO CARD ----------------
st.markdown("""
<div class="card">
<h3>👋 Hello, I'm Rea May</h3>
<p>
A passionate Computer Science student who enjoys building clean, functional, and user-friendly applications.
I love turning ideas into real systems using code and creativity.
</p>
</div>
""", unsafe_allow_html=True)

# ---------------- EDUCATION ----------------
st.markdown("""
<div class="card">
<h3>🎓 Education</h3>
<p>
Bachelor of Science in Computer Science<br>
3rd Year College Student<br><br>
Focused on software development, web technologies, and UI/UX design.
</p>
</div>
""", unsafe_allow_html=True)

# ---------------- SKILLS SNAPSHOT ----------------
st.markdown("""
<div class="card">
<h3>💡 What I Do</h3>
<p>
✔ Build web applications using Python & Streamlit<br>
✔ Design simple and clean user interfaces<br>
✔ Practice front-end development (HTML/CSS)<br>
✔ Develop school and personal projects
</p>
</div>
""", unsafe_allow_html=True)

# ---------------- GOALS ----------------
st.markdown("""
<div class="card">
<h3>🎯 Goals</h3>
<p>
✔ Become a full-stack developer<br>
✔ Improve UI/UX design skills<br>
✔ Build real-world applications<br>
✔ Gain internship experience in tech industry
</p>
</div>
""", unsafe_allow_html=True)

# ---------------- PERSONALITY / BIO ----------------
st.markdown("""
<div class="card">
<h3>🚀 Developer Mindset</h3>
<p>
I believe in continuous learning and improvement.
Every project I build helps me grow my skills in problem-solving, creativity, and logic.
</p>
</div>
""", unsafe_allow_html=True)
