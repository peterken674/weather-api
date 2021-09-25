import urllib.request, json
from . import models
from django.conf import settings

# Global variables
api_key = settings.API_KEY
base_url = 'https://api.weatherapi.com/v1/forecast.json?key={}&q={}&days={}&aqi=no&alerts=no'

# Fetch data
def fetch_data(city, number_of_days):
    """Fetch temperatures from Weather API

    Args:
        city (str): The city passed by the user to search data for.
        number_of_days (int): Number of days to fetch data for (up to 10 days)

    Returns:
        temperatures ([obj]): List of temperatures for the specified days
    """

    # Build the request URL
    request_url = base_url.format(api_key, city, number_of_days)

    with urllib.request.urlopen(request_url) as url:
        data = url.read()
        response = json.loads(data) #Convert to JSON

        temperatures = []

        if response['location']:
            forecast_results_list = response['forecast']['forecastday']
            temperatures = process_results(forecast_results_list)

    return temperatures

# Process API response