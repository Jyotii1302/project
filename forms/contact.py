import re
import streamlit as st
import requests  # Make sure requests is installed via pip

WEBHOOK_URL = st.secrets["WEBHOOK_URL"]

def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email Address")
        message = st.text_area("Your Message")  # Changed feedback to message
        submit_button = st.form_submit_button("Send Message")  # Updated button text

    if submit_button:
        if not WEBHOOK_URL:
            st.error("Contact service is not set up. Please try again later.", icon="📧")
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

        if not message:  # Changed variable name to message
            st.error("Please provide your message.", icon="💬")
            st.stop()

        # Prepare the data payload and send it to the specified webhook URL
        data = {"email": email, "name": name, "message": message}  # Updated to use message
        response = requests.post(WEBHOOK_URL, json=data)

        if response.status_code == 200:
            st.success("Thank you for your message! 🎉", icon="🚀")  # Updated success message
        else:
            st.error("There was an error sending your message. Please try again later.", icon="😨")  # Updated error message

# To use the contact_form function, call it in your main app file
