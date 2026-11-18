# 🎙️ Python Voice & Text-Based Wikipedia Chatbot

A Python-based interactive chatbot that allows users to search for information using either **text input or voice commands**. It retrieves information from Wikipedia and provides responses in both written and spoken formats.

This project was developed as a practical Python project during my second year of B.Tech in 2023.

##  Project Overview

The Python Voice & Text-Based Wikipedia Chatbot is designed to make information searching easier through human-computer interaction.

Users can interact with the chatbot in two ways:

- **Text Mode:** Type a question using the keyboard.
- **Voice Mode:** Ask a question through a microphone.

The chatbot processes the query, retrieves a relevant summary from Wikipedia, displays the result on the screen, and reads the answer aloud.

## ✨ Features

- 🎤 **Voice Input:** Recognizes spoken questions through a microphone.
- ⌨️ **Text Input:** Accepts questions typed through the keyboard.
- 📚 **Wikipedia Integration:** Retrieves information using the Wikipedia library.
- 🔊 **Text-to-Speech:** Converts answers into spoken responses.
- 🖥️ **Text Output:** Displays chatbot responses in the terminal.
- 🔄 **Interactive Interface:** Allows users to perform multiple searches in one session.
- ⚠️ **Error Handling:** Handles unclear speech, unavailable speech recognition services, and missing Wikipedia pages.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| SpeechRecognition | Voice input and speech recognition |
| PyAudio | Microphone audio input |
| pyttsx3 | Text-to-speech conversion |
| Wikipedia | Information retrieval |

## Project Structure

```text
python-voice-and-text-wikipedia-chatbot/
│
├── chatbot.py
├── README.md
└── requirements.txt
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/python-voice-and-text-wikipedia-chatbot.git
```

### 2. Navigate to the project folder

```bash
cd python-voice-and-text-wikipedia-chatbot
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you do not have a requirements.txt file, install the libraries manually:

```bash
pip install pyttsx3 wikipedia SpeechRecognition PyAudio
```

### 4. Run the chatbot

```bash
python chatbot.py
```

## 💻 How to Use

After running the program, the chatbot displays three options:

```text
===== WIKIPEDIA CHATBOT =====

1. Enter text
2. Speak using microphone
3. Exit

Choose an option:
```

**Option 1 – Text Input**

Enter a question using your keyboard.

Example:

```text
Enter your question: What is Artificial Intelligence?
```

**Option 2 – Voice Input**

Select option 2 and speak your question into the microphone.

Example:

```text
Listening... Speak now!
You said: What is Machine Learning?
```

**Chatbot Response**

The chatbot retrieves a Wikipedia summary, displays it in the terminal, and reads it aloud.

**Option 3 – Exit**

Closes the chatbot.

## 🔄 How It Works

```text
        User Interaction
               |
       -----------------
       |               |
    Text Input     Voice Input
       |               |
       |        Speech Recognition
       |               |
       ------- Query ---
               |
       Wikipedia Search
               |
        Retrieve Summary
               |
       -----------------
       |               |
    Text Output    Speech Output
       |               |
       ------- End -----
```

## Requirements

- Python 3.x
- Working microphone for voice input
- Internet connection for online speech recognition and Wikipedia searches
- Speakers or headphones for spoken responses

## 🎯 Learning Outcomes

Through this project, I gained practical experience in:

- Python programming and functions.
- Integrating external Python libraries.
- Speech recognition and voice-based interaction.
- Text-to-speech implementation.
- Retrieving information from external sources.
- Building interactive command-line applications.
- Handling errors and user input.

## Future Improvements

- Integrate an AI-powered conversational model.
- Add a graphical user interface (GUI).
- Support multiple languages.
- Improve speech recognition accuracy.
- Add conversation history.
- Integrate additional knowledge sources.

