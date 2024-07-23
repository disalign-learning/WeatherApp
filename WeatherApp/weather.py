import requests
import json

BASE_URL = https://api.weather.gov/openapi.json

def get_weather(location):
    endpoint = f"{BASE_URL}{location}/forecast"

    response = requests.get(endpoint)

    if response.status_code == 200:
        return response.json
    else:
        return None

def main():
    location = input("What location in latitude/longitude do you want to check the weather?")
    forecast = get_weather(location)

    if forecast is not None:
        print(json.dumps(forecast,indent=4))
    else:
        print("Failed to fetch weather forecast.")
        
if __name__ == "__main__":
    main()