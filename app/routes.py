from app import app
from . import distance

@app.route('/v1/planet/mars')
def index():
    return distance.get_distance()
