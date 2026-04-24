import streamlit as st

st.set_page_config(page_title="About")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
    text-align: center;
}
html, body, .stApp, p, div, span, label {
    color: #000000 !important;
    text-align: center;
}
section[data-testid="stSidebar"] {
    background-color: rgba(255,255,255,0.9);
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
