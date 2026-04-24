import streamlit as st

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
            st.error("Please fill all fields")

st.markdown("### Social Links")
st.write("- GitHub:  https://github.com/reamay526")