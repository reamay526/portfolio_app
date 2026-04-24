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

st.title("Skills")

st.write("Python")
st.progress(85)

st.write("HTML")
st.progress(88)

st.write("CSS")
st.progress(87)

st.subheader("Tools")
st.write("GitHub")
st.write("VS Code")
st.write("Streamlit")
