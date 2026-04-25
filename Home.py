import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
    font-family: Arial;
}

html, body, .stApp, p, div, span, label, h1, h2, h3 {
    color: #000000 !important;
}

/* CENTER TITLE */
.top-title {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 30px;
}

/* SIDEBAR VISIBILITY FIX */
section[data-testid="stSidebar"] {
    background-color: rgba(255,255,255,0.95);
    color: black !important;
}

/* SIDEBAR TEXT */
section[data-testid="stSidebar"] * {
    color: black !important;

/* BUTTON PREMIUM LOOK */
.stButton > button {
    background: linear-gradient(90deg, #3b1b5a, #ff4fa3);
    color: white !important;
    border-radius: 20px;
    padding: 10px 20px;
    border: none;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.05);
    opacity: 0.9;

.block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="top-title">👋 Welcome to My Portfolio</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.5, 3, 0.5])

with col2:

    left, right = st.columns([1.5, 2.5], gap="large")

    with left:
        st.image("mayie.png", width=250)

    with right:
        st.markdown("### Rea May M. Villanueva")

        st.write("🎓 BSCS 3B")
        st.write("💻 Aspiring Developer & Designer")
        st.write("🌐 Interested in Web Development")

        st.write("")
        st.write("")

        if st.button("🚀 Say Hello"):
            st.success("Hello! Thanks for visiting my portfolio 👋")

st.markdown("---")

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
