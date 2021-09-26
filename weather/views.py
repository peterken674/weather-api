from django.shortcuts import render
from .request import fetch_data
import statistics
from .models import WeatherResults
from urllib.error import HTTPError

from rest_framework.views import APIView
from .serializer import ResultsSerializer
from rest_framework.response import Response
from django.http import JsonResponse

class Results(APIView):
    def get_results(self, city: str, num_of_days):
        """Call the function that processes the data from the API and computes the required values, packaging them into an object.

        Args:
            city (str): City to search for.
            num_of_days (int): Number of days to search for.

        Returns:
            obj: Object containing max, min, average, and median values.
        """
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
        average = "{:.1f}".format( sum(temps_list) / len(temps_list))
        median = "{:.1f}".format( statistics.median(temps_list))

        # Create WeatherResults to be serialized.
        result_obj = WeatherResults(maximum, minimum, average, median)

        return result_obj

    def get(self, request, city, format=None):
        try:
            days = int(request.GET.get('days', 3))
            results = self.get_results(city, days)
            serializers = ResultsSerializer(results)
            return Response(serializers.data)
        except HTTPError as err:
            data={'status_code': err.code, 'message': err.reason}
            return Response(data)


