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

/* REMOVE TOP GAP */
[data-testid="stHeader"] {
    background: transparent !important;
}

/* CONTAINER */
.block-container {
    background: transparent !important;
    padding-top: 3rem;
    padding-bottom: 3rem;
}

/* TEXT IMPROVEMENT */
html, body, .stApp, p, div, span, label {
    color: #111 !important;
    font-size: 16px;
    line-height: 1.7;
}

/* HERO TITLE */
.top-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    margin-bottom: 20px;
    color: white;
    text-shadow: 2px 2px 10px rgba(0,0,0,0.3);
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

/* BUTTON */
div.stButton > button {
    background: linear-gradient(90deg, #00c6ff, #7f00ff) !important;
    color: white !important;
    border-radius: 25px;
    padding: 12px 24px;
    border: none;
    font-weight: 700;
    box-shadow: 0 6px 18px rgba(0, 198, 255, 0.35);
}

div.stButton > button:hover {
    transform: scale(1.05);
    transition: 0.2s ease-in-out;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO TITLE ----------------
st.markdown('<div class="top-title">👋 Welcome to My Portfolio</div>', unsafe_allow_html=True)

st.write("")

# ---------------- HERO SECTION ----------------
col1, col2 = st.columns([1, 2])

with col1:
    st.image("mayie.png", width=240)

    if st.button("🚀 Say Hello"):
        st.success("Hello! Welcome to my portfolio 👋")

with col2:
    st.markdown("""
    ### Rea May M. Villanueva

    🎓 **BS Computer Science (3rd Year)**  
    💻 **Aspiring Developer & UI Designer**  
    🌐 **Web Development Enthusiast**

    ---
    
    I am a Computer Science student passionate about building **clean, functional, and user-friendly applications**.  
    I enjoy transforming ideas into real systems using **Python and web technologies**.

    I continuously improve my skills in **programming, UI design, and system development**,  
    aiming to build efficient and meaningful digital solutions.
    """)

st.markdown("---")

# ---------------- QUICK HIGHLIGHTS ----------------
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    ### 🎯 Goal  
    Become a skilled and creative developer
    """)

with c2:
    st.markdown("""
    ### 🚀 Focus  
    Web development & UI design
    """)

with c3:
    st.markdown("""
    ### 🌱 Learning  
    Python • Streamlit • Frontend
    """)
