import json
from tests.base_test import BaseTestCase


class ProductTestCase(BaseTestCase):
    def test_creating_product(self):
        new_product = {'name': 'shirt', 'category': 'apparel', 'description': {
            'color': 'black',
            'size': '35',
            'gender': 'male'
        }, 'price': '1200'}
        response = self.post('/api/v1/products', data=new_product)
        self.assertEqual(response.status_code, 201)
