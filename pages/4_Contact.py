import streamlit as st

st.set_page_config(page_title="Contact", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
    font-family: Arial;
}

/* TEXT */
html, body, .stApp {
    color: #000000 !important;
}

/* CENTER CONTAINER */
.block-container {
    padding-top: 3rem;
    max-width: 900px;
    margin: auto;
}

/* CARD STYLE (MATCH ALL PAGES) */
.card {
    background: rgba(255,255,255,0.80);
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    text-align: center;
}

/* INPUT ALIGNMENT */
input, textarea {
    border-radius: 10px !important;
}

/* HEADINGS */
h1, h2, h3 {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("📬 Contact Me")

# ---------------- FORM CARD ----------------
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

# ---------------- LINKS CARD ----------------
st.markdown("""
<div class="card">
<h3>🌐 Connect With Me</h3>
<p>
<a href="https://github.com/reamay526" target="_blank">GitHub</a><br>
<a href="https://www.facebook.com/rea.villanueva.9277" target="_blank">Facebook</a>
</p>
</div>
""", unsafe_allow_html=True)
