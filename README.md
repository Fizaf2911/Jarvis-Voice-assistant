# 🤖 Jarvis Voice Assistant (Gemini API)

Jarvis is a **voice-controlled AI assistant** powered by **Google Gemini API**.  
It listens to your voice 🎤, processes your query with Gemini (`gemini-2.0-flash`), and responds back with speech 🔊.

---

## ✨ Features
- 🎙️ **Voice Input** (SpeechRecognition + microphone)
- 🧠 **AI Responses** using Gemini API
- 🔊 **Text-to-Speech** replies (pyttsx3)
- 🛑 Say **"exit"**, **"quit"**, or **"stop"** to end session

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/jarvis-gemini-assistant.git
cd jarvis-gemini-assistant
(Optional) Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install Dependencies
pip install -r requirements.txt


If you don’t have requirements.txt, install manually:

pip install google-generativeai SpeechRecognition pyttsx3 pyaudio


⚠️ Note: pyaudio may require extra setup:

Windows: pip install pipwin && pipwin install pyaudio

Linux (Ubuntu/Debian): sudo apt-get install portaudio19-dev python3-pyaudio

🔑 API Key Setup

Get your Gemini API key from Google AI Studio
.

Open client.py and replace:

genai.configure(api_key="API_KEY")


with your actual key:

genai.configure(api_key="YOUR_GEMINI_API_KEY")

▶️ Usage

Run the assistant:

python client.py


Jarvis will greet you:

Hello! I am Jarvis. How can I assist you today?


Then you can ask things like:

"What is the capital of Japan?"

"Tell me a fun fact."

"Summarize the latest tech news."

Say "exit", "quit", or "stop" to close the assistant.

📂 Project Structure
jarvis-gemini-assistant/
│── client.py        # Main assistant script
│── README.md        # Project documentation
│── requirements.txt # Python dependencies

🛠️ Requirements

Python 3.8+

Working microphone

Gemini API Key
