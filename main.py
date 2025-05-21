import   speech_recognition as sr 
import webbrowser
import pyttsx3
import pocketsphinx


recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak (text):
    engine.say(text)
    engine.runAndWait()



if __name__ =="__main__":
    speak("Initializing sister ")
    while True:
        # listen for the wake word jarvis 
        r = sr.Recognizer()
        with sr.Microphone()as source :
            print("say Something")
            audio = r.listen(source)

        command = r.recognize_google
        (audio)
        print(command)

        #recognixer speech using sphinx  

        
        print(" Sphinx thinks you said  " + r.recognize_google(audio))
        sr.UnknownValueError 
        print("sphinx could not understand audio ")
        sr.RequestError 
        print("sphinx error  {0}.format(e)")
