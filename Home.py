import streamlit as st

st.set_page_config(page_title="My Portfolio", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
}

html, body, .stApp {
    color: #000000 !important;
    font-family: Arial;
}

h1, h2, h3 {
    color: #000000 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    colA, colB = st.columns([1, 2])

    with colA:
        st.image("mayie.png", width=220)

    with colB:
        st.title("Welcome to My Portfolio")
        st.subheader("Rea May M. Villanueva")
        st.write("BSCS 3B")
        st.write("Aspiring Developer & Designer")
        st.write("Interested in Web Development")

        st.button("Say Hello 👋")
