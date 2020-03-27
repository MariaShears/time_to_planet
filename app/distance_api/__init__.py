import os
import datetime
import hashlib
import json
import requests
import sqlite3
import pickle

# Munich
lon = 11.576124
lat = 48.137154


class DistanceAPIParams:
    def __init__(self):
        jwt_token = os.environ['ASTRONOMYAPI_JWT']
        api_url = os.environ['ASTRONOMYAPI_URL']
        now = datetime.datetime.now()
        yesterday = now - datetime.timedelta(days=1)
        self.url = "%s/positions" % api_url
        self.headers = {'authorization': "Bearer %s" % jwt_token}
        self.query_params = {
            'lon': lon,
            'lat': lat,
            'to_year': now.year,
            'to_month': now.month,
            'to_day': now.day,
            'from_year': yesterday.year,
            'from_month': yesterday.month,
            'from_day': yesterday.day
        }

    def get_hash(self):
        dic = {
            'url': self.url,
            'headers': self.headers,
            'query_params': self.query_params
        }
        raw_json = json.dumps(dic, sort_keys=True, indent=4)
        result = hashlib.md5(raw_json.encode())
        hex_val = result.hexdigest()
        return hex_val


# retrives distance to planet via AstronomyAPI
def get_distance(planet):
    # get current api params that include things like todays date
    params = DistanceAPIParams()
    # get the hash of these values which is used as a cache key
    current_hash = params.get_hash()

    # check db for current cache key
    conn = sqlite3.connect('api_cache.db')
    c = conn.cursor()
    # Create table if it does not exist
    c.execute('''CREATE TABLE IF NOT EXISTS cache
             (cache_key text, data blob)''')
    # check db for cached value
    c.execute('SELECT * FROM cache WHERE cache_key=?', (current_hash,))
    db_cache = c.fetchone()

    distance = 0
    if db_cache is None:
        # get distances from the remote api
        r = requests.get(params.url, params=params.query_params, headers=params.headers)
        raw_json = r.json()
        parsed_result = parse(raw_json)
        # cache parsed_result
        pickled_results = pickle.dumps(parsed_result)
        c.execute('INSERT INTO cache (cache_key, data) VALUES (?,?)', (current_hash, pickled_results))
        distance = parsed_result[planet]
    else:
        un_pickled_results = pickle.loads(db_cache[1])
        distance = un_pickled_results[planet]

    conn.commit()
    conn.close()
    return distance



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

