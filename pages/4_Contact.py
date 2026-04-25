import streamlit as st

st.set_page_config(page_title="Contact", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
    font-family: Arial;
}

/* MAIN TEXT */
html, body, .stApp {
    color: #000000 !important;
}

/* CONTAINER */
.block-container {
    padding-top: 3rem;
    max-width: 900px;
    margin: auto;
}

/* CARD STYLE */
.card {
    background: rgba(255,255,255,0.80);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    text-align: center;
}

/* INPUT STYLE */
input, textarea {
    border-radius: 10px !important;
}

/* LINKS STYLE (FIXED) */
a {
    text-decoration: none;
    font-weight: bold;
    color: #7a00ff;
}

a:hover {
    color: #ff0057;
}

/* HEADINGS */
h1, h2, h3 {
    text-align: center;
}

/* SIDEBAR (SAFE FIX) */
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

# ---------------- TITLE ----------------
st.title("📬 Contact Me")

# ---------------- FORM ----------------
st.markdown('<div class="card">', unsafe_allow_html=True)

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")

if st.button("Send Message"):
    if name and email and message:
        st.success("Message sent successfully 🚀")
    else:
        st.error("Please fill all fields")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- LINKS ----------------
st.markdown("""
<div class="card">
<h3>🌐 Connect With Me</h3>

<p>
<a href="https://github.com/reamay526" target="_blank">🔗 GitHub Profile</a><br><br>
<a href="https://www.facebook.com/rea.villanueva.9277" target="_blank">📘 Facebook Profile</a>
</p>

</div>
""", unsafe_allow_html=True)
