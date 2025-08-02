from src.data import fetch_weather
from src.ui import show_weather

API_KEY = "5961cc2151e8c770260cde5abdd694aa"

city = input("Enter the city name: ")
response = fetch_weather(city, API_KEY)
show_weather(response, city)


