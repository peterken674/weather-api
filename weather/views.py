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
    list_temps = []

    for temp in temps:
        temperature = temp.temperature
        list_temps.append(temperature)

    maximum = max(list_temps)
    minimum = min(list_temps)
    average = sum(list_temps) / len(list_temps)
    median = statistics.median(list_temps)

    context = {
        "city": city,
        "temps": list_temps,
        "maximum": maximum,
        "minimum": minimum,
        "average": average,
        "median": median,
    }
    return render(request, 'index.html', context)
