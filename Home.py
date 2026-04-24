import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="🌐")

st.markdown("""
<style>
.stApp { background-color: #f7f3ff; }
</style>
""", unsafe_allow_html=True)

st.title("Welcome to My Portfolio")

col1, col2 = st.columns(2)

with col1:
    st.image("butterfly.png")

with col2:
    st.write("Name: Rea May M. Villanueva")
    st.write("Course: BSCS 3B")

st.success("Simple Streamlit Multipage App")
