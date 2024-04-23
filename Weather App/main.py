
import tkinter as tk
from datetime import datetime
import requests

# API key for OpenWeatherMap
API_KEY = "3c26067d2afe8365a6463001adb3e791"

# Base URL for OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"


def get_weather(city):
    """
    Retrieve weather data for a given city from OpenWeatherMap API
    """
    try:
        # API request to OpenWeatherMap
        url = BASE_URL + "q=" + city + "&appid=" + API_KEY
        response = requests.get(url)
        data = response.json()

        # Extract relevant weather data from response
        location = f"{data['name']}, {data['sys']['country']}"
        description = data['weather'][0]['description'].title()
        temperature = data['main']['temp'] - 273.15  # Kelvin to Celsius
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Convert Unix timestamps to local time
        sunrise_unix = data['sys']['sunrise']
        sunrise_time = datetime.fromtimestamp(sunrise_unix).strftime("%H:%M:%S")
        sunset_unix = data['sys']['sunset']
        sunset_time = datetime.fromtimestamp(sunset_unix).strftime("%H:%M:%S")

        return {
            'location': location,
            'description': description,
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'sunrise_time': sunrise_time,
            'sunset_time': sunset_time
        }

    except Exception as e:
        # Handle invalid city input or API errors
        return {'error': str(e)}


def format_output(weather_data):
    """
    Format the weather data as a string for display
    """
    if 'error' in weather_data:
        return f"Error: {weather_data['error']}"

    location = weather_data['location']
    description = weather_data['description']
    temperature = f"{weather_data['temperature']:.2f}°C"
    humidity = f"{weather_data['humidity']}%"
    wind_speed = f"{weather_data['wind_speed']} m/s"
    sunrise_time = weather_data['sunrise_time']
    sunset_time = weather_data['sunset_time']

    return f"Location: {location}\n" \
           f"Conditions: {description}\n" \
           f"Temperature: {temperature}\n" \
           f"Humidity: {humidity}\n" \
           f"Wind Speed: {wind_speed}\n" \
           f"Sunrise: {sunrise_time}\n" \
           f"Sunset: {sunset_time}"


def get_weather_for_city(event=None):
    """
    Retrieve weather data for the city entered by the user
    """
    city = city_entry.get()
    weather_data = get_weather(city)
    output = format_output(weather_data)
    result_label.config(text=output)


# Create a Tkinter window
root = tk.Tk()
root.title("Weather App")
root.bind("<Return>", get_weather_for_city)
root.geometry("400x300")

# Create input field for city
city_label = tk.Label(root, text="Enter city name:", pady=20, font=("Arial", 10, "bold"))
city_label.pack()
city_entry = tk.Entry(root, width=30)
city_entry.pack()

# Create button to get weather
get_weather_button = tk.Button(root, text="Get Weather", bg="#ADD8E6", padx=10, command=get_weather_for_city, font=("Arial", 10, "bold"))
get_weather_button.pack()


# Create label to display weather information
result_label = tk.Label(root, text="", wraplength=600, justify="left", padx=10, pady=10, font=("Arial", 10, "bold"))
result_label.pack()

# Run the Tkinter event loop
root.mainloop()
