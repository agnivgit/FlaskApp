import unittest
from app import app
import logging

logging.basicConfig(level=logging.INFO)

class AppTestCase(unittest.TestCase):

    # Setting up Context of the App and tearing down
    def setUp(self):
        self.context = app.app_context()
        self.context.push()
        self.client = app.test_client()

    def tearDown(self):
        self.context.pop()

    # TestCases for Unit test
    def test_1_get_request(self):
        app.logger.info("Executing 1st test case..")
        response = self.client.get()
        assert response.status_code == 200
        assert "<p>Hello, World</p>\n" == response.get_data(as_text=True)        

    def test_2_get_request_with_header(self):
        app.logger.info("Executing 2nd test case..")
        response = self.client.get('/',headers={"content-type":"application/json"})
        assert response.status_code == 200
        assert '{"message": "Hello, World"}\n' == response.get_data(as_text=True) 

    def test_3_post_request(self):
        app.logger.info("Executing 3rd test case..")
        response = self.client.post()
        assert response.status_code == 200
        assert "" == response.get_data(as_text=True)

if __name__ == "__main__":
    unittest.main()        


