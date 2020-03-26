import os
import datetime
import requests
import json

# Munich
lon = 11.576124
lat = 48.137154


# retrives distance to planet via AstronomyAPI
def get_distance(planet):
    jwt_token = os.environ['ASTRONOMYAPI_JWT']
    api_url = os.environ['ASTRONOMYAPI_URL']
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
    url = "%s/positions" % api_url
    r = requests.get(url, params=payload, headers=headers)
    raw_json = r.json()
    parsed_result = parse(raw_json)
    return parsed_result[planet]


def row_to_distance(row):
    first_cell = row['cells'][0]
    planet_id = first_cell['id']
    distance = first_cell['distance']['from_earth']['km']
    return distance, planet_id


def parse(raw_json):
    rows = raw_json['data']['table']['rows']
    distance_pairs = list(map(row_to_distance, rows))
    distance_dic = {}
    for pair in distance_pairs:
        distance_dic.update({pair[1]: pair[0]})
    return distance_dic
