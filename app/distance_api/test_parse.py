import unittest
import json

from . import parse

class TestDistanceAPIParse(unittest.TestCase):
    def test_parse(self):
        raw_json = "";
        with open('./app/distance_api/mock_data.json') as f:
            raw_json = json.load(f)
        expected_result = {
            "sun": 149151360.83925638,
            "mercury": 135331999.11231053,
            "venus": 107089159.00548483,
            "moon": 407445.55591713585,
            "mars": 228111103.1515586,
            "jupiter": 814494981.5786254,
            "saturn": 1499756688.9622102,
            "uranus": 3090229927.5256147,
            "neptune": 4621695743.049282,
            "pluto": 5138408053.535285
        }
        result = parse.parse(raw_json)
        self.assertEqual(result, expected_result)
