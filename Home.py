import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide")

st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #ff4fa3, #7a00ff);
    font-family: Arial;
}

/* REMOVE TOP BAR */
[data-testid="stHeader"] {
    background: transparent !important;
}

/* CONTAINER */
.block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
}

/* TEXT */
html, body, .stApp, p, div, span, label, h1, h2, h3 {
    color: #000000 !important;
}

/* HERO TITLE */
.hero-title {
    text-align: center;
    font-size: 42px;
    font-weight: 800;
    color: white;
    margin-bottom: 5px;
}

.hero-role {
    text-align: center;
    font-size: 18px;
    color: #f2f2f2;
    margin-bottom: 25px;
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
    width: 100%;
}

div.stButton > button:hover {
    transform: scale(1.05);
    transition: 0.2s ease-in-out;
}

/* CARD */
.card {
    background: rgba(255,255,255,0.85);
    padding: 15px;
    border-radius: 15px;
    text-align: center;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO TITLE ----------------
st.markdown('<div class="hero-title">Rea May M. Villanueva</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-role">Aspiring Developer • UI Designer • BS Computer Science</div>', unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    left, right = st.columns([1, 2], gap="large")

    with left:
        st.image("mayie.png", width=220)

        # ---------------- TOGGLE BUTTON ----------------
        if "hello_clicked" not in st.session_state:
            st.session_state.hello_clicked = False

        if st.button("🚀 Say Hello"):
            st.session_state.hello_clicked = not st.session_state.hello_clicked

        if st.session_state.hello_clicked:
            st.markdown("""
            <div style="
                background: white;
                padding: 12px;
                border-radius: 12px;
                text-align: center;
                margin-top: 10px;
                box-shadow: 0 6px 15px rgba(0,0,0,0.15);
            ">
                👋 Hello! Welcome to my portfolio
            </div>
            """, unsafe_allow_html=True)

    with right:
        st.markdown("""
        ### 👋 About Me

        I am a Computer Science student passionate about building clean, functional, and user-friendly applications.

        I enjoy turning ideas into real systems using Python and web development tools.
        """)

# ---------------- QUICK HIGHLIGHTS ----------------
st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
    🎯 Goal<br>
    Become a skilled developer
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
    🚀 Focus<br>
    Clean web applications
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
    🌱 Learning<br>
    Python • UI Design • Web Dev
    </div>
    """, unsafe_allow_html=True)
