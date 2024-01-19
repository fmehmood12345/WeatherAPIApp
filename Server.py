# Import necessary modules and libraries
from flask import Flask
from fastapi import FastAPI, Depends, HTTPException, Query
import requests
from Utilities import get_response, get_weather_api_url
from pydantic import BaseModel


# Create a Flask application
app = FastAPI()

def determine_umbrella_need(weather_description):
    # # Check if "Cloudy" or "cloudy" is in the description (case-insensitive)
    if "Clouds" in weather_description['Description'] or "clouds" in weather_description['Description'] or "Rain" in weather_description['Description'] or "rain" in weather_description['Description']:
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

    weather_data = {'City': response['name'],
                    'Temperature': response['main']['temp'],
                    'Description': response['weather'][0][
                        'description']}  # [0] because there is only 1 index for weather

    # Determine umbrella need and get the message
    message = determine_umbrella_need(weather_data)

    # Return a JSON response with the message
    return {"message": message}


# Run the Flask application in debug mode if this script is executed
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    # How to run: http://127.0.0.1:8000/docs add docs to the end
