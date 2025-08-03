import streamlit as st
from datetime import datetime
import pytz
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

        st.markdown("### 🕒 Time Information")
        user_timezone = "Asia/Jerusalem"
        city_timezone = get_timezone_by_city(city)

        try:
            user_time = datetime.now(pytz.timezone(user_timezone))
            city_time = datetime.now(pytz.timezone(city_timezone))

            formatted_user_time = user_time.strftime("%A, %B %d, %Y, %I:%M %p")
            formatted_city_time = city_time.strftime("%A, %B %d, %Y, %I:%M %p")

            st.write(f"🧍 Your local time: **{formatted_user_time}**")
            st.write(f"📍 Time in {city}: **{formatted_city_time}**")
        except Exception as e:
            st.warning("⚠️ Timezone information not available.")

        st.markdown('### 🗺️Location Map')
        m = folium.Map(location=[lat, lon], zoom_start=12)
        folium.Marker([lat, lon], popup=city).add_to(m)
        folium_static(m)

    else:
        st.error("City not found or API error. Please check the city name.")


def get_timezone_by_city(city):
    mapping = {
        "new york": "America/New_York",
        "london": "Europe/London",
        "tel aviv": "Asia/Jerusalem",
        "paris": "Europe/Paris",
        "tokyo": "Asia/Tokyo",
        "sydney": "Australia/Sydney"

    }
    return mapping.get(city.lower(), "UTC")
