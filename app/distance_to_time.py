# TODO: pass in real distance
def get_time(distance_in_km):
    return travel_time(distance_in_km)

light_speed = 299792458


# calculate time to travel the given distance with speed of light
def travel_time(distance_in_km):
    # convert distance in km to m
    distance_in_m = distance_in_km * 1000
    return round(distance_in_m/light_speed)
