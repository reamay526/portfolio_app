import streamlit as st

st.set_page_config(page_title="Projects", layout="wide")

# ---------------- STYLE (KEEP CONSISTENT DESIGN) ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #3b1b5a, #ff4fa3, #7a00ff);
    font-family: Arial, sans-serif;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

.block-container {
    padding-top: 2.5rem;
    padding-bottom: 2.5rem;
}

/* TEXT */
html, body, .stApp, p, div, span, label {
    color: #111111 !important;
    font-weight: 700 !important;
}

/* TITLE */
h1 {
    text-align: center;
    color: white !important;
    font-weight: 900 !important;
}

/* GLASS CARD (MATCH OTHER PAGES) */
.card {
    background: rgba(255, 255, 255, 0.30);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 16px 18px;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.10);
    margin-bottom: 15px;
    border: 1px solid rgba(255, 255, 255, 0.25);
}

/* CENTER TEXT */
.card h3 {
    text-align: center;
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
st.markdown("<h1>💼 My Projects</h1>", unsafe_allow_html=True)

# ---------------- PROJECT GRID ----------------
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    <h3>🌐 Portfolio Website</h3>
    <p>
    ✔ Built using Streamlit<br>
    ✔ Multi-page structure<br>
    ✔ Responsive UI design<br>
    ✔ Personal developer portfolio
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>🧩 Other Projects</h3>
    <p>
    ✔ Python mini applications<br>
    ✔ UI/UX practice layouts<br>
    ✔ School-based system projects<br>
    ✔ Coding exercises & experiments
    </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- FUTURE PROJECT SECTION ----------------
st.markdown("""
<div class="card">
<h3>🚀 Future Goals</h3>
<p>
I aim to build more advanced full-stack applications, improve UI/UX design skills,
and develop real-world systems that solve practical problems.
</p>
</div>
""", unsafe_allow_html=True)
