import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def get_weather():

    city = input("Enter city name: ")

    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=yes"

    try:

        response = requests.get(url)

        data = response.json()

        if response.status_code == 200:

            print("\n===== Weather Information =====\n")

            print(f"City: {data['location']['name']}")
            print(f"Country: {data['location']['country']}")
            print(f"Temperature: {data['current']['temp_c']}°C")

        else:
            print("Error:", data["error"]["message"])

    except Exception as e:
        print(f"Error: {e}")


get_weather()