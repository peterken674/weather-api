from django.shortcuts import render
from .request import fetch_data
import statistics

def index(request):
    """Index view

    """
    results = fetch_data("Nairobi", 3)
    city = results["city"]
    temps = results["temperatures"]

    # List of temperature values
    temps_list = []

    for temp in temps:
        temperature = temp.temperature
        temps_list.append(temperature)

    maximum = max(temps_list)
    minimum = min(temps_list)
    average = sum(temps_list) / len(temps_list)
    median = statistics.median(temps_list)

    context = {
        "city": city,
        "temps": temps_list,
        "maximum": maximum,
        "minimum": minimum,
        "average": average,
        "median": median,
    }
    return render(request, 'index.html', context)
