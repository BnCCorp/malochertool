import unittest

from app import app


class AppTests(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False

        self.app = app.test_client()

        self.assertEqual(app.debug, False)

    def tearDown(self):
        pass

    def test_index_html(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Malochertool - Übersicht'.encode('utf-8'), response.data)
        self.assertIn('Hier ist die index.html'.encode('utf-8'), response.data)

if __name__ == '__main__':
    unittest.main()