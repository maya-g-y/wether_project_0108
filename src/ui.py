def show_weather(response, city):
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        print(f"\nWeather in {city}: ")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Description: {description}")
    else:
        print(f"\nWeather in {city} failed with status code: {response.status_code}")
