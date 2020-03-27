import unittest
from . import distance_to_time


class TestDistanceToTime(unittest.TestCase):
    def test_convert_distance_to_time(self):
        result = distance_to_time.convert_distance_to_time(118957737.83775564)
        self.assertEqual(result, 397)
