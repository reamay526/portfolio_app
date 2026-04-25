import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide")

st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
    font-family: Arial;
}

/* FORCE BLACK TEXT */
html, body, .stApp, p, div, span, label, h1, h2, h3 {
    color: #000000 !important;
}

/* SIDEBAR VISIBILITY FIX */
section[data-testid="stSidebar"] {
    background-color: rgba(255,255,255,0.95);
    color: black !important;
}

/* SIDEBAR TEXT */
section[data-testid="stSidebar"] * {
    color: black !important;
}

/* BUTTON STYLE (VISIBLE) */
.stButton > button {
    background-color: #3b1b5a;
    color: white !important;
    border-radius: 10px;
    padding: 8px 16px;
    border: none;
}

.stButton > button:hover {
    background-color: #ff4fa3;
    color: white;
}

/* SPACING */
.block-container {
    padding-top: 3rem;
    padding-bottom: 2rem;
}

</style>
""", unsafe_allow_html=True)

# CENTER LAYOUT
col1, col2, col3 = st.columns([1,2,1])

with col2:

    left, right = st.columns([1,2], vertical_alignment="center")

    with left:
        st.image("mayie.png", width=260)  # BIGGER IMAGE

    with right:
        st.markdown("## 👋 Welcome to My Portfolio")  # ONE LINE CLEAN
        st.markdown("### Rea May M. Villanueva")
        st.write("🎓 BSCS 3B")
        st.write("💻 Aspiring Developer & Designer")
        st.write("🌐 Interested in Web Development")

        if st.button("🚀 Say Hello"):
            st.success("Hello! Thanks for visiting my portfolio 👋")

# SPACING
st.markdown("---")

# LOWER SECTION
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
