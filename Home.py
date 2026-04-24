import streamlit as st

st.set_page_config(page_title="Portfolio", page_icon="🌐", layout="centered")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
    text-align: center;
}
html, body, .stApp, p, div, span, label {
    color: #000000 !important;
    text-align: center;
}
section[data-testid="stSidebar"] {
    background-color: rgba(255,255,255,0.9);
}
</style>
""", unsafe_allow_html=True)

st.title("Welcome to My Portfolio")

st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("mayie.png", width=150)

with col2:
    st.markdown("### Rea May M. Villanueva")
    st.write("BSCS 3B")
    st.write("Aspiring Developer & Designer")
    st.write("Interested in Web Development")

st.markdown("---")

st.success("Explore my portfolio using the sidebar.")
