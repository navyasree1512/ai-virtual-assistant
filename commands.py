import datetime
import wikipedia
import pywhatkit
import pyjokes
import webbrowser
import os

from weather import get_weather


def execute(command):

    if "time" in command:

        return datetime.datetime.now().strftime("%I:%M %p")

    elif "date" in command:

        return str(datetime.date.today())

    elif "wikipedia" in command:

        topic = command.replace("wikipedia", "")

        return wikipedia.summary(topic, sentences=2)

    elif "youtube" in command:

        song = command.replace("play", "")

        pywhatkit.playonyt(song)

        return "Playing on YouTube."

    elif "google" in command:

        query = command.replace("search", "")

        pywhatkit.search(query)

        return "Searching Google."

    elif "weather" in command:

        city = command.split()[-1]

        return get_weather(city)

    elif "joke" in command:

        return pyjokes.get_joke()

    elif "calculator" in command:

        return "Please ask calculations through Gemini."

    elif "open notepad" in command:

        os.system("notepad")

        return "Opening Notepad."

    elif "open youtube" in command:

        webbrowser.open("https://youtube.com")

        return "Opening YouTube."

    elif "open google" in command:

        webbrowser.open("https://google.com")

        return "Opening Google."

    else:

        return None