import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="🌐")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
    }

    html, body, .stApp {
        color: #000000 !important;
    }

    h1, h2, h3, h4, h5, h6,
    p, span, label, div {
        color: #000000 !important;
    }

    input, textarea {
        background-color: rgba(255,255,255,0.9) !important;
        color: #000000 !important;
    }

    section[data-testid="stSidebar"] {
        background-color: rgba(255,255,255,0.9);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Welcome to My Portfolio")

col1, col2 = st.columns(2)

with col1:
    st.image("butterfly.png")

with col2:
    st.write("Name: Rea May M. Villanueva")
    st.write("Course: BSCS 3B")

st.success("Simple Streamlit Multipage App")
