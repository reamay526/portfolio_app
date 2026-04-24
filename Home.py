import streamlit as st

st.set_page_config(page_title="My Portfolio", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
    text-align: center;
}

html, body, .stApp {
    color: #000000 !important;
    text-align: center;
}

h1, h2, h3 {
    color: #3b1b5a;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.image("mayie.png", width=220)

with col2:
    st.title("Welcome to My Portfolio")
    st.subheader("Rea May M. Villanueva")
    st.write("BSCS 3B")
    st.markdown("Aspiring Developer & Designer")
    st.write("Interested in Web Development")

    if st.button("Say Hello"):
        st.success("Thanks for visiting my portfolio!")
