import streamlit as st

st.set_page_config(page_title="Contact", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #ff4fa3, #7a00ff);
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

/* CARD (REMOVE GREY LOOK → MAKE CLEAN WHITE) */
.card {
    background: #ffffff;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    margin-bottom: 20px;
    text-align: center;
}

/* INPUTS */
input, textarea {
    border-radius: 10px !important;
    border: 1px solid #ddd !important;
}

/* HEADINGS */
h1, h2, h3 {
    text-align: center;
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

/* 🔥 FIX BUTTON VISIBILITY */
div.stButton > button {
    background: linear-gradient(90deg, #ff0057, #7a00ff) !important;
    color: white !important;
    font-weight: bold !important;
    border-radius: 25px !important;
    padding: 10px 20px !important;
    border: none !important;
    box-shadow: 0 6px 15px rgba(0,0,0,0.2);
    width: 100%;
}

div.stButton > button:hover {
    transform: scale(1.03);
    transition: 0.2s ease-in-out;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
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

if st.button("🚀 Send Message"):
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
<a href="https://github.com/reamay526" target="_blank">🔗 GitHub</a><br><br>
<a href="https://www.facebook.com/rea.villanueva.9277" target="_blank">📘 Facebook</a>
</p>

</div>
""", unsafe_allow_html=True)
