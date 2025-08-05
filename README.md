
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

## 🚀 Install & Run via Poetry
This project uses [Poetry](https://python-poetry.org) for dependency management.
1. **Clone the repository**
```bash
git clone https://github.com/your-username/weather_project_0108.git
cd weather_project_0108
```
2. **Install Poetry (if you don’t already have it)**
```bash
pip ipip install poetry
```
3. **Install dependencies**
```bash
poetry install
```
4. **Run the app**
```bash
poetry run streamlit run app.py
```

## 📁Project Structure
```bash
weather_project_0108/
│
├── app.py                 # Main Streamlit entry point
├── pyproject.toml         # Poetry configuration + dependencies
├── poetry.lock            # Exact locked versions
├── README.md              # Project documentation
├──.gitignore              # Git ignore rules
└── src/
    ├── data.py            # Fetches weather data from the API
    └── ui.py              # UI logic: display weather, time, map, etc.               # UI logic: display weather, time, map, etc.
```

## 📦Dependencies
Managed by Poetry in pyproject.toml. Key packages:
- streamlit
- requests
- folium
- streamlit-folium
- pytz


## 👩 Author
Created by Maya Geva. 
This app was built as part of a project to learn and practice Python, API handling, and Streamlit.

