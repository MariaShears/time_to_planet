VALID_PLANETS = [
    "sun",
    "mercury",
    "venus",
    "moon",
    "mars",
    "jupiter",
    "saturn",
    "uranus",
    "neptune",
    "pluto"
]


def is_valid(planet):
    """Returns if the planet exist in the plants AstronomyAPI supports"""
    return planet in VALID_PLANETS
