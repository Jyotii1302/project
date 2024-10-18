import streamlit as st
from forms.contact import contact_form

# Function to display contact form
def show_contact_form():
    contact_form()

# --- HERO SECTION ---
col1, col2 = st.columns([1, 3])  # Adjusted column proportions for better layout
with col1:
    # Using the original image path as requested
    st.image("profile_image.jpg", width=150)

with col2:
    st.title("Jyoti Houdhary")
    st.write(
        "Currently pursuing Integrated B.Tech in MTE at Lovely Professional University, Phagwara, Punjab, India. "
        "I have a keen interest in AI, ML, NLP, and Deep Learning."
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications")
st.write(
    """
    - Strong knowledge and hands-on experience in AI and Machine Learning
    - Understanding of Natural Language Processing and Deep Learning techniques
    - Excellent team player with a proactive approach to tasks
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills")
st.write(
    """
    - Programming: Python (Scikit-learn, Pandas), SQL
    - Data Visualization: Streamlit, Plotly, Matplotlib
    - Machine Learning: Supervised and Unsupervised Learning, Neural Networks
    - Tools: Jupyter Notebook, Git
    """
)

# --- CONTACT FORM SECTION ---
st.write("\n")
st.subheader("Contact Form")
st.write("If you'd like to reach out, feel free to contact me using the form below.")

if st.button("💬 Contact Me"):
    show_contact_form()
