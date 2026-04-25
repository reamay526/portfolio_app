import streamlit as st

st.set_page_config(page_title="About", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #3b1b5a, #ff4fa3, #7a00ff);
}

.block-container {
    padding-top: 2.5rem;
    padding-bottom: 2.5rem;
}

/* Title */
.top-title {
    text-align: center;
    font-size: 38px;
    font-weight: 900;
    color: white;
    margin-bottom: 25px;
}

/* Card */
.card {
    background: rgba(255, 255, 255, 0.25);
    backdrop-filter: blur(10px);
    padding: 16px;
    border-radius: 14px;
    margin-bottom: 15px;
    border: 1px solid rgba(255,255,255,0.2);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #3b1b5a, #7a00ff);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="top-title">📘 About Me</div>', unsafe_allow_html=True)

# ---------------- PROFILE ----------------
st.markdown("""
<div class="card">
<h3>👩‍💻 Profile</h3>
<p>
BS Computer Science student (3B) at DEBESMSCAT.
Passionate about building clean, functional, and user-friendly web applications.
</p>
</div>
""", unsafe_allow_html=True)

# ---------------- EDUCATION ----------------
st.markdown("""
<div class="card">
<h3>🎓 Education</h3>
<p>Bachelor of Science in Computer Science</p>
<p>3rd Year – Section 3B</p>
<p>DEBESMSCAT</p>
</div>
""", unsafe_allow_html=True)

# ---------------- SKILLS ----------------
st.markdown("""
<div class="card">
<h3>💻 Skills</h3>
<p>HTML • CSS • Python • Java • Git • Streamlit</p>
</div>
""", unsafe_allow_html=True)

# ---------------- INTERESTS ----------------
st.markdown("""
<div class="card">
<h3>🚀 Interests</h3>
<p>Web development, UI/UX design, and interactive applications.</p>
</div>
""", unsafe_allow_html=True)

# ---------------- INTERACTIVE SECTION (FIX FOR REQUIREMENT) ----------------
st.markdown("## 🎯 Quick Interaction")

focus = st.selectbox(
    "What do you want to know about me?",
    ["Skills", "Goals", "Projects Interest"]
)

if focus == "Skills":
    st.info("I focus on Python, Streamlit, and frontend basics.")
elif focus == "Goals":
    st.success("My goal is to become a full-stack developer.")
else:
    st.warning("I aim to build real-world applications and portfolios.")

# ---------------- GOALS ----------------
st.markdown("""
<div class="card">
<h3>🎯 Goals</h3>
<p>✔ Become a full-stack developer<br>
✔ Improve UI/UX design skills<br>
✔ Build real-world applications</p>
</div>
""", unsafe_allow_html=True)
