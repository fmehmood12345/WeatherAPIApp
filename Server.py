# Import necessary modules and libraries
from flask import Flask
from fastapi import FastAPI, Depends, HTTPException, Query
import requests
from Utilities import get_response, get_weather_api_url
from pydantic import BaseModel


# Create a Flask application
app = FastAPI()

def determine_umbrella_need(weather_description: str) -> str:
    if ("Clouds" or "clouds" or "Rain" or "rain") in weather_description:
        return "You should take an umbrella :("
    else:
        return "You don't need an umbrella :)"

# Define a method for handling HTTP GET requests
@app.get("/weather/{city}")
def get_weather(city: str):
    # Getting the API URL from the utility function
    api_url = get_weather_api_url(city)

    # Send an HTTP GET request to the OpenWeatherMap API and put it in JSON format (Python dictionary)
    response = get_response(api_url).json()

    # Check if "clouds" or "rain" is in the description
    weather_description = response.get('Description', '').lower()

    # Determine umbrella need and get the message
    message = determine_umbrella_need(weather_description)

    # Return a JSON response with the message
    return {"message": message}


# Run the Flask application in debug mode if this script is executed
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
