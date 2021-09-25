from weather.models import Weather
from django.test import TestCase
from unittest import TestCase

class WeatherTest(TestCase):
    """Test class that defines test cases for the Weather class behaviours.
    Args:
        unittest (TestCase): TestCase class that helps in creating test cases.
    """
    def setUp(self) -> None:
        """setUp method to run before each test cases.
        """
        self.test_day = Weather("2021-09-25", 21.8)

    def test_init(self):
        """test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.test_day.date, "2021-09-25")
        self.assertEqual(self.test_day.temperature, 21.8)