import os
import datetime
import requests

# AstronomyAPI creds
jwt_token = os.environ.get('ASTRONOMYAPI_JWT', '')

# Munich
lon= 11.576124
lat = 48.137154

# retrives distance to planet via AstronomyAPI
def get_distance(planet):
    now = datetime.datetime.now()
    yesterday = now - datetime.timedelta(days=1)
    payload = {
        'lon': lon,
        'lat': lat,
        'to_year': now.year,
        'to_month': now.month,
        'to_day': now.day,
        'from_year': yesterday.year,
        'from_month': yesterday.month,
        'from_day': yesterday.day
    }
    headers = {'authorization': "Bearer %s" % jwt_token}
    r = requests.get('http://localhost:3000/positions', params=payload, headers=headers)
    raw_json = r.json()
    parsed_result = parse(raw_json)
    return parsed_result[planet]


def parse(raw_json):
    # TODO: parse raw_json and return real values
    return {
        "sun": 118957737.83775564,
        "mercury": 118957737.83775564,
        "venus": 118957737.83775564,
        "moon": 118957737.83775564,
        "mars": 118957737.83775564,
        "jupiter": 118957737.83775564,
        "saturn": 118957737.83775564,
        "uranus": 118957737.83775564,
        "neptune": 118957737.83775564,
        "pluto": 118957737.83775564
    }
