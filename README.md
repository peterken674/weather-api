# WeatherAPI
## Description
Weather API that returns maximum, minimum, average and median temperatures for a given number of days in a given city. The API fetches data from this [Weather API](https://www.weatherapi.com/).

The endpoint is:

```
/api/locations/{city}/?days={number_of_days}
``` 
Where:

_city (str)_ : The city whose data you want to fetch.

_number_of_days (int)_ : A positive integer indicating number of days to fetch the data.

This API response is in the following JSON format:

```json
{
    "maximum": value,
    "minimum": value,
    "average": value,
    "median": value
}
```

or

```json
{
    "status_code": value,
    "message": value
}
```
in case an error is encountered.

#

## Setup/Installation
On your terminal, clone the project. The following are instructions for Linux users but other users can follow the same steps.
    
    $ git clone git@github.com:peterken674/weather-api.git

Navigate into the cloned project.

    $ cd weather-api

Create a `.env` file.

    $ touch .env

Inside `.env`, add the following and fill the empty fields with the appropriate values:

```python
SECRET_KEY=
DEBUG=True
MODE='dev'
ALLOWED_HOSTS=['.localhost','127.0.0.1']
DISABLE_COLLECTSTATIC=1
API_KEY=
```
The API_KEY is from your account on [Weather API](https://www.weatherapi.com/), sign up if you don't have one.

Create the virtual environment and install the requirements from `requirements.txt`

    $ python3 -m venv env
    $ . env/bin/activate
    $ pip install -r requirements.txt


Perform an initial migration.

    $ python3 manage.py migrate


Start the server to run locally.

    $ python3 manage.py runserver

## Known Bugs
The [Weather API](https://www.weatherapi.com/) being used only returns a maximum forecast of 3 days, despite the documentation indicating that it shoulg return at least 10.
## Technologies Used
- Django REST Framework
- Python 3.9.7
- Weather API
## Support and contact details
If you have any suggestions, questions or in case of a fire, you can reach the developer via [email](mailto:peterken.ngugi@gmail.com).
### License
 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Copyright &copy; 2021 **[peterken674](www.github.com/peterken674)**