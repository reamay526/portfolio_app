import streamlit as st

st.set_page_config(page_title="About")

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

    input, textarea {
        background-color: rgba(255,255,255,0.9) !important;
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

st.title("About Me")

st.write("I am a BSCS student learning programming and web development.")

st.subheader("Education")
st.write("Bachelor of Science in Computer Science")

st.subheader("Goals")
st.write("- Become a developer")
st.write("- Improve coding skills")
