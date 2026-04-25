import streamlit as st

st.set_page_config(page_title="Contact", layout="wide")

st.markdown("""
<style>

/* FULL BACKGROUND (REMOVE ALL WHITE AREAS) */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #3b1b5a, #ff4fa3, #7a00ff);
}

/* REMOVE TOP WHITE GAP */
[data-testid="stHeader"] {
    background: transparent !important;
}

[data-testid="stToolbar"] {
    background: transparent !important;
}

/* REMOVE CONTAINER WHITE SPACE */
.block-container {
    background: transparent !important;
    padding-top: 1rem !important;
    padding-bottom: 3rem;
    max-width: 900px;
    margin: auto;
}

/* MAIN TEXT */
html, body, .stApp {
    color: #000000 !important;
}

/* TITLE FIX (IMPORTANT) */
h1 {
    color: white !important;
    text-align: center;
    margin-top: 0px;
}

.card {
    background: #ffffff;
    padding: 18px;          /* smaller padding */
    border-radius: 12px;    /* slightly tighter corners */
    box-shadow: 0 6px 16px rgba(0,0,0,0.12);
    margin-bottom: 15px;
    text-align: center;
    max-width: 500px;       /* 🔥 makes box smaller */
    margin-left: auto;
    margin-right: auto;     /* centers the box */
}

/* INPUT */
input, textarea {
    border-radius: 10px !important;
    border: 1px solid #ddd !important;
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

div.stButton > button:hover {
    transform: scale(1.03);
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

# ---------------- TITLE (NOW INSIDE GRADIENT CLEANLY) ----------------
st.markdown("<h1>📬 Contact Me</h1>", unsafe_allow_html=True)

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
