import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="🌐", layout="wide")

st.title("🌐 My Streamlit Portfolio")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("butterfly.png")

with col2:
    st.subheader("Rea May M. Villanueva")
    st.write("BSCS 3B")
    st.write("Simple Streamlit Multipage Project")

st.info("Use the sidebar to navigate through pages.")