import streamlit as st

st.set_page_config(page_title="Projects", layout="wide")

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
st.markdown("<h1>💼 My Projects</h1>", unsafe_allow_html=True)

# ---------------- INTERACTIVE FILTER (REQUIRED FIX) ----------------
category = st.selectbox(
    "Filter projects by category:",
    ["All", "Streamlit", "Frontend", "Practice Projects"]
)

# ---------------- PROJECT DATA (SIMPLIFIED LOGIC) ----------------
projects = {
    "Streamlit": {
        "title": "🌐 Portfolio App",
        "desc": "Multipage Streamlit Portfolio Application"
    },
    "Frontend": {
        "title": "👩‍💻 Personal Website",
        "desc": "HTML/CSS Portfolio Design"
    },
    "Practice Projects": {
        "title": "🎨 Bootstrap Project",
        "desc": "Responsive Web Design Practice"
    }
}

# ---------------- DISPLAY LOGIC ----------------
for key, project in projects.items():
    if category == "All" or category == key:

        st.markdown(f"""
        <div class="card">
            <h3>{project['title']}</h3>
            <p>{project['desc']}</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button(f"View Details - {project['title']}"):
            st.info(f"""
            Project: {project['title']}
            Description: {project['desc']}
            Status: Completed
            Tools: HTML, CSS, Streamlit (depending on project)
            """)
