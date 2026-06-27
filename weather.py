import requests

API_KEY = "YOUR_OPENWEATHER_KEY"


def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    data = response.json()

    if data.get("cod") != 200:
        return "Sorry, I couldn't find that city."

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    return f"The temperature in {city} is {temp} degrees Celsius with {desc}."