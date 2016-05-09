import unittest
from app import app

class FavmappTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    # Integration
    def test_health_check(self):
        response = self.app.get('/api')
        self.assertEquals(response.data,
                          '"Hello this is the Favmapp API"',
                          "GET healthcheck didn't respond ok")
        response = self.app.post('/api')
        self.assertEquals(response.data,
                          '"Hello, you successfully sent a POST to Favmapp API"',
                          "POST healthcheck didn't respond ok")

    # Unit
    def test_tag_has_name(self):
        from app.models import Tag
        from app.error_handler import InvalidUsage
        name = None
        with self.assertRaises(InvalidUsage) as context:
            Tag.create(name)
        self.assertEquals(400, context.exception.status_code)
        name = ''
        with self.assertRaises(InvalidUsage) as context:
            Tag.create(name)
        self.assertEquals(400, context.exception.status_code)


if __name__ == '__main__':
    unittest.main()