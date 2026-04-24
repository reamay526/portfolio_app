import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #74ebd5, #ACB6E5);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Skills")

python = st.slider("Python", 0, 100, 70)
st.progress(python)

html = st.slider("HTML", 0, 100, 60)
st.progress(html)

css = st.slider("CSS", 0, 100, 55)
st.progress(css)

st.checkbox("GitHub")
st.checkbox("Streamlit")
st.checkbox("VS Code")
