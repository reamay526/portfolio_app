import streamlit as st

st.set_page_config(page_title="Portfolio", page_icon="🌐", layout="centered")

# CLEAN STYLE (READABLE + SOFT LOOK)
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
        text-align: center;
    }

    html, body, .stApp {
        color: #000000 !important;
        text-align: center;
    }

    h1, h2, h3 {
        color: #000000 !important;
    }

    p, div, span, label {
        color: #000000 !important;
    }

    section[data-testid="stSidebar"] {
        background-color: rgba(255,255,255,0.9);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HEADER
st.markdown("## 🌐 Welcome to My Portfolio")
st.caption("Simple Streamlit Multipage Project")

st.markdown("---")

# PROFILE SECTION (CLEAN LAYOUT)
col1, col2 = st.columns([1, 2], vertical_alignment="center")

with col1:
    st.image("mayie.png", width=160)

with col2:
    st.markdown("### Rea May M. Villanueva")
    st.write("BSCS 3B")
    st.write("Aspiring Developer | UI/UX Learner")

st.markdown("---")

# WELCOME MESSAGE
st.success("Welcome! Explore my skills, projects, and contact page using the sidebar.")

st.markdown("---")

st.write("Built using Streamlit")
