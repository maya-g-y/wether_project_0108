import streamlit as st

def show_weather(data, city):
    if data["cod"] == 200:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        icon_code = data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

        st.subheader(f"Weather in {city}")
        st.image(icon_url, width=100)
        st.markdown("### ☁️ Weather Summary")

        col1, col2, col3 = st.columns(3)
        col1.metric("🌡️ Temperature (°C)", f"{temperature}°")
        col2.metric("💧 Humidity (%)", f"{humidity}%")
        col3.metric("☁️ Conditions", description.capitalize())

    else:
        st.error("City not found or API error. Please check the city name.")
