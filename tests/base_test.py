import json
import unittest
from run import app


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)
        url = "/api/v1/auth"
        data = {"username": "joma", "password": "123456"}
        response = self.client.post(url,
                                    data=json.dumps(data),
                                    content_type='application/json')
        data=json.loads(response.data)
        self.token="Bearer " + data ['access_token']

    def get(self, url):
        return self.client.get(url,
                               headers={"Authorization": self.token}
                               )

    def post(self, url, data):
        return self.client.post(url,
                                data=json.dumps(data),
                                content_type='application/json',
                                headers={"Authorization": self.token}
                                )

    def tearDown(self):
        pass

        
