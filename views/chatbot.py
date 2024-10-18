import os
import nltk
import ssl
import streamlit as st
import random
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import json

# Ensure SSL context
ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

# Load intents from a JSON file
with open(r'C:\Users\User\NLP\intents.json', 'r') as file:
    intents = json.load(file)

tags = []
patterns = []

# Loop through the intents
for intent in intents['intents']:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# Create vectorizer and classifier
vectorizer = TfidfVectorizer()
clf = LogisticRegression(random_state=0, max_iter=10000)

# Transform patterns into TF-IDF features
X = vectorizer.fit_transform(patterns)
y = tags

# Train the classifier
clf.fit(X, y)

def chatbot(tag):
    """Return a random response for the given tag."""
    for intent in intents['intents']:
        if intent['tag'] == tag:
            response = random.choice(intent['responses'])
            return response

def typing_effect(response):
    """Simulate typing effect for the chatbot response."""
    typed_response = ""
    for char in response:
        typed_response += char
        time.sleep(0.05)  # Adjust the typing speed
        # Display the typed response as a string in a single line
        st.write(typed_response)

def main():
    st.title("MENSTRUAL HEALTH AWARENESS CHATBOT")
    st.write("WELCOME TO CHATBOT")
    
    # Initialize a session state to keep track of the last response
    if 'last_response' not in st.session_state:
        st.session_state.last_response = ""

    # Create buttons for each question
    for intent in intents['intents']:
        if st.button(intent['tag']):
            response = chatbot(intent['tag'])
            # Show the response immediately, while simulating typing
            with st.empty():  # Create a placeholder for typing effect
                typing_effect(response)
            st.session_state.last_response = response  # Save the last response

    # Display the last response below the buttons if any
    if st.session_state.last_response:
        st.write("Chatbot: " + st.session_state.last_response)

if __name__ == '__main__':
    main()
