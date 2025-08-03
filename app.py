import streamlit as st
from datetime import datetime
from src.data import fetch_weather
from src.ui import show_weather, get_timezone_by_city


st.set_page_config(page_title="Weather Checker", page_icon="🌦️")

st.title('🌦️Weather App')

API_KEY = "5961cc2151e8c770260cde5abdd694aa"

if "search_history" not in st.session_state:
    st.session_state.search_history = []

with st.form(key="weather_form"):
    city = st.text_input("Enter the city name")
    submit = st.form_submit_button("Get Weather")

if submit and city:
    response = fetch_weather(city, API_KEY)
    data = response.json()

    if data["cod"] == 200:
        show_weather(data, city)

        st.session_state.search_history.append({
            "city": city,
            "temperature": data['main']['temp'],
            "description": data['weather'][0]['description'].capitalize(),
            "time": datetime.now().strftime("%H:%M")
        })
    else:
        st.error("City not found or API error.")

st.sidebar.title("🕘 Search History")

if st.sidebar.button("🗑️ Clear History"):
    st.session_state.search_history.clear()

if st.session_state.search_history:
    for item in reversed(st.session_state.search_history):
        st.sidebar.markdown(
            f"**{item['city']}** ({item['time']})  \n"
            f"{item['temperature']}°C – {item['description']}"
        )
else:
    st.sidebar.info("No searches yet.")
