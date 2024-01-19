import requests
from Utilities import get_response, get_local_server_api_url

city = input("Please enter your city: ")

# Calling the function in Utilities.py which gets the endpoint for weather in local server, specifying the city as part
# of the URL
Local_Server_URL = get_local_server_api_url(city)

# Send an HTTP GET request to the Flask server, and puts it into json format
response = (get_response(Local_Server_URL)).json()
