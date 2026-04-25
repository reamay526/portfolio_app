import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide")

st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #ff4fa3, #7a00ff);
    font-family: Arial;
}

/* REMOVE TOP WHITE GAP */
[data-testid="stHeader"] {
    background: transparent !important;
}

/* CONTAINER */
.block-container {
    background: transparent !important;
    padding-top: 3rem;
    padding-bottom: 3rem;
}

/* GLOBAL TEXT */
html, body, .stApp, p, div, span, label, h1, h2, h3 {
    color: #000000 !important;
}

/* TITLE */
.top-title {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 30px;
    color: white;
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

/* ✅ UPDATED BUTTON GRADIENT */
div.stButton > button {
    background: linear-gradient(90deg, #00c6ff, #7f00ff) !important;
    color: white !important;
    border-radius: 20px;
    padding: 12px 24px;
    border: none;
    font-weight: 700;
    box-shadow: 0 6px 18px rgba(0, 198, 255, 0.35);
}

div.stButton > button:hover {
    background: linear-gradient(90deg, #00e0ff, #9b2dff) !important;
    transform: scale(1.05);
    transition: 0.2s ease-in-out;
    box-shadow: 0 8px 22px rgba(0, 198, 255, 0.45);
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="top-title">👋 Welcome to My Portfolio</div>', unsafe_allow_html=True)

# ---------------- PROFILE ----------------
col1, col2, col3 = st.columns([0.5, 3, 0.5])

with col2:

    left, right = st.columns([1.5, 2.5], gap="large")

    with left:
        st.image("mayie.png", width=250)

    with right:
st.markdown("### Rea May M. Villanueva")
st.write("🎓 BS Computer Science Student (3rd Year)")
st.write("💻 Aspiring Full-Stack Developer & UI Designer")
st.write("🌐 Passionate about building clean, user-friendly web applications")

st.write("""
I am currently improving my skills in Python, web development, and UI design.  
I enjoy turning ideas into functional and visually appealing applications.
""")

if st.button("🚀 Say Hello"):
    st.success("Hello! Welcome to my portfolio — feel free to explore my work 👋") 

st.markdown("---")

# ---------------- INFO ----------------
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### 🎯 Goal")
    st.write("To become a skilled and creative developer")

with c2:
    st.markdown("### 🚀 Focus")
    st.write("Building clean and functional web applications")

with c3:
    st.markdown("### 🌱 Learning")
    st.write("Improving Python, UI design, and web development skills")
