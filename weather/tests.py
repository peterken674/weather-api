from weather.models import Weather
from unittest import TestCase
from .request import fetch_data

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

        temp_objs = self.response_obj['temperatures']
        self.assertEqual(len(temp_objs), 3)

        day1 = temp_objs[0] #today
        day2 = temp_objs[1] #tomorrow
        day3 = temp_objs[2] #day after tomorrow, and so on, depending on num_of_days

        # Since the temperature forecasts and date will vary (depending on the day you run this test), this section should be adjusted respectively to fit the expected Weather API response for that specific day and the subsequent days.
        # Test these values against the response from https://api.weatherapi.com/v1/forecast.json?key={{api_key}}&q=Nairobi&days=3 at the time of testing.
        self.assertEqual(day1.date, '2021-09-27') 
        self.assertEqual(day2.date, '2021-09-28')
        self.assertEqual(day3.date, '2021-09-29')

        self.assertEqual(day1.temperature, 20.8)
        self.assertEqual(day2.temperature, 21.8)
        self.assertEqual(day3.temperature, 22.3)
