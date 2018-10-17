import json
from tests.base_test import BaseTestCase


class SaleTestCase(BaseTestCase):
    def test_creating_sale(self):

        ''' sample sale record '''

        new_sale = {
            'id': '1', 
            'date_created': '12/7/2008', 
            'user': 'attendant1',
            'line_items':{
                'products':{
                    'product_id':'1',
                    'item_count':'2',
                    'selling_price':'1200'
                }
            }
        }

        response=self.post('api/v1/sales/',new_sale)
        self.assertEqual(response.mimetype,'application/json')   
        self.assertEqual(response.status_code,201)
        self.assertEqual(json.loads(response.data),{'message':'sale record created successfully'})

    def test_for_empty_data(self):
        response=self.post('/api/v1/sales', data={})
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.mimetype,'application/json')    

    def test_get_sales(self):
        response=self.get('/api/v1/sales')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.mimetype,'application/json')
    
    def test_get_specific(self):
        response=self.get('/api/v1/sales/1')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.mimetype,'application/json')

    def test_get_non_existing_sale(self):
        response=self.get('/api/v1/sales/199434')
        self.assertEqual(response.status_code,404)
        self.assertEqual(json.loads(response.data),{'error':'sale record not found'})
        self.assertEqual(response.mimetype,'application/json')