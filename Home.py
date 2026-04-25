import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
    color: #000000;
    font-family: Arial;
}

html, body, .stApp, p, div, span, label, h1, h2, h3 {
    color: #000000 !important;
}

h1{
    text-align: top center;
}
 h2, h3 {
    text-align: center;
}

.block-container {
    padding-top: 3rem;
    padding-bottom: 2rem;
}

.stButton > button {
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    left, right = st.columns([1, 2], vertical_alignment="center")

    with left:
        st.image("mayie.png", width=280)

    with right:
        st.markdown("## 👋 Welcome to My Portfolio")
        st.markdown("### Rea May M. Villanueva")
        st.write("🎓 BSCS 3B")
        st.write("💻 Aspiring Developer & Designer")
        st.write("🌐 Interested in Web Development")

        if st.button("🚀 Say Hello"):
            st.success("Hello! Thanks for visiting my portfolio 👋")

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
