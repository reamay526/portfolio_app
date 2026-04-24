import streamlit as st

st.set_page_config(page_title="Skills")

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

st.title("Skills")

st.write("Python")
st.progress(85)

st.write("HTML")
st.progress(88)

st.write("CSS")
st.progress(87)

st.subheader("Tools")
st.write("- GitHub")
st.write("- VS Code")
st.write("- Streamlit")
