import streamlit as st

st.set_page_config(page_title="About Me", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
}
html, body, .stApp, p, div, span, label {
    color: #000000 !important;
    text-align: center;
}
section[data-testid="stSidebar"] {
    background-color: rgba(255,255,255,0.9);
}
h1, h2, h3 {
    color: #3b1b5a;
}
</style>
""", unsafe_allow_html=True)

st.title("About Me")
st.write("I enjoy learning programming and building simple applications.")
st.subheader("Education")
st.write("BS Computer Science")
st.subheader("Goals")
st.write("- Improve coding skills")
st.write("- Build useful projects")
