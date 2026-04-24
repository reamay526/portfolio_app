import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="🌐", layout="centered")

# SIMPLE STYLE (clean + readable)
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

    section[data-testid="stSidebar"] {
        background-color: rgba(255,255,255,0.9);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# TITLE
st.title("Welcome to My Portfolio")

st.write("Simple project made using Streamlit (basic CS level)")

st.markdown("---")

# IMAGE + INFO
col1, col2 = st.columns([1, 2])

with col1:
    st.image("mayie.png", width=150)

with col2:
    st.subheader("Rea May M. Villanueva")
    st.write("BSCS 3B")
    st.write("Basic CS Student")
    st.write("Learning Python & Web Development")

st.markdown("---")

# MESSAGE
st.success("Use the sidebar to navigate through my pages.")
