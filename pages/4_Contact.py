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

st.title("Contact Me")

with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")

    submit = st.form_submit_button("Send")

    if submit:
        if name and email and message:
            st.success("Message sent successfully! ✅")
        else:
            st.error("Please fill all fields.")

st.markdown("### Social Links")
st.write("- GitHub: https://github.com/reamay526")
st.write("- Facebook: https://www.facebook.com/rea.villanueva.9277")
