import urllib.request
import json
from .models import Weather
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
        ([obj]): City and list of temperatures for the specified days, with their respective dates
    """

    # Build the request URL
    request_url = base_url.format(api_key, city, number_of_days)

    with urllib.request.urlopen(request_url) as url:
        data = url.read()
        response = json.loads(data)  # Convert to JSON

        temperatures = []

    if response['location']:
        city_name = response['location']['name']
        forecast_results_list = response['forecast']['forecastday']
        temperatures = process_results(forecast_results_list)

    return {"city": city_name, "temperatures": temperatures}

# Process API response


def process_results(results_list):
    """Map the results to the model.

    Args:
        results_list ([obj]): List of day weather forecast data details

    Returns:
        temperatures_list ([obj]): List of forecasted average temperatures for specified number of days
    """
    day_objs = []

    # Loop through the results list creating day objects and map them to the model.
    for day in results_list:
        date = day.get("date")
        temp = day.get("day").get("avgtemp_c")

        day_obj = Weather(date, temp)

        day_objs.append(day_obj)

    return day_objs
