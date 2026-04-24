import streamlit as st

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
}

.block-container {
    padding-top: 3rem;
}

html, body, .stApp {
    color: #000000 !important;
}
</style>
""", unsafe_allow_html=True)

st.title("About Me")

st.markdown("""
I enjoy learning programming and building simple applications.
""")

st.subheader("Education")
st.write("BS Computer Science")

st.subheader("Goals")
st.write("Improve coding skills")
st.write("Build useful projects")
