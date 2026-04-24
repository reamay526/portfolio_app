import streamlit as st

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
    font-family: Arial;
}

html, body, .stApp {
    color: #000000 !important;
}

.block-container {
    padding-top: 3rem;
}
</style>
""", unsafe_allow_html=True)

st.title("Projects")

st.subheader("Portfolio App")
st.write("Multipage Streamlit portfolio website")

st.subheader("Other Projects")
st.write("Simple Python apps")
st.write("UI practice projects")
st.write("School systems")
