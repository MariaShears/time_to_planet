import unittest
from . import distance_to_time

class TestDistanceToTime(unittest.TestCase):
    def test_get_time(self):
        result = distance_to_time.get_time(118957737.83775564)
        self.assertEqual(result, 397)
