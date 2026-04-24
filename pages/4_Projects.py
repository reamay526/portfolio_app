import streamlit as st

st.title("Projects")

projects = [
    "Attendance System",
    "Portfolio Website",
    "Banking System"
]

for project in projects:
    st.write("✔", project)