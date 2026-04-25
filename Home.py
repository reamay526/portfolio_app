import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #ff4fa3, #7a00ff);
    font-family: "Segoe UI", Arial, sans-serif;
}

/* REMOVE TOP BAR */
[data-testid="stHeader"] {
    background: transparent !important;
}

/* CONTAINER */
.block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
    max-width: 950px;
    margin: auto;
}

/* TEXT */
html, body, .stApp, p, div, span, label {
    color: #111 !important;
    font-size: 16px;
    line-height: 1.7;
}

/* HEADINGS */
h1, h2, h3 {
    color: white !important;
    text-align: center;
    font-weight: 700;
}

/* CARD */
.card {
    background: rgba(255,255,255,0.92);
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    text-align: center;
}

/* BUTTON */
div.stButton > button {
    background: linear-gradient(90deg, #00c6ff, #7f00ff) !important;
    color: white !important;
    border-radius: 25px;
    padding: 12px 24px;
    border: none;
    font-weight: 700;
}

div.stButton > button:hover {
    transform: scale(1.05);
    transition: 0.2s ease-in-out;
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

# ---------------- HERO TITLE ----------------
st.markdown("<h1>👋 Hi, I'm Rea May</h1>", unsafe_allow_html=True)
st.markdown("<h3>💻 Aspiring Developer | UI Designer | CS Student</h3>", unsafe_allow_html=True)

st.write("")

# ---------------- HERO SECTION ----------------
col1, col2 = st.columns([1, 2])

with col1:
    st.image("mayie.png", width=240)

    if st.button("🚀 Say Hello"):
        st.success("Thanks for visiting my portfolio 👋")

with col2:
    st.markdown("""
    <div class="card">
    <h3>Short Intro</h3>
    <p>
    I am a Computer Science student passionate about building clean and functional web applications.
    I enjoy turning ideas into real digital systems using Python and web technologies.
    </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- QUICK HIGHLIGHTS ----------------
st.markdown("---")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
    <h3>🎯 Goal</h3>
    <p>Become a skilled developer</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
    <h3>🚀 Focus</h3>
    <p>Web development & UI design</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
    <h3>🌱 Learning</h3>
    <p>Python • Streamlit • Frontend</p>
    </div>
    """, unsafe_allow_html=True)
