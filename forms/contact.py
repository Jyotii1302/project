import re
import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Function to validate email addresses
def is_valid_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

# Function to connect to Google Sheets
def connect_to_sheets():
    # Load credentials from Streamlit secrets
    json_key = st.secrets["google_service_account"]

    # Load credentials from the JSON content
    creds = ServiceAccountCredentials.from_json_keyfile_dict(json_key, 
                                                             ['https://spreadsheets.google.com/feeds', 
                                                              'https://www.googleapis.com/auth/drive'])
    client = gspread.authorize(creds)

    # Open the spreadsheet using its URL
    spreadsheet_url = "https://docs.google.com/spreadsheets/d/1oD27TYdwUgwSj4SGXLOwPOHNHYB4k01pft_hzSP7o7o/edit?usp=sharing"  # Your Google Sheet URL
    sheet = client.open_by_url(spreadsheet_url).sheet1  # Access the first sheet

    return sheet

# Function to display the contact form and handle submissions
def contact_form():
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Send Message")

    if submit_button:
        # Validate input fields
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

        # Connect to Google Sheets and append data
        sheet = connect_to_sheets()
        row = [name, email, message]  # Prepare the row to be added
        sheet.append_row(row)  # Append the data to the sheet

        st.success("Thank you for your message! 🎉")

# Run the contact form function
if __name__ == "__main__":
    st.title("Contact Form")
    contact_form()
