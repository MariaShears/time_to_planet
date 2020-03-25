import unittest
from . import responces

class TestResponces(unittest.TestCase):
    def test_success_resp(self):
        seconds = 666
        planet = "mars"
        result = responces.success_resp(seconds, planet)
        self.assertEqual(result, {
            "from": "earth",
            "to": planet,
            "seconds": seconds
        })

    def test_error_resp(self):
        reason = "life is hard"
        result = responces.error_resp(resaon)
        self.assertEqual(result, { "error": reason })
