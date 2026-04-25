import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide")

st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
    font-family: Arial;
}

/* ALL TEXT BLACK */
html, body, .stApp, p, div, span, label, h1, h2, h3 {
    color: #000000 !important;
}

/* SIDEBAR CLEAN */
section[data-testid="stSidebar"] {
    background-color: rgba(255,255,255,0.95);
}
section[data-testid="stSidebar"] * {
    color: black !important;
}

/* TITLE IMPROVEMENT */
h2 {
    font-size: 32px;
    font-weight: bold;
}

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
}

/* SPACING */
.block-container {
    padding-top: 4rem;
    padding-bottom: 3rem;
}

</style>
""", unsafe_allow_html=True)

# MAIN CENTER
col1, col2, col3 = st.columns([1,2,1])

with col2:

    left, right = st.columns([1,2], vertical_alignment="center")

    with left:
        st.image("mayie.png", width=280)

    with right:
        st.markdown("## 👋 Welcome to My Portfolio")
        st.markdown("### Rea May M. Villanueva")

        st.write("🎓 BSCS 3B")
        st.write("💻 Aspiring Developer & Designer")
        st.write("🌐 Interested in Web Development")

        st.write("")  # spacing

        if st.button("🚀 Say Hello"):
            st.success("Hello! Thanks for visiting my portfolio 👋")

# SPACE
st.markdown("")

# SOFT SECTION (NO HARD BOXES, JUST CLEAN SPACING)
c1, c2, c3 = st.columns(3, gap="large")

with c1:
    st.markdown("### 🎯 Goal")
    st.caption("To become a skilled and creative developer")

with c2:
    st.markdown("### 🚀 Focus")
    st.caption("Building clean and functional web applications")

with c3:
    st.markdown("### 🌱 Learning")
    st.caption("Improving Python, UI design, and web development skills")
