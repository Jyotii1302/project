import streamlit as st

# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)

pcos_detection_page = st.Page(
    "views/app.py",  
    title="PCOS Detection",
    icon=":material/medical_services:", 

chatbot_page = st.Page(
    "views/chatbot.py",  
    title="Menstrual Health Chatbot",
    icon=":material/smart_toy:",
)

# --- NAVIGATION SETUP [WITH SECTIONS] ---
pg = st.navigation(
    {
        "Info": [about_page],  # About Me section
        "Projects": [pcos_detection_page, chatbot_page],  # Projects section with PCOS and Chatbot
    }
)

# --- SHARED ON ALL PAGES ---
st.image("assets/profile_image.png", width=150)  # Assuming you have a profile image for About Me
st.sidebar.markdown("Made with ❤️ by [Jyoti Houdhary](https://github.com/JyotiHoudhary)")

# --- RUN NAVIGATION ---
pg.run()
