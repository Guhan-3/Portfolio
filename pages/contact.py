import streamlit as st
from send_email import send_mail

st.title("Contact Me")

with st.form(key="email"):
    user_email = st.text_input("Your Mail ID")
    raw_message = st.text_area("Your Message")
    message = f"""\
Subject:Email from {user_email}

From: {user_email}
{raw_message}
    """
    button = st.form_submit_button("Submit")

    if button:
        send_mail(message)
        st.info("Mail Sent Successfully")
