import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="🌐")

# STYLE INCLUDED
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #d9c2ff, #e6e6e6, #ffb3d9);
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
        background-color: rgba(255,255,255,0.8);
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
