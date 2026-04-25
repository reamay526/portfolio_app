import streamlit as st

st.set_page_config(page_title="Contact", layout="wide")

st.markdown("""
<style>

/* FULL BACKGROUND */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #3b1b5a, #ff4fa3, #7a00ff);
}

/* REMOVE TOP WHITE SPACE */
[data-testid="stHeader"] {
    background: transparent !important;
}

.block-container {
    background: transparent !important;
    padding-top: 1rem !important;
    max-width: 900px;
    margin: auto;
}

/* TITLE */
h1, h2, h3 {
    text-align: center;
    color: white !important;
}

/* SMALL + COMPACT CARD */
.card {
    background: #ffffff;
    padding: 12px;
    border-radius: 12px;
    box-shadow: 0 6px 16px rgba(0,0,0,0.12);
    max-width: 450px;
    margin: 0 auto 15px auto;
    text-align: center;
}

/* INPUTS */
input {
    border-radius: 10px !important;
    margin-bottom: 8px !important;
}

/* SMALLER TEXTAREA */
textarea {
    border-radius: 10px !important;
    height: 90px !important;
    margin-bottom: 8px !important;
}

/* BUTTON */
div.stButton > button {
    background: linear-gradient(90deg, #ff0057, #7a00ff) !important;
    color: white !important;
    font-weight: bold !important;
    border-radius: 25px !important;
    padding: 10px 20px !important;
    border: none !important;
    width: 100%;
}

/* LINKS */
a {
    text-decoration: none;
    font-weight: bold;
    color: #7a00ff;
}
a:hover {
    color: #ff0057;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #3b1b5a, #7a00ff);
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] div {
    color: white !important;
    font-weight: 500;
}

section[data-testid="stSidebar"] div:hover {
    background-color: rgba(255,255,255,0.15);
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.markdown("<h2>📬 Contact Me</h2>", unsafe_allow_html=True)

# FORM CARD
st.markdown('<div class="card">', unsafe_allow_html=True)

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")

if st.button("🚀 Send Message"):
    if name and email and message:
        st.success("Message sent successfully 🚀")
    else:
        st.error("Please fill all fields")

st.markdown('</div>', unsafe_allow_html=True)

# LINKS CARD
st.markdown("""
<div class="card">
<h3>🌐 Connect With Me</h3>

<p>
<a href="https://github.com/reamay526" target="_blank">🔗 GitHub</a><br><br>
<a href="https://www.facebook.com/rea.villanueva.9277" target="_blank">📘 Facebook</a>
</p>

</div>
""", unsafe_allow_html=True)
