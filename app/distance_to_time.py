from . import distance_api

light_speed = 299792458


def get_time(planet):
    distance_in_km = distance_api.get_distance(planet)
    return convert_distance_to_time(distance_in_km)


def convert_distance_to_time(distance_in_km):
    # convert distance in km to m
    distance_in_m = distance_in_km * 1000
    # calculate time to travel the given distance with speed of light
    return round(distance_in_m / light_speed)
