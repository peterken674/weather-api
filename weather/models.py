from django.db import models


class Weather:
    """
    Class to be used to form the weather details object fetched from the API.
    """

    def __init__(self, date, temperature):
        self.date = date
        self.temperature = temperature


class WeatherResults:
    def __init__(self, max, min, avg, median):
        self.maximum = max
        self.minimum = min
        self.average = avg
        self.median = median
