import streamlit as st

st.set_page_config(page_title="My Portfolio", layout="wide")

# ================= THEME =================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
        color: white;
    }

    h1, h2, h3 {
        color: #ff4d6d;
    }

    .stButton > button {
        background-color: #6a0dad;
        color: white;
        border-radius: 10px;
        border: none;
    }

    .stButton > button:hover {
        background-color: #ff4d6d;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ================= SIDEBAR =================
with st.sidebar:
    st.markdown("## 🌸 My Portfolio")

    page = st.radio(
        "Navigation",
        ["🏠 Home", "🙋 About", "💼 Projects", "📩 Contact"]
    )

    st.markdown("---")
    st.write("BSCS 3B")
    st.write("Aspiring Developer")

# ================= HOME PAGE =================
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
    st.info("Explore my portfolio using the sidebar.")

    if st.button("Say Hello"):
        st.success("Thanks for visiting!")

# ================= ABOUT =================
elif page == "🙋 About":
    st.title("About")
    st.write("KEEP YOUR ORIGINAL ABOUT TEXT FROM YOUR FILE")

# ================= PROJECTS =================
elif page == "💼 Projects":
    st.title("Projects")
    st.write("KEEP YOUR ORIGINAL PROJECT TEXT FROM YOUR FILE")

# ================= CONTACT =================
elif page == "📩 Contact":
    st.title("Contact")

    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    if st.button("Send"):
        if name and email and message:
            st.success("Message sent successfully!")
        else:
            st.error("Please fill all fields.")
