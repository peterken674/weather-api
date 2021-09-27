from weather.models import Weather, WeatherResults
from unittest import TestCase
from .request import fetch_data
import requests
import statistics


class WeatherTest(TestCase):
    """Test class that defines test cases for the Weather class behaviours.
        Args:
            unittest (TestCase): TestCase class that helps in creating test cases.
    """

    def setUp(self) -> None:
        """setUp method to run before each test cases.
        """
        self.test_day = Weather("2021-09-25", 21.8)

        # Make a test query to the server
        self.response_obj = fetch_data('Nairobi', 3)

        self.temp_objs = self.response_obj['temperatures']

        self.day1 = self.temp_objs[0]  # today
        self.day2 = self.temp_objs[1]  # tomorrow
        # day after tomorrow, and so on, depending on num_of_days
        self.day3 = self.temp_objs[2]

    def test_init(self):
        """test_init test case to test if the object is initialized properly
        """
        self.assertTrue(isinstance(self.test_day, Weather))
        self.assertEqual(self.test_day.date, "2021-09-25")
        self.assertEqual(self.test_day.temperature, 21.8)

    def test_request(self):
        """Test the request sent to the server
        """
        city = self.response_obj['city']
        self.assertEqual(city, 'Nairobi')

        self.assertEqual(len(self.temp_objs), 3)

        # Since the temperature forecasts and date will vary (depending on the day you run this test), this section should be adjusted respectively to fit the expected Weather API response for that specific day and the subsequent days.
        # Test these values against the response from https://api.weatherapi.com/v1/forecast.json?key={{api_key}}&q=Nairobi&days=3 at the time of testing.
        self.assertEqual(self.day1.date, '2021-09-27')
        self.assertEqual(self.day2.date, '2021-09-28')
        self.assertEqual(self.day3.date, '2021-09-29')

        self.assertEqual(self.day1.temperature, 20.8)
        self.assertEqual(self.day2.temperature, 21.8)
        self.assertEqual(self.day3.temperature, 22.3)


class WeatherResultsTest(TestCase):
    """Test the WeatherResults class and our API response

        Args:
            unittest (TestCase): TestCase class that helps in creating test cases.
    """

    def setUp(self) -> None:
        """setUp method to run before each test cases.
        """
        self.test_obj = WeatherResults(
            23.4, 20.8, 22.4, 22.1)  # arbitrary test values

        # Make a test query to the server
        self.response_obj = fetch_data('Nairobi', 3)
        # ensure your server is running (port 8000) for this to work
        self.my_api_response = requests.get(
            'http://127.0.0.1:8000/api/locations/Nairobi/?days=3')

        self.temp_objs = self.response_obj['temperatures']

        self.day1 = self.temp_objs[0]  # today
        self.day2 = self.temp_objs[1]  # tomorrow
        # day after tomorrow, and so on, depending on num_of_days
        self.day3 = self.temp_objs[2]

        self.my_api_response_json = self.my_api_response.json()

    def test_init(self):
        """Test initialization of objects of WeatherResults class
        """
        self.assertTrue(isinstance(self.test_obj, WeatherResults))
        self.assertEqual(self.test_obj.maximum, 23.4)
        self.assertEqual(self.test_obj.minimum, 20.8)
        self.assertEqual(self.test_obj.average, 22.4)
        self.assertEqual(self.test_obj.median, 22.1)

    def test_my_api(self):
        """Test the endpoint 
        """

        temperatures_list = [self.day1.temperature,
                             self.day2.temperature, 
                             self.day3.temperature]

        maximum = max(temperatures_list)
        minimum = min(temperatures_list)
        average = float("{:.1f}".format(
            sum(temperatures_list) / len(temperatures_list)))
        median = float("{:.1f}".format(statistics.median(temperatures_list)))

        self.assertEqual(self.my_api_response_json['maximum'], maximum)
        self.assertEqual(self.my_api_response_json['minimum'], minimum)
        self.assertEqual(self.my_api_response_json['average'], average)
        self.assertEqual(self.my_api_response_json['median'], median)
