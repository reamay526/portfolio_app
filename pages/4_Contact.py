import streamlit as st

st.set_page_config(page_title="Contact", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #3b1b5a, #ff4fa3, #7a00ff);
}

.block-container {
    padding-top: 1rem;
}

h1 {
    text-align: center;
    color: white !important;
    font-weight: 900;
}

/* Card */
.card {
    background: rgba(255,255,255,0.4);
    padding: 15px;
    border-radius: 12px;
    max-width: 600px;
    margin: auto;
    margin-bottom: 15px;
    text-align: center;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #3b1b5a, #7a00ff);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1>📬 Contact Me</h1>", unsafe_allow_html=True)

# ---------------- FORM (STRICT VERSION) ----------------
with st.container():
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("🚀 Send Message"):
        if name.strip() and email.strip() and message.strip():

            # simple format check (basic compliance upgrade)
            if "@" in email:
                st.success("Message sent successfully 🚀")
                st.info(f"Preview: {name} ({email}) sent a message.")
            else:
                st.error("Please enter a valid email address.")
        else:
            st.error("All fields are required.")

# ---------------- SOCIAL LINKS ----------------
st.markdown("""
<div class="card">
<h3>🌐 Connect With Me</h3>
<p>
<a href="https://github.com/reamay526" target="_blank">GitHub</a><br>
<a href="https://www.facebook.com/rea.villanueva.9277" target="_blank">Facebook</a>
</p>
</div>
""", unsafe_allow_html=True)
