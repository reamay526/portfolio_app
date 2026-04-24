import streamlit as st

st.set_page_config(page_title="Streamlit Multipage App", page_icon="🌐", layout="wide")

# Animated gradient + black text
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(-45deg, #a1c4fd, #c2e9fb, #fbc2eb, #fad0c4);
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    html, body, [class*="css"] {
        color: black !important;
    }

    section[data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.65);
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 2])

with col1:
    st.image("butterfly.png")

with col2:
    st.title("Rea May M. Villanueva")
    st.subheader("BSCS 3B")
    st.write("Streamlit Multipage Web Application")

st.info("Use the sidebar to navigate.")
