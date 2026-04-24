import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="🌐", layout="centered")

# STYLE (ALL BLACK TEXT + SIMPLE BACKGROUND)
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
    p, span, div, label, caption {
        color: #000000 !important;
    }

    /* FORCE INPUT TEXT BLACK */
    input, textarea {
        color: #000000 !important;
    }

    /* SIDEBAR CLEAN */
    section[data-testid="stSidebar"] {
        background-color: rgba(255,255,255,0.9);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# TITLE
st.title("Welcome to My Portfolio")

st.write("Simple Streamlit project for basic Computer Science")

st.markdown("---")

# PROFILE SECTION
col1, col2 = st.columns([1, 2])

with col1:
    st.image("mayie.png", width=150)

with col2:
    st.subheader("Rea May M. Villanueva")
    st.write("BSCS 3B")
    st.write("Basic Computer Science Student")
    st.write("Learning Programming & Web Development")

st.markdown("---")

# MESSAGE
st.success("Welcome! Use the sidebar to navigate through my pages.")
