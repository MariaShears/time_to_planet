import unittest
from . import planet_validator

class TestPlanetValidator(unittest.TestCase):
    def test_valid_planets(self):
        for planet in planet_validator.VALID_PLANETS:
            result = planet_validator.validate(planet)
            self.assertEqual(result, True)

    def test_invalid_planet(self):
        result = planet_validator.validate("lalal")
        self.assertEqual(result, False)
