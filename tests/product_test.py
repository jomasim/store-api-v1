import json
from tests.base_test import BaseTestCase


class ProductTestCase(BaseTestCase):
    def test_creating_product(self):
        new_product = {'id':'1','name': 'shirt', 'category': 'apparel', 'description': {
            'color': 'black',
            'size': '35',
            'gender': 'male'
        }, 'price': '1200','quantity':'10'}
        response = self.post('/api/v1/products', data=new_product)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.mimetype,'application/json')

    def test_for_empty_data(self):
        response=self.post('/api/v1/products', data={})
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.mimetype,'application/json')

    def test_get_all_products(self):
        response=self.get('/api/v1/products')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.mimetype,'application/json')

    def test_get_specific_product(self):
        response=self.get('/api/v1/products/1')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.mimetype,'application/json')
    
    def test_get_non_existing_product(self):
        response=self.get('/api/v1/products/199434')
        self.assertEqual(response.status_code,404)
        self.assertEqual(json.loads(response.data),{'error':'product not found'})
        self.assertEqual(response.mimetype,'application/json')

