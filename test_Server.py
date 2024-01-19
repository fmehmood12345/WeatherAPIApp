import unittest

from unittest.mock import patch
from Server import app, determine_umbrella_need
from Utilities import get_weather_api_url, get_local_server_api_url, get_response


class TestWeatherApp(unittest.TestCase):


    def test_determine_umbrella_need(self):
        # Test the determine_umbrella_need function
        cloudy_weather = {'Description': 'Cloudy'}
        rainy_weather = {'Description': 'Rain'}
        sunny_weather = {'Description': 'Sunny'}

        self.assertEqual(determine_umbrella_need(cloudy_weather), "You should take an umbrella :(")
        self.assertEqual(determine_umbrella_need(rainy_weather), "You should take an umbrella :(")
        self.assertEqual(determine_umbrella_need(sunny_weather), "You don't need an umbrella :)")


if __name__ == '__main__':
    unittest.main()
