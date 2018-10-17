import json
from tests.base_test import BaseTestCase


class UserTestCase(BaseTestCase):
    def test_creating_user(self):
        sample_user = {
            'id': '1',
            'name': 'joma simeon',
            'email': 'simjoms@gmail.com',
            'phone': '+254728109567'
        }
        response=self.post('/api/v1/user',sample_user)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.mimetype,'application/json')
