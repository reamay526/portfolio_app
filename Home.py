import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="🌐", layout="centered")

# STYLE (same safe gradient + readable text)
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

# HEADER
st.title("🌐 My Portfolio")

st.markdown("### Welcome to my personal website")

st.markdown("---")

# CENTERED CARD STYLE LAYOUT
col1, col2 = st.columns([1, 2])

with col1:
    st.image("butterfly.png", width=200)

with col2:
    st.markdown("## Rea May M. Villanueva")
    st.write("🎓 BSCS 3B Student")
    st.write("💻 Aspiring Developer")
    st.write("🎨 Interested in UI/UX Design")

st.markdown("---")

# HIGHLIGHT BOX STYLE
st.success("🚀 Explore my skills, projects, and contact details using the sidebar")

st.info("💡 This portfolio is built using Streamlit multipage app")

st.markdown("---")

# FOOTER STYLE
st.markdown("📌 Simple | Clean | Beginner Friendly Portfolio")
