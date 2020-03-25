from app import app
from markupsafe import escape

from . import planet_validator
from . import responces
from . import distance_to_time

mock_distance_in_km = 118957737.83775564


@app.route('/v1/planet/<planet>', methods=['GET'])
def index(planet):
    safe_planet = escape(planet)
    safe_planet = safe_planet.lower()
    if planet_validator.is_valid(safe_planet):
        return responces.success_resp(distance_to_time.get_time(mock_distance_in_km), safe_planet)
    else:
        return responces.error_resp("%s is not a planet" % safe_planet), 404
