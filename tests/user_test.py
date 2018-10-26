import json
from tests.base_test import BaseTestCase


class UserTestCase(BaseTestCase):
    def test_creating_user(self):
        sample_user = {
            'id': '1',
            'name': 'john doe',
            'email': 'doe@gmail.com',
            'phone': '+254728109567',
            'username': 'john',
            'password':'technics100'
        }
        response = self.post('/api/v1/user', sample_user)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data), {
                         'message': 'user created successfully'})
        self.assertEqual(response.mimetype, 'application/json')

    def test_for_empty_data(self):
        response = self.post('/api/v1/user', data={})
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.mimetype, 'application/json')

    def test_for_existing_user(self):
        existing_user = {
            'id': '1',
            'name': 'joma simeon',
            'email': 'simjoms@gmail.com',
            'phone': '+254728109567',
            'username': 'joma',
            'password':'technics100'

        }
        response = self.post('/api/v1/user', existing_user)
        self.assertEqual(response.status_code, 409)
        self.assertEqual(json.loads(response.data), {
                         'message': 'user exists'})
        self.assertEqual(response.mimetype, 'application/json')
