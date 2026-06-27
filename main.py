from voice import speak, listen
from assistant import ask_gemini
from commands import execute


def main():

    speak("Hello Navya.")

    speak("I am your AI Virtual Assistant.")

    while True:

        command = listen()

        if command == "":
            continue

        if "exit" in command:

            speak("Goodbye.")

            break

        result = execute(command)

        if result is None:

            answer = ask_gemini(command)

            speak(answer)

        else:

            speak(result)


if __name__ == "__main__":

    main()