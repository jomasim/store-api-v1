import json
import unittest
from run import app


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)

    def get(self, url):
        return self.client.get(url,
        headers={"Authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDAwMzg2MDIsIm5iZiI6MTU0MDAzODYwMiwianRpIjoiNTdjNzQzZDQtMGNlMi00ZjlmLWE0NDItODc2OGQwNGM5NTA2IiwiZXhwIjoxNTQwMDM5NTAyLCJpZGVudGl0eSI6ImpvbWEiLCJmcmVzaCI6MTU0MDAzOTgwMiwidHlwZSI6ImFjY2VzcyJ9.cO-NroSHJQ1ITrV2yBJb6ulJDMIPZXObufly-L-GtpY"}
        )

    def post(self, url, data):
        return self.client.post(url,
                                data=json.dumps(data),
                                content_type='application/json',
                                headers={"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDAwMzg2MDIsIm5iZiI6MTU0MDAzODYwMiwianRpIjoiNTdjNzQzZDQtMGNlMi00ZjlmLWE0NDItODc2OGQwNGM5NTA2IiwiZXhwIjoxNTQwMDM5NTAyLCJpZGVudGl0eSI6ImpvbWEiLCJmcmVzaCI6MTU0MDAzOTgwMiwidHlwZSI6ImFjY2VzcyJ9.cO-NroSHJQ1ITrV2yBJb6ulJDMIPZXObufly-L-GtpY"}
                                )

    def tearDown(self):
        pass
