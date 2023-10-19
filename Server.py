# Import necessary modules and libraries
from flask import Flask
from flask_restful import Api, Resource
import requests
from constants import get_response, get_weather_api_url

# Create a Flask application
app = Flask(__name__)
api = Api(app)


# Create a Resource class for handling the weather data
class weather(Resource):
    # Define a method for handling HTTP GET requests
    def get(self, city):

        #Getting the api url from constants file.
        API_URL = get_weather_api_url(city)

        # Send an HTTP GET request to the OpenWeatherMap API and put it in json format ie. python dictionary
        response = (get_response(API_URL)).json()

        # Parse the JSON response into a Python dictionary
        #data = response.json()

        weather_data = {'City': response['name'],
                        'Temperature': response['main']['temp'],
                        'Description': response['weather'][0][
                            'description']}  # [0] because there is only 1 index for weather
        return weather_data


# Add the weather Resource to the API and define the route for accessing it
api.add_resource(weather, '/weather/<string:city>')

# Run the Flask application in debug mode if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
