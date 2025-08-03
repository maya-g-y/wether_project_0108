
# 🌦️ Weather App

A simple and interactive Streamlit web application that displays detailed weather information for any city around the world. The app is designed for general users who want to quickly view current weather conditions, location maps, local times, and more.

---

## ✨ Features

- 🔍 Input any city name to retrieve real-time weather data using the **OpenWeatherMap API**.
- 🌡️ Displays temperature, humidity, and conditions with matching **weather icons**.
- 🗺️ Interactive map of the location using **Folium**.
- 🧭 Shows both the **user's local time** and the **local time in the queried city**.
- 🕘 Maintains a searchable **search history** (with the ability to delete entries).
- 🎨 Visually organized layout using Streamlit's **columns, icons, and color formatting**.
- ♻️ Built with **modular code** for easy maintenance and future expansion.

---

## 🛠️ How to Run

1. **Clone the repository**
```bash
git clone https://github.com/your-username/weather_project_0108.git
cd weather_project_0108
```
2. **Install required packages**
```bash
pip install -r requirements.txt
```
3. **Run the application**
```bash
streamlit run app.py
```

## 📁Project Structure
```bash
weather_project_0108/
│
├── app.py                   # Streamlit app entry point
├── requirements.txt         # Python dependencies
├── README.md                # Project description
│
├── src/
│   ├── data.py              # Fetches weather data from API
│   └── ui.py                # UI logic: display weather, time, map, etc.
```

## 📦Dependencies
- streamlit
- requests
- folium
- streamlit-folium
- pytz


*All dependencies are listed in requirements.txt*

## 👩 Author
Created by Maya Geva. 
This app was built as part of a project to learn and practice Python, API handling, and Streamlit.

