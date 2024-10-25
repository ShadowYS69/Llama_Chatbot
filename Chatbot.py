import streamlit as st
from groq import Groq

# Initialize the Groq client
client = Groq()

# Set up the Streamlit app layout
st.title("AI in Education: Bridging Learning Gaps")
st.subheader("How can AI help meet diverse learning needs?")

# Input text box for user learning challenges
user_input = st.text_area("Describe your learning needs or challenges:")

# Button to send the message
if st.button("Get Recommendations"):
    if user_input.strip():
        # Create chat completion request
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "user",
                    "content": f"How can AI help with the following learning needs: {user_input}?"
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )

        # Display the response
        response = ""
        for chunk in completion:
            response += chunk.choices[0].delta.content or ""
        st.write("AI Recommendations:")
        st.write(response)
    else:
        st.warning("Please describe your learning needs.")

# Section on diversity in learning
st.header("Understanding Diversity in Learning")
st.write("""
AI can help recognize different learning styles and preferences, ensuring inclusive education for all.
""")

# Feedback mechanism
st.header("Share Your Experience")
feedback = st.text_area("What are your thoughts on AI in education?")
if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")
