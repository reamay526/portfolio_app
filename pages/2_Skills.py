import streamlit as st

st.set_page_config(page_title="Skills", layout="wide")

# ---------------- STYLE ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #3b1b5a, #ff4fa3, #7a00ff);
}

.block-container {
    padding-top: 2.5rem;
    padding-bottom: 2.5rem;
}

h1 {
    text-align: center;
    color: white !important;
    font-weight: 900;
}

/* Card */
.card {
    background: rgba(255,255,255,0.25);
    padding: 16px;
    border-radius: 14px;
    margin-bottom: 15px;
    text-align: center;
    backdrop-filter: blur(10px);
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
st.markdown("<h1>⚡ My Skills</h1>", unsafe_allow_html=True)

# ---------------- INTERACTIVE SECTION (FIX FOR REQUIREMENT) ----------------
st.markdown("## 🎯 Skill Explorer")

skill_area = st.selectbox(
    "Select a skill category:",
    ["Programming", "Frontend", "Tools"]
)

if skill_area == "Programming":
    st.progress(85)
    st.write("Python - 85%")
elif skill_area == "Frontend":
    st.progress(88)
    st.write("HTML - 88%")
    st.progress(87)
    st.write("CSS - 87%")
else:
    st.write("✔ GitHub")
    st.write("✔ VS Code")
    st.write("✔ Streamlit")

# ---------------- VISUAL SUMMARY ----------------
st.markdown("""
<div class="card">
<h3>🚀 Focus Areas</h3>
<p>Web Development • UI Design • Clean Code • Problem Solving</p>
</div>
""", unsafe_allow_html=True)
