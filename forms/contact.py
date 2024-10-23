import re
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# Function to validate email format
def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

# Function to connect to Google Sheets
def connect_to_gsheet():
    # Load the JSON key from Streamlit secrets
    json_key = st.secrets["GOOGLE_SHEET_JSON"]
    creds = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(json_key), scope=["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"])
    
    client = gspread.authorize(creds)
    sheet = client.open("Your Google Sheet Name").sheet1  # Replace with your actual sheet name
    return sheet

# Contact form function
def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Send Message")

    if submit_button:
        if not name:
            st.error("Please provide your name.", icon="🧑")
            st.stop()

        if not email:
            st.error("Please provide your email address.", icon="📨")
            st.stop()

        if not is_valid_email(email):
            st.error("Please provide a valid email address.", icon="📧")
            st.stop()

        if not message:
            st.error("Please provide your message.", icon="💬")
            st.stop()

        # Connect to Google Sheets and append the data
        sheet = connect_to_gsheet()
        sheet.append_row([name, email, message])  # Add the new row to the sheet

        st.success("Thank you for your message! 🎉", icon="🚀")

# Call the contact_form function in your main app
if __name__ == "__main__":
    st.title("Contact Form")
    contact_form()
