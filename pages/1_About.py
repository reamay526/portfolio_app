import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #74ebd5, #ACB6E5);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("About Me")

st.write("""
I am Rea May M. Villanueva, a BSCS student currently learning programming and web development.
""")

st.subheader("Education")
st.write("Bachelor of Science in Computer Science")

st.subheader("Interest")
st.write("- Programming")
st.write("- Web Development")
st.write("- UI Design")
