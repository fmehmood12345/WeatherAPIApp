# Import the 'requests' module for making HTTP requests
import requests

# Define the base URL for your Flask server
"""This URL represents the server's location and port. 
Let's break it down: 
    http:// is the protocol for making HTTP requests.
    127.0.0.1 is the IP address that refers to the local machine (your own computer). 
    
In the context of client and server applications running on the same computer, this IP address is used to refer to the 
machine itself. 

:5000 is the port number on which the Flask server is running. Flask, by default, runs on port 5000 when you use 
app.run() without specifying a different port. This port is where the Flask server listens for incoming requests. """

Base = "http://127.0.0.1:5000"

# Prompt the user to enter a city name
city = input("Please enter your city: ")

# Send an HTTP GET request to the Flask server, specifying the city as part of the URL
response = requests.get(f"{Base}/weather/{city}")

# Parse the JSON response from the server and print it
# print(response.json())

# Check if "Cloudy" or "cloudy" is in the description (case-insensitive)
if "Clouds" in response.json()['Description'] or "clouds" in response.json()['Description'] or "Rain" in \
        response.json()['Description'] or "rain" in response.json()['Description']:
    print("---------------------------------")
    print("You should take an umbrella :(")
    print("---------------------------------")
else:
    print("---------------------------------")
    print("You don't need an umbrella :)")
    print("---------------------------------")



# UNDERSTANDING JSON DATA
#Code:
"""
{  'City': data['name'], 
    'Temperature': data['main']['temp'],
    'Description': data['weather'][0]['description']
}
"""

#Data:
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
