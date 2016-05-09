import os
import unittest
import tempfile
from app import app

class FavmappTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_health_check(self):
        response = self.app.get('/')
        self.assertEquals(response.data,
                          '"Hello this is the Favmapp API"',
                          "GET healthcheck didn't respond ok")
        response = self.app.post('/')
        self.assertEquals(response.data,
                          '"Hello, you successfully sent a POST to Favmapp API"',
                          "POST healthcheck didn't respond ok")

if __name__ == '__main__':
    unittest.main()