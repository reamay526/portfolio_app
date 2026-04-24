import streamlit as st

st.title("Skills")

python = st.slider("Python", 0, 100, 70)
st.progress(python)

html = st.slider("HTML", 0, 100, 60)
st.progress(html)

st.checkbox("GitHub")
st.checkbox("Streamlit")
