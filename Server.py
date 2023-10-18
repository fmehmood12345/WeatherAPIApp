# Import necessary modules and libraries
from flask import Flask
from flask_restful import Api, Resource
import requests

# Create a Flask application
app = Flask(__name__)
api = Api(app)


# Create a Resource class for handling the weather data
class weather(Resource):
    # Define a method for handling HTTP GET requests
    def get(self, city):
        # Define your OpenWeatherMap API key
        api_key = '063778e183000493832b73cd4be50766'

        # Create the API URL to fetch weather data for the specified city
        api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

        # Send an HTTP GET request to the OpenWeatherMap API
        response = requests.get(api_url)

        # Parse the JSON response into a Python dictionary
        data = response.json()

        weather_data = {'City': data['name'],
                        'Temperature': data['main']['temp'],
                        'Description': data['weather'][0][
                            'description']}  # [0] because there is only 1 index for weather
        return weather_data


# Add the weather Resource to the API and define the route for accessing it
api.add_resource(weather, '/weather/<string:city>')

# Run the Flask application in debug mode if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
