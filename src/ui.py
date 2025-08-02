import streamlit as st
import folium
from streamlit_folium import folium_static

def show_weather(data, city):
    if data["cod"] == 200:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        icon_code = data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

        lat = data['coord']['lat']
        lon = data['coord']['lon']

        st.subheader(f"Weather in {city}")
        st.image(icon_url, width=100)
        st.markdown("### ☁️ Weather Summary")

        col1, col2, col3 = st.columns(3)
        col1.metric("🌡️ Temperature (°C)", f"{temperature}°")
        col2.metric("💧 Humidity (%)", f"{humidity}%")
        col3.metric("☁️ Conditions", description.capitalize())

        st.markdown('### 🗺️Location Map')
        m = folium.Map(location=[lat, lon], zoom_start=12)
        folium.Marker([lat, lon], popup=city).add_to(m)
        folium_static(m)

    else:
        st.error("City not found or API error. Please check the city name.")
