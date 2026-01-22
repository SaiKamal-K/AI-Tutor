import streamlit as st
import google.generativeai as genai

# Load API key from Streamlit secrets
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# System instruction
system_prompt = """You are a Python code reviewer.
Review the code, identify errors, suggest improvements,
and give a rating out of 5. Only accept Python code as input."""

# Initialize Gemini model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=system_prompt
)

# UI
st.title("🚀 Python Code Reviewer with Gemini AI")
st.write("Enter your Python code snippet below.")

user_prompt = st.text_area("📌 Enter your Python code:", height=250)

if st.button("🔍 Review Code"):
    if user_prompt.strip():
        with st.spinner("Reviewing your code... ⏳"):
            response = model.generate_content(user_prompt, stream=True)

        st.subheader("✅ AI Review:")
        for chunk in response:
            if chunk.text:   # IMPORTANT
                st.write(chunk.text)
    else:
        st.warning("⚠ Please enter a Python code snippet first.")
