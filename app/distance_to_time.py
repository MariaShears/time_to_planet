light_speed = 299792458

def get_time(distance_in_km):
    # convert distance in km to m
    distance_in_m = distance_in_km * 1000
    # calculate time to travel the given distance with speed of light
    return round(distance_in_m/light_speed)
