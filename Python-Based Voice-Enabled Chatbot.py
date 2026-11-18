
import pyttsx3
import wikipedia
import speech_recognition as sr


engine = pyttsx3.init()


recognizer = sr.Recognizer()


# Function to speak the response
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to get voice input
def get_voice_input():
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query

    except sr.UnknownValueError:
        print("Sorry, I could not understand your voice.")
        speak("Sorry, I could not understand your voice.")
        return None

    except sr.RequestError:
        print("Speech recognition service is unavailable.")
        speak("Speech recognition service is unavailable.")
        return None


def chatbot():

    speak("Welcome to your personal Wikipedia assistant.")

    while True:
        print("\n===== WIKIPEDIA CHATBOT =====")
        print("1. Enter text")
        print("2. Speak using microphone")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            query = input("Enter your question: ")

        elif choice == "2":
            query = get_voice_input()

            if query is None:
                continue

        elif choice == "3":
            print("Goodbye!")
            speak("Goodbye! Have a nice day.")
            break

        else:
            print("Invalid choice. Try again.")
            continue

        try:
            print("\nSearching Wikipedia...")
            result = wikipedia.summary(query, sentences=3)

            print("\nChatbot Response:")
            print(result)

            speak(result)

        except wikipedia.exceptions.DisambiguationError:
            message = "Your search has multiple meanings. Please be more specific."
            print(message)
            speak(message)

        except wikipedia.exceptions.PageError:
            message = "Sorry, no Wikipedia page was found."
            print(message)
            speak(message)



if __name__ == "__main__":
    chatbot()
