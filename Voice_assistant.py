import speech_recognition as sr
import pyttsx3
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    print("Processing command:", command)
    command = command.lower()  # Convert to lowercase once

    if "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com/")
    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com/")
    elif "chatgpt" in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com")
    else:
        speak("I heard " + command)


if __name__ == "__main__":
    speak("Initializing Jarvis")
    while True:
        try:
            with sr.Microphone() as source:
                print("Say the wake word...")
                audio = recognizer.listen(source)

            word = recognizer.recognize_google(audio)
            print("You said:", word)

            if word.lower() == "jarvis":
                speak("Yes, jaravis  is  listening")
            

                with sr.Microphone() as source:
                    print("Listening for your command...")
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                print("Command received:", command)

                speak("You said " + command)
                processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio")
            speak("Sorry, I didn't catch that.")

        except sr.RequestError as e:
            print(f"Speech Recognition error: {e}")
            speak("There was a problem connecting to the speech service.")
