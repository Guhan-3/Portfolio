import streamlit as st
from send_email import send_mail

st.title("Contact Me")

with st.form(key="email"):
    user_email = st.text_input("Your Mail ID")
    topic = st.selectbox("what topic do you want to discuss?",
                         ("Python Basis", "Python Project", "Other Python Queries", "Other Information")
                         , placeholder="Select The Topic...")
    raw_message = st.text_area("Your Message")
    message = f"""\
Subject:Email from {user_email}

From: {user_email}
Topic: {topic}
{raw_message}
    """
    button = st.form_submit_button("Submit")

    if button:
        send_mail(message)
        st.info("Mail Sent Successfully")
