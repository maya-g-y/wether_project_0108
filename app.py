import streamlit as st
from src.data import fetch_weather
from src.ui import show_weather

st.set_page_config(page_title="Weather Checker", page_icon="🌦️")

st.title('Weather App')

API_KEY = "5961cc2151e8c770260cde5abdd694aa"
with st.form(key="weather_form"):
    city = st.text_input("Enter the city name")
    submit = st.form_submit_button("Get Weather")

if submit and city:
    response = fetch_weather(city, API_KEY)
    data = response.json()
    show_weather(data, city)
