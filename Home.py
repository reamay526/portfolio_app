import streamlit as st

st.set_page_config(page_title="Portfolio", page_icon="🌐", layout="centered")

# STYLE (SAFE GRADIENT + READABLE TEXT)
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

    h1, h2, h3, h4, h5, h6,
    p, span, label, div {
        color: #000000 !important;
        text-align: center;
    }

    section[data-testid="stSidebar"] {
        background-color: rgba(255,255,255,0.9);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# PROFILE IMAGE FIRST (CENTERED)
st.image("butterfly.png", width=180)

# NAME + INFO
st.markdown("## Rea May M. Villanueva")
st.write("🎓 BSCS 3B")
st.write("💻 Aspiring Developer")
st.write("🎨 UI/UX Learner")

st.markdown("---")

# MESSAGE BOX
st.success("Welcome! Explore my skills, projects, and contact details in the sidebar.")

st.info("This is a simple Streamlit multipage portfolio project.")
