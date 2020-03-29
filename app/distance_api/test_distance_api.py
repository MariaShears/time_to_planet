from unittest import TestCase, mock
import json
import os
import datetime

from app import distance_api


def get_test_data():
    """returns the json responce of AstronomyAPI loaded from a static file"""
    raw_json = ""
    with open('./app/distance_api/mock_data.json') as f:
        raw_json = json.load(f)
    return raw_json


class FakeRequest:
    def __init__(self, raw_json):
        self.raw_json = raw_json

    def json(self):
        return self.raw_json


class TestDistanceAPI(TestCase):
    def test_parse(self):
        expected_result = {
            "sun": 149151360.83925638,
            "mercury": 135331999.11231053,
            "venus": 107089159.00548483,
            "moon": 407445.55591713585,
            "mars": 228111103.1515586,
            "jupiter": 814494981.5786254,
            "saturn": 1559951962.544126,
            "uranus": 3090229927.5256147,
            "neptune": 4621695743.049282,
            "pluto": 5138408053.535285
        }
        raw_json = get_test_data()
        result = distance_api.parse(raw_json)
        self.assertEqual(result, expected_result)

    @mock.patch.dict(os.environ,
                     {'ASTRONOMYAPI_JWT': 'test_jwt',
                      'ASTRONOMYAPI_URL': 'http://localhost'})
    def test_distance_api_params(self):
        dt = datetime.date(2003, 12, 29)
        params = distance_api.DistanceAPIParams(dt)
        hashed_params = params.get_hash()
        self.assertEqual(hashed_params, "9ef833ddf39ff36fcd04e05bbde68782")

    @mock.patch.dict(os.environ,
                     {'ASTRONOMYAPI_JWT': 'test_jwt',
                      'ASTRONOMYAPI_URL': 'http://localhost'})
    def test_get_distance(self):
        with mock.patch('app.distance_api.sqlite3') as sqlite3_mock:
            sqlite3_mock.connect().cursor().fetchone.return_value = None
            with mock.patch('app.distance_api.requests') as requests_mock:
                test_data = get_test_data()
                requests_mock.get.return_value = FakeRequest(test_data)
                d = distance_api.get_distance('moon')
                self.assertEqual(d, 407445.55591713585)
