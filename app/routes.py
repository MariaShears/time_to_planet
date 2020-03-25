from app import app
from markupsafe import escape

from . import distance
from . import planet_validator
from . import responces


@app.route('/v1/planet/<planet>', methods=['GET'])
def index(planet):
    safe_planet = escape(planet)
    if (planet_validator.validate(planet)):
        return responces.success_resp(500, planet)
    else:
        return (responces.error_resp("%s is not a planet" % planet), 404)
