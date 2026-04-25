import streamlit as st

st.set_page_config(page_title="Contact", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>

/* BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #ff4fa3, #7a00ff);
    font-family: Arial, sans-serif;
}

/* REMOVE HEADER SPACE */
[data-testid="stHeader"] {
    background: transparent !important;
}

[data-testid="stAppViewContainer"] > .main {
    padding-top: 0rem !important;
}

/* CONTAINER */
.block-container {
    padding-top: 0.5rem !important;
    padding-bottom: 1.5rem !important;
}

/* TEXT */
html, body, .stApp, p, div, span, label {
    color: #000000 !important;
    font-weight: 700 !important;
}

/* TITLE */
h1 {
    text-align: center;
    font-weight: 900 !important;
    margin-top: 0px !important;
}

/* CARD (COMPACT) */
.card {
    background: rgba(255, 255, 255, 0.50);
    backdrop-filter: blur(10px);
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.12);
    border: 1px solid rgba(255,255,255,0.3);
    max-width: 600px;
    margin: auto;
}

/* INPUTS */
.stTextInput input,
.stTextArea textarea {
    background-color: rgba(255,255,255,0.75) !important;
    color: #000000 !important;
    border-radius: 8px !important;
    border: 1px solid rgba(0,0,0,0.15) !important;
    font-weight: 700 !important;
}

/* BUTTON */
div.stButton > button {
    background: linear-gradient(90deg, #ff0057, #7a00ff) !important;
    color: white !important;
    font-weight: 800 !important;
    border-radius: 20px !important;
    padding: 8px 16px !important;
    width: 100%;
}

/* LINKS */
a {
    text-decoration: none;
    font-weight: 800;
    color: #4b0082 !important;
}

a:hover {
    color: #ff0057 !important;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #3b1b5a, #7a00ff);
}

section[data-testid="stSidebar"] * {
    color: white !important;
    font-weight: 700 !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1>📬 Contact Me</h1>", unsafe_allow_html=True)

# ---------------- FORM ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)

name = st.text_input("Your Name")
email = st.text_input("Your Email")
message = st.text_area("Your Message")

if st.button("🚀 Send Message"):
    if name and email and message:
        st.success("Message sent successfully 🚀")
    else:
        st.error("Please fill in all fields")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- SOCIAL LINKS (SINGLE COLUMN) ----------------
st.markdown("""
<div class="card">
<h3 style='text-align:center;'>🌐 Connect With Me</h3>

<div style="text-align:center; line-height:2;">
    <a href="https://github.com/reamay526" target="_blank">GitHub</a><br><br>
    <a href="https://www.facebook.com/rea.villanueva.9277" target="_blank">Facebook</a>
</div>

</div>
""", unsafe_allow_html=True)
