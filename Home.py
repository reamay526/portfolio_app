import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="🌐")

# STYLE
st.markdown("""<style>.stApp{background:linear-gradient(135deg,#3b1b5a,#e6e6e6,#ff4fa3);}html,body,.stApp{color:#000 !important;}</style>""", unsafe_allow_html=True)

st.title("Welcome to My Portfolio")

col1, col2 = st.columns(2)

with col1:
    st.image("butterfly.png")

with col2:
    st.write("Name: Rea May M. Villanueva")
    st.write("Course: BSCS 3B")

st.success("Simple Streamlit Multipage App")
