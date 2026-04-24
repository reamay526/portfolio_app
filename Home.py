import streamlit as st

st.set_page_config(page_title="My Portfolio", layout="wide")

# ===== THEME =====
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        color: white;
    }

    h1, h2, h3 {
        color: #ff4d6d;
    }

    .stButton > button {
        background-color: #6a0dad;
        color: white;
        border-radius: 8px;
        border: none;
    }

    .stButton > button:hover {
        background-color: #ff4d6d;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===== SIDEBAR =====
with st.sidebar:
    st.markdown("<h2 style='color:#ff4d6d;'>🌸 My Portfolio</h2>", unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        ["🏠 Home", "🙋 About", "💼 Projects", "📩 Contact"]
    )

    st.markdown("---")
    st.write("BSCS 3B")
    st.write("Aspiring Developer")

# ===== HOME CONTENT =====
if page == "🏠 Home":
    col1, col2 = st.columns(2)

    with col1:
        st.title("Welcome to My Portfolio")
        st.subheader("Rea May M. Villanueva")
        st.write("BSCS 3B")
        st.markdown("### Aspiring Developer & Designer")
        st.write("Interested in Web Development")

        if st.button("Say Hello"):
            st.success("Thanks for visiting!")

    with col2:
        st.image("mayie.png
        ", width=200)

elif page == "🙋 About":
    st.title("About Me")
    st.write("I am a Computer Science student passionate about web development and design.")

elif page == "💼 Projects":
    st.title("Projects")
    st.write("• Portfolio App\n• Web Projects\n• School Systems")

elif page == "📩 Contact":
    st.title("Contact Me")

    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    if st.button("Send"):
        if name and email and message:
            st.success("Message sent successfully!")
        else:
            st.error("Please complete all fields.")
