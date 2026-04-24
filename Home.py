import streamlit as st

st.set_page_config(page_title="My Portfolio", layout="wide")

# ================= THEME (YOUR COLORS) =================
st.markdown(
    """
    <style>

    .stApp {
        background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
    }

    html, body, .stApp, p, div, span, label {
        color: #000000 !important;
    }

    h1, h2, h3 {
        color: #3b1b5a;
    }

    section[data-testid="stSidebar"] {
        background-color: rgba(255,255,255,0.9);
    }

    .stButton > button {
        background-color: #3b1b5a;
        color: white;
        border-radius: 10px;
    }

    .stButton > button:hover {
        background-color: #ff4fa3;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ================= SIDEBAR =================
with st.sidebar:
    st.markdown("## 🌸 Portfolio")

    page = st.radio(
        "Navigation",
        ["🏠 Home", "🙋 About", "💼 Projects", "📩 Contact"]
    )

    st.markdown("---")
    st.write("BSCS 3B")
    st.write("Aspiring Developer")

# ================= HOME =================
if page == "🏠 Home":

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("mayie.png", width=180)

    with col2:
        st.title("Welcome to My Portfolio")
        st.subheader("Rea May M. Villanueva")
        st.write("BSCS 3B")
        st.markdown("### Aspiring Developer & Designer")
        st.write("Interested in Web Development")

    st.markdown("---")

    if st.button("Say Hello"):
        st.success("Thanks for visiting my portfolio!")

elif page == "🙋 About":
    st.title("About Me")
    st.write("See About page")

elif page == "💼 Projects":
    st.title("Projects")
    st.write("See Projects page")

elif page == "📩 Contact":
    st.title("Contact")
    st.write("See Contact page")
