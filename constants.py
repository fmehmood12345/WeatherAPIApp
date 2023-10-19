import requests

# Used to make endpoint for external weather server
def get_weather_api_url(city):
    # Define your OpenWeatherMap API key
    api_key = '063778e183000493832b73cd4be50766'

    # Create the API URL to fetch weather data for the specified city
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    return api_url

# Used to make endpoint for local server
def get_local_server_api_url(city):
    Base = 'http://127.0.0.1:5000'
    Local_Server_URL = f"{Base}/weather/{city}"
    return Local_Server_URL


# Used to get response from local or external servers
def get_response(url):
    response = requests.get(url)
    return response


# Define the base URL for your Flask server
"""This URL represents the server's location and port. 
Let's break it down: 
    http:// is the protocol for making HTTP requests.
    127.0.0.1 is the IP address that refers to the local machine (your own computer). 

In the context of client and server applications running on the same computer, this IP address is used to refer to the 
machine itself. 

:5000 is the port number on which the Flask server is running. Flask, by default, runs on port 5000 when you use 
app.run() without specifying a different port. This port is where the Flask server listens for incoming requests. """

# UNDERSTANDING JSON DATA
# Code:
"""
{  'City': data['name'], 
    'Temperature': data['main']['temp'],
    'Description': data['weather'][0]['description']
}
"""

# Data:
"""
{ 
 'coord': {'lon': -74.006, 'lat': 40.7143}, 
 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 
 'base': 'stations', 
 'main': {'temp': 290.57, 'feels_like': 289.96, 'temp_min': 288.68, 'temp_max': 292.73, 'pressure': 1021, 'humidity': 61}, 
 'visibility': 10000, 'wind': {'speed': 2.06, 'deg': 240},
 'clouds': {'all': 100}, 
 'dt': 1697648878, 'sys': {'type': 2, 'id': 2008101, 'country': 'US', 'sunrise': 1697627397, 'sunset': 1697667129},
 'timezone': -14400, 'id': 5128581, 'name': 'New York', 'cod': 200
}
"""
