from app import app
from markupsafe import escape

from . import planet_validator
from . import responces
from . import distance_to_time


@app.route('/v1/planet/<planet>', methods=['GET'])
def index(planet):
    safe_planet = escape(planet)
    safe_planet = safe_planet.lower()
    if not planet_validator.is_valid(safe_planet):
        return responces.error_resp("%s is not a planet" % safe_planet), 404
    return responces.success_resp(distance_to_time.get_time(safe_planet), safe_planet)
