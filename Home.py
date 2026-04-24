import streamlit as st

st.set_page_config(page_title="My Portfolio", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
    font-family: Arial;
}

html, body, .stApp {
    color: #000000 !important;
}

h1, h2, h3 {
    color: #000000 !important;
}

.block-container {
    padding-top: 3rem;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    left, right = st.columns([1, 2])

    with left:
        st.image("mayie.png", width=220)

    with right:
        st.title("Welcome to My Portfolio")
        st.subheader("Rea May M. Villanueva")
        st.write("BSCS 3B")
        st.write("Aspiring Developer & Designer")
        st.write("Interested in Web Development")

        st.button("Say Hello 👋")
