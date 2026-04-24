import streamlit as st

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #3b1b5a, #e6e6e6, #ff4fa3);
}

.block-container {
    padding-top: 3rem;
}

html, body, .stApp {
    color: #000000 !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Contact Me")

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")

if st.button("Send"):
    if name and email and message:
        st.success("Message sent successfully!")
    else:
        st.error("Please fill all fields")
        
st.write("GitHub: https://github.com/reamay526")
st.write("Facebook: https://www.facebook.com/rea.villanueva.9277")
