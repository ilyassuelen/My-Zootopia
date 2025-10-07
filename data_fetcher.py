import requests
import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()  # Loads the .env file

API_KEY = os.getenv("API_KEY")

def fetch_data(animal):
    animal_encoded = urllib.parse.quote(animal)  # encode name for URL
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_encoded}"
    headers = {"X-Api-Key": API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data if data else []
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []