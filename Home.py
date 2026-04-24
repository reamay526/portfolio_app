import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
    color: #000000;
    font-family: Arial;
}

.block-container {
    padding-top: 3rem;
    padding-bottom: 2rem;
}

h1, h2, h3 {
    text-align: center;
    color: #000000;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2], gap="large")

with col1:
    st.image("mayie.png", width=220)

with col2:
    st.markdown("## 👋 Welcome to My Portfolio")
    st.markdown("### Rea May M. Villanueva")
    st.write("🎓 BSCS 3B")
    st.write("💻 Aspiring Developer & Designer")
    st.write("🌐 Interested in Web Development")

    st.button("🚀 Say Hello")
    
st.markdown("---")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### 👩‍💻 About")
    st.info("Passionate about building clean and useful applications")

with c2:
    st.markdown("### 🛠 Skills")
    st.success("Python • HTML • CSS")

with c3:
    st.markdown("### 📬 Contact")
    st.warning("Open for collaboration")
