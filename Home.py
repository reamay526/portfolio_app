import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #3b1b5a, #ff4fa3, #7a00ff);
    font-family: Arial;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

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

# ---------------- PROFILE ----------------
col1, col2, col3 = st.columns([0.5, 3, 0.5])

with col2:

    left, right = st.columns([1.2, 2.8], gap="large")

    # ---------------- LEFT SIDE ----------------
    with left:
        st.image("mayie.png", width=220)

        # ✔ BUTTON + MESSAGE INLINE (SIDE BY SIDE)
        btn_col, msg_col = st.columns([1, 2])

        with btn_col:
            if st.button("🚀 Say Hello"):
                st.session_state.hello = not st.session_state.hello

        with msg_col:
            if st.session_state.hello:
                st.markdown("👋 Hi there! Glad you’re here — explore my portfolio.")

    # ---------------- RIGHT SIDE ----------------
    with right:
        st.markdown("### Rea May Villanueva")
        st.write("💻 Aspiring Developer & UI Designer")
        st.write("🎓 Computer Science Student (3rd Year)")

        st.write("""
I build clean and user-friendly web applications using Python and Streamlit.
I enjoy turning ideas into real working systems.
        """)

st.markdown("---")

# ---------------- HIGHLIGHTS ----------------
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### 🎯 Goal")
    st.write("Become a skilled developer")

with c2:
    st.markdown("### 🚀 Focus")
    st.write("Web apps & UI design")

with c3:
    st.markdown("### 🌱 Learning")
    st.write("Python • Streamlit • UI/UX")
