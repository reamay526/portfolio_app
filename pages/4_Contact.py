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

/* HEADER FIX */
[data-testid="stHeader"] {
    background: transparent !important;
}

.block-container {
    padding-bottom: 2.5rem;
}

/* TITLE (WHITE FOR CONTRAST) */
h1, h2, h3 {
    text-align: center;
    color: white !important;
    font-weight: 900 !important;
}

/* GLASS CARD (IMPROVED VISIBILITY) */
.card {
    background: rgba(255, 255, 255, 0.40);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    padding: 22px;
    border-radius: 14px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    border: 1px solid rgba(255, 255, 255, 0.35);
    max-width: 700px;
    margin: auto;
    text-align: center;
}

/* TEXT INSIDE CARD (FIX VISIBILITY) */
.card p, .card h3 {
    color: #111111 !important;
    font-weight: 800 !important;
}

/* INPUT STYLE (CLEARER) */
input, textarea {
    border-radius: 10px !important;
    font-weight: 600 !important;
}

/* BUTTON */
div.stButton > button {
    background: linear-gradient(90deg, #ff0057, #7a00ff) !important;
    color: white !important;
    font-weight: 800 !important;
    border-radius: 25px !important;
    padding: 10px 20px !important;
    border: none !important;
    width: 100%;
    box-shadow: 0 6px 16px rgba(0,0,0,0.25);
}

div.stButton > button:hover {
    transform: scale(1.03);
    transition: 0.2s ease-in-out;
}

/* LINKS */
a {
    text-decoration: none;
    font-weight: 800;
    color: #4b0082;
}

a:hover {
    color: #ff0057;
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

# ---------------- FORM CARD ----------------
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

# ---------------- SOCIAL LINKS ----------------
st.markdown("""
<div class="card">
<h3>🌐 Connect With Me</h3>
<p>
<a href="https://github.com/reamay526" target="_blank">GitHub</a><br><br>
<a href="https://www.facebook.com/rea.villanueva.9277" target="_blank">Facebook</a>
</p>
</div>
""", unsafe_allow_html=True)
