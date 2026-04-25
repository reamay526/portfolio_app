import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide")

# ---------------- STYLE ----------------
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

/* GLOBAL TEXT */
html, body, .stApp, p, div, span, label {
    color: #111111 !important;
    font-weight: 700 !important;
    line-height: 1.7;
}

/* TITLE */
.top-title {
    text-align: center;
    font-size: 38px;
    font-weight: 900;
    color: white;
    margin-bottom: 40px;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #3b1b5a, #7a00ff);
}

section[data-testid="stSidebar"] * {
    color: white !important;
    font-weight: 700 !important;
}

/* BUTTON */
div.stButton > button {
    background: linear-gradient(90deg, #00c6ff, #7f00ff) !important;
    color: white !important;
    border-radius: 20px;
    padding: 10px 18px;
    border: none;
    font-weight: 800 !important;
    width: 100%;
}

div.stButton > button:hover {
    transform: scale(1.05);
    transition: 0.2s ease-in-out;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="top-title">👋 Welcome to My Portfolio</div>', unsafe_allow_html=True)

# ---------------- STATE ----------------
if "hello" not in st.session_state:
    st.session_state.hello = False

# ---------------- HERO SECTION ----------------
col1, col2, col3 = st.columns([0.5, 3, 0.5])

with col2:

    left, right = st.columns([1.2, 2.8], gap="large")

    # LEFT SIDE
    with left:
        st.image("mayie.png", width=220)

        if st.button("🚀 Say Hello"):
            st.session_state.hello = not st.session_state.hello

        if st.session_state.hello:
            st.success("👋 Hi there! Glad you’re here — explore my portfolio.")

    # RIGHT SIDE (NAME BIGGER HERE)
    with right:

        st.markdown("""
        <h1 style="
            font-size: 48px;
            font-weight: 900;
            margin-bottom: 10px;
            color: #000000;
        ">
        Rea May Villanueva
        </h1>
        """, unsafe_allow_html=True)

        st.write("🎓 Computer Science Student (3rd Year)")
        st.write("💻 Aspiring Developer & UI Designer")

        st.write("""
I build clean and user-friendly web applications using Python and Streamlit.
        """)

# ---------------- FOOTER ----------------
st.markdown("---")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### ⚡ Strength")
    st.write("Clean & simple UI design")

with c2:
    st.markdown("### 🚀 Focus")
    st.write("Web app development")

with c3:
    st.markdown("### 🌱 Growth")
    st.write("Python • Streamlit • UI/UX")
