import streamlit as st

st.set_page_config(page_title="Streamlit Multipage App", page_icon="🌐", layout="wide")

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

col1, col2 = st.columns([1, 2])

with col1:
    st.image("butterfly.png")

with col2:
    st.title("Rea May M. Villanueva")
    st.subheader("BSCS 3B")
    st.write("Streamlit Multipage Web Application")

st.info("Use the sidebar to navigate through the pages.")
