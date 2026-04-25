import streamlit as st

st.set_page_config(page_title="Portfolio Home", layout="wide")

# ---------------- CSS (CLEAN & SAFE) ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #3b1b5a, #ff4fa3, #7a00ff);
}

/* Header spacing */
.block-container {
    padding-top: 3rem;
    padding-bottom: 3rem;
}

/* Title */
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: 900;
    color: white;
    margin-bottom: 30px;
}

/* Card style */
.card {
    background: rgba(255, 255, 255, 0.15);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(8px);
    color: white;
}

/* Button */
div.stButton > button {
    background: linear-gradient(90deg, #00c6ff, #7f00ff);
    color: white;
    border-radius: 12px;
    border: none;
    font-weight: bold;
    width: 100%;
}

div.stButton > button:hover {
    transform: scale(1.03);
    transition: 0.2s;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="main-title">👋 Welcome to My Portfolio</div>', unsafe_allow_html=True)

# ---------------- HERO SECTION ----------------
col1, col2 = st.columns([1, 2])

with col1:
    st.image("mayie.png", width=220)

with col2:
    st.markdown("""
    <div class="card">
        <h2>Rea May Villanueva</h2>
        <p>🎓 Computer Science Student (3rd Year)</p>
        <p>💻 Aspiring Developer & UI Designer</p>
        <p>I create clean, functional, and user-friendly web applications using Python and Streamlit.</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- INTERACTIVE SECTION (REQUIRED) ----------------
st.markdown("## 🎯 Quick Interaction Section")

st.write("Select your interest to explore my portfolio focus:")

interest = st.selectbox(
    "Choose area:",
    ["Web Development", "UI Design", "Python Projects", "Data Apps"]
)

if interest == "Web Development":
    st.info("You will see my website projects in the Projects page.")
elif interest == "UI Design":
    st.success("I focus on clean and modern UI layouts.")
elif interest == "Python Projects":
    st.warning("I build logic-based and interactive Python apps.")
else:
    st.error("I also explore data-driven applications.")

# ---------------- BUTTON INTERACTION ----------------
if st.button("🚀 Explore My Portfolio"):
    st.success("Go to the sidebar to navigate: About, Skills, Projects, Contact")

# ---------------- FOOTER ----------------
st.markdown("---")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("### ⚡ Strength")
    st.write("Clean UI & structured design")

with c2:
    st.markdown("### 🚀 Focus")
    st.write("Python + Streamlit development")

with c3:
    st.markdown("### 🌱 Growth")
    st.write("UI/UX + Full-stack basics")
