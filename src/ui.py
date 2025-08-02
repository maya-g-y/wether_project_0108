import streamlit as st

def show_weather(data, city):
    if data["cod"] == 200:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']

        st.subheader(f"Weather in {city}")
        st.markdown("### ☁️ Weather Summary")
        st.table({
            "Temperature (°C)": [temperature],
            "Humidity (%)": [humidity],
            "Conditions": [description]
        })
    else:
        st.error("City not found or API error. Please check the city name.")
