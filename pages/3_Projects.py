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

st.title("Projects")

projects = {
    "Attendance System": "Simple attendance tracking system.",
    "Portfolio Website": "Streamlit multipage application.",
    "Banking System": "Basic transaction simulation."
}

for title, desc in projects.items():
    with st.expander(title):
        st.write(desc)
