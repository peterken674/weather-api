from django.shortcuts import render
from .request import fetch_data
import statistics
from .models import WeatherResults

from rest_framework.views import APIView
from .serializer import ResultsSerializer
from rest_framework.response import Response

class Results(APIView):
    def get_results(self, city, num_of_days):
        data = fetch_data(city, num_of_days)
        temps = data["temperatures"]

        # List of temperature (only) values
        temps_list = []

        for temp in temps:
            temperature = temp.temperature
            temps_list.append(temperature)

        # Calculations
        maximum = max(temps_list)
        minimum = min(temps_list)
        average = sum(temps_list) / len(temps_list)
        median = statistics.median(temps_list)

        # Create WeatherResults to be serialized.
        result_obj = WeatherResults(maximum, minimum, average, median)

        return result_obj

    def get(self, request, city, format=None):
        days = int(request.query_params['days'])
        results = self.get_results(city, days)
        serializers = ResultsSerializer(results)
        return Response(serializers.data)


