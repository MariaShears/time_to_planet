import unittest
from . import planet_validator


class TestPlanetValidator(unittest.TestCase):
    def test_valid_planets(self):
        for planet in planet_validator.VALID_PLANETS:
            result = planet_validator.is_valid(planet)
            self.assertEqual(result, True)

    def test_invalid_planet(self):
        result = planet_validator.is_valid("lalal")
        self.assertEqual(result, False)
