import json
from tests.base_test import BaseTestCase
from models.models import User
from werkzeug.security import generate_password_hash, check_password_hash

class TestAuth(BaseTestCase):
    def test_for_get_user_identity(self):
        user = User.get_by_username("joma")
        self.assertTrue(user)
        self.assertEqual(user['name'], "joma simeon")

    def test_match_password(self):
        username = "joma"
        user = User.get_by_username(username)
        password = "123456"
        self.assertTrue(user)
        self.assertTrue(check_password_hash(user['password'], password))

    def test_login(self):
        user={"username": "joma",
            "password": "123456"
                }
        response = self.post('/api/v1/auth', data=user)
        self.assertTrue(response)
        self.assertEqual(response.status_code,200)