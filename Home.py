import streamlit as st

st.set_page_config(page_title="Streamlit Multipage App", page_icon="🌐", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(-45deg, #d9c2ff, #e6e6e6, #ff4f8b, #caa6ff);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    html, body, .stApp, [class*="css"] {
        color: #000000 !important;
    }

    p, span, label, div {
        color: #000000 !important;
    }

    input, textarea {
        color: #000000 !important;
    }

    section[data-testid="stSidebar"] {
        background-color: rgba(255,255,255,0.75);
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 2])

with col1:
    st.image("butterfly.png", use_column_width=True)

with col2:
    st.title("Rea May M. Villanueva")
    st.subheader("BSCS 3B")
    st.write("A simple Streamlit Multipage Web Application")

st.info("Use the sidebar to navigate through pages.")
