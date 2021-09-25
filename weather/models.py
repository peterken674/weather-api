from django.db import models

class Weather:
    """
    Class to be used to form the weather details object fetched from the API.
    """
    def __init__(self, temperature):
        self.temperature = temperature
