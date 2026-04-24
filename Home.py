import streamlit as st

st.set_page_config(page_title="My Portfolio", layout="wide")

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
h1, h2, h3 {
    color: #3b1b5a;
    text-align: center;
}
section[data-testid="stSidebar"] {
    background-color: rgba(255,255,255,0.9);
}
.stButton > button {
    background-color: #3b1b5a;
    color: white;
    border-radius: 10px;
}
.stButton > button:hover {
    background-color: #ff4fa3;
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## 🌸 Portfolio")
    page = st.radio("Navigation", ["Home", "About", "Skills", "Projects", "Contact"])
    st.markdown("---")
    st.write("BSCS 3B")
    st.write("Aspiring Developer")

if page == "Home":
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image("mayie.png", width=200)
        st.title("Welcome to My Portfolio")
        st.subheader("Rea May M. Villanueva")
        st.write("BSCS 3B")
        st.markdown("Aspiring Developer & Designer")
        st.write("Interested in Web Development")
        if st.button("Say Hello"):
            st.success("Thanks for visiting my portfolio!")

elif page == "About":
    col1, col2, col3 = st.columns(3)
    with col2:
        st.title("About Me")
        st.write("I enjoy learning programming and building simple applications.")
        st.subheader("Education")
        st.write("BS Computer Science")
        st.subheader("Goals")
        st.write("Improve coding skills")
        st.write("Build useful projects")

elif page == "Skills":
    col1, col2, col3 = st.columns(3)
    with col2:
        st.title("Skills")
        st.write("Python")
        st.write("HTML")
        st.write("CSS")
        st.markdown("Tools")
        st.write("GitHub")
        st.write("VS Code")
        st.write("Streamlit")

elif page == "Projects":
    col1, col2, col3 = st.columns(3)
    with col2:
        st.title("Projects")
        st.subheader("Portfolio App")
        st.write("Multipage Streamlit portfolio website")
        st.subheader("Other Projects")
        st.write("Simple Python apps")
        st.write("UI practice projects")
        st.write("School systems")

elif page == "Contact":
    col1, col2, col3 = st.columns(3)
    with col2:
        st.title("Contact Me")
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        if st.button("Send"):
            if name and email and message:
                st.success("Message sent successfully!")
            else:
                st.error("Please fill all fields.")
