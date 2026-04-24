import streamlit as st

st.set_page_config(page_title="Portfolio", page_icon="🌐", layout="centered")

# STYLE (SAFE + READABLE)
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

# LEFT IMAGE + RIGHT TEXT
col1, col2 = st.columns([1, 2])

with col1:
    st.image("mayie.png", width=180)

with col2:
    st.markdown("## Rea May M. Villanueva")
    st.write("🎓 BSCS 3B")
    st.write("💻 Aspiring Developer")
    st.write("🎨 UI/UX Learner")

st.markdown("---")

# WELCOME BACK (RESTORED)
st.success("👋 Welcome to my Portfolio!")
st.info("Explore my skills, projects, and contact details using the sidebar.")

st.markdown("---")
st.write("Simple Streamlit Multipage Portfolio")
