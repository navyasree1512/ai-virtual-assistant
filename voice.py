import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 170)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(text):
    print("Assistant:", text)
    engine.say(str(text))
    engine.runAndWait()


def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        command = recognizer.recognize_google(audio)

        print("You:", command)

        return command.lower()

    except:

        return ""