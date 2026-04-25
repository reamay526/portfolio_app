import streamlit as st

st.set_page_config(page_title="Portfolio", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #ff4fa3, #7a00ff);
    font-family: Arial;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

.block-container {
    background: transparent !important;
    padding-top: 3rem;
    padding-bottom: 3rem;
}

html, body, .stApp, p, div, span, label, h1, h2, h3 {
    color: #000000 !important;
}

.top-title {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    margin-bottom: 30px;
    color: white;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #3b1b5a, #7a00ff);
}

section[data-testid="stSidebar"] * {
    color: white !important;
    font-weight: 500;
}

div.stButton > button {
    background: linear-gradient(90deg, #00c6ff, #7f00ff) !important;
    color: white !important;
    border-radius: 20px;
    padding: 12px 24px;
    border: none;
    font-weight: 700;
}

div.stButton > button:hover {
    transform: scale(1.05);
    transition: 0.2s ease-in-out;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="top-title">👋 Welcome to My Portfolio</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.5, 3, 0.5])

with col2:
    left, right = st.columns([1.5, 2.5], gap="large")

    with left:
        st.image("mayie.png", width=250)

    with right:
        st.markdown("### Rea May M. Villanueva")
        st.write("🎓 BS Computer Science Student (3rd Year)")
        st.write("💻 Aspiring Full-Stack Developer & UI Designer")
        st.write("🌐 Passionate about building clean web applications")

        st.write("""
        I enjoy transforming ideas into functional systems using Python and web technologies.
        I am continuously improving my skills in programming, design, and development.
        """)

        if st.button("🚀 Say Hello"):
            st.success("Hello! Welcome to my portfolio 👋")

st.markdown("---")

st.markdown("## 📌 What I Do")
st.write("""
✔ Build Python web applications using Streamlit  
✔ Design clean and user-friendly interfaces  
✔ Develop school and personal projects  
✔ Learn full-stack development fundamentals  
""")
