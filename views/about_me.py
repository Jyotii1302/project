import streamlit as st
from forms.contact import contact_form

@st.experimental_dialog("Contact Me")
def show_contact_form():
    contact_form()

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile_image.png", width=230)  # Replace with your profile image path

with col2:
    st.title("Jyoti Houdhary", anchor=False)
    st.write(
        "Currently pursuing Integrated B.Tech in MTE at Lovely Professional University, Phagwara, Punjab, India. "
        "I have a keen interest in AI, ML, NLP, and Deep Learning."
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - Strong knowledge and hands-on experience in AI and Machine Learning
    - Understanding of Natural Language Processing and Deep Learning techniques
    - Excellent team player with a proactive approach to tasks
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: Python (Scikit-learn, Pandas), SQL
    - Data Visualization: Streamlit, Plotly, Matplotlib
    - Machine Learning: Supervised and Unsupervised Learning, Neural Networks
    - Tools: Jupyter Notebook, Git
    """
)

# --- FEEDBACK SECTION ---
st.write("\n")
st.subheader("Feedback")
st.write("If you have any suggestions, compliments, or modifications, feel free to contact me using the form below.")

if st.button("💬 Send Feedback"):
    show_contact_form()
