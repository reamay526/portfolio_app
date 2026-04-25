import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #ff4fa3, #7a00ff);
    font-family: Arial;
}

/* REMOVE TOP WHITE SPACE */
[data-testid="stHeader"] {
    background: transparent !important;
}

/* MAIN CONTAINER */
.block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
}

/* TEXT */
html, body, .stApp, p, div, span, label, h1, h2, h3 {
    color: #000000 !important;
}

/* TITLE */
.top-title {
    text-align: center;
    font-size: 38px;
    font-weight: 800;
    color: white;
    margin-bottom: 30px;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #3b1b5a, #7a00ff);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* BUTTON */
div.stButton > button {
    background: linear-gradient(90deg, #00c6ff, #7f00ff) !important;
    color: white !important;
    border-radius: 20px;
    padding: 10px 18px;
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

# ---------------- TITLE ----------------
st.markdown('<div class="top-title">👋 Welcome to My Portfolio</div>', unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "hello" not in st.session_state:
    st.session_state.hello = False

# ---------------- PROFILE ----------------
col1, col2, col3 = st.columns([0.5, 3, 0.5])

with col2:
    left, right = st.columns([1.2, 2.8], gap="large")

    # ---------------- IMAGE + BUTTON ----------------
    with left:
        st.image("mayie.png", width=220)

        btn, msg = st.columns([1, 3])

        with btn:
            if st.button("🚀 Say Hello"):
                st.session_state.hello = not st.session_state.hello

        with msg:
            if st.session_state.hello:
                st.write("👋 Hi there! Glad you’re here — feel free to explore my projects.")

    # ---------------- INFO ----------------
    with right:
        st.markdown("### Rea May M. Villanueva")

        st.write("🎓 BS Computer Science (3rd Year)")
        st.write("💻 Aspiring Developer & UI Designer")
        st.write("🌐 Interested in Web Development")

        st.write("""
I am a Computer Science student passionate about building clean and user-friendly digital solutions.
I enjoy turning ideas into functional applications using Python and web technologies.

I am continuously improving my skills in programming, interface design, and system development.
        """)

st.markdown("---")

# ---------------- HIGHLIGHTS ----------------
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### 🎯 Goal")
    st.write("Become a skilled and creative developer")

with c2:
    st.markdown("### 🚀 Focus")
    st.write("Build clean and functional web applications")

with c3:
    st.markdown("### 🌱 Learning")
    st.write("Improve Python, UI design, and web development")
