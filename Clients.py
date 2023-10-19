# Import the 'requests' module for making HTTP requests
import requests
from constants import get_response, Base

# Prompt the user to enter a city name
city = input("Please enter your city: ")

Local_Server_URL = f"{Base}/weather/{city}"

# Send an HTTP GET request to the Flask server, specifying the city as part of the URL
response = get_response(Local_Server_URL)

# Parse the JSON response from the server and print it
#print(response.json())

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



