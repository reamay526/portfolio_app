import streamlit as st

st.set_page_config(page_title="My Portfolio", layout="wide")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("mayie.png", width=180)

with col2:
    st.title("Welcome to My Portfolio")
    st.subheader("Rea May M. Villanueva")
    st.write("BSCS 3B")
    st.markdown("### 💡 Aspiring Developer & Designer")
    st.write("Interested in Web Development")

st.markdown("---")

st.markdown("## 👋 About Me")
st.write("""
I am a Computer Science student passionate about building web applications,
learning new technologies, and improving my design and development skills.
""")

st.markdown("---")

st.markdown("## 📌 Navigation")
st.info("Use the sidebar to explore my portfolio: About • Projects • Contact")

if st.button("✨ Say Hello"):
    st.success("Thanks for visiting my portfolio!")
