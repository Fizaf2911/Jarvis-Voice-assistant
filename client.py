import google.generativeai as genai
genai.configure(api_key="API_KEY")

# Initialize model (Gemini 2.0 Flash)
model = genai.GenerativeModel('gemini-2.0-flash')  # New faster model

# Generate response
response = model.generate_content("Explain how AI works in a few words")
print(response.text)