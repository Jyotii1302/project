import re
import streamlit as st
import requests  # Make sure requests is installed via pip

WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def feedback_form():
    with st.form("feedback_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email Address")
        feedback = st.text_area("Your Feedback")
        submit_button = st.form_submit_button("Send Feedback")

    if submit_button:
        if not WEBHOOK_URL:
            st.error("Feedback service is not set up. Please try again later.", icon="📧")
            st.stop()

        if not name:
            st.error("Please provide your name.", icon="🧑")
            st.stop()

        if not email:
            st.error("Please provide your email address.", icon="📨")
            st.stop()

        if not is_valid_email(email):
            st.error("Please provide a valid email address.", icon="📧")
            st.stop()

        if not feedback:
            st.error("Please provide your feedback.", icon="💬")
            st.stop()

        # Prepare the data payload and send it to the specified webhook URL
        data = {"email": email, "name": name, "feedback": feedback}
        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 200:
            st.success("Thank you for your feedback! 🎉", icon="🚀")
        else:
            st.error("There was an error sending your feedback. Please try again later.", icon="😨")

# To use the feedback_form function, call it in your main app file
