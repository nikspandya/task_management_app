import unittest

from api import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        # set up test client for main app
        self.app = app.test_client()

    def test_app_main_page(self):
        # sends HTTP GET request to the application
        response_code = self.app.get("/")
        # assert the status code of the response
        self.assertEqual(response_code.status_code, 200)


if __name__ == "__main__":
    unittest.main()
