import requests

def fetch_weather(city, api_key):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'APPID': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response



