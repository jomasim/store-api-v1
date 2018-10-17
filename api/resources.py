from flask import jsonify, make_response, request
from flask_restful import Resource
products = []
sales = []

''' sample product dict '''

sample = {'id': '1', 'name': 'shirt', 'category': 'apparel', 'description': {
    'color': 'black',
    'size': '35',
            'gender': 'male'
}, 'price': '1200', 'quantity': '10'}

''' sample sale record '''


sample_sale = {
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

class Product(Resource):
    def get(self, product_id=None):
        if not product_id:
            return make_response(jsonify({'products': products}), 200)
        else:
            products.append(sample)

            ''' search for product  using product_id '''

            product = [
                product for product in products if product['id'] == str(product_id)]
            if not product:
                return make_response(jsonify({'error': 'product not found'}), 404)
            else:
                return make_response(jsonify({'product': product}), 200)

    def post(self):
        data = request.get_json()
        if not data:
            return make_response(jsonify({'error': 'invalid data'}), 422)
        product_id = len(products)+1
        product = {'id': product_id, 'name': data['name'], 'category': data['category'],
                   'description': data['description'],
                   'price': data['price'], 'quantity': data['quantity']
                   }
        products.append(product)
        return make_response(jsonify({'products': products}), 201)


class Sales(Resource):
    def get(self,sale_id=None):

        if not sale_id:
            return make_response(jsonify({'sales': sales}), 200)
        else:
            sales.append(sample_sale)
        
            ''' search sale by sale id '''
            sale=[sale for sale in sales if sale['id']==str(sale_id)]
            if not sale:
                 return make_response(jsonify({'error': 'sale record not found'}), 404)
            else:
                return make_response(jsonify({'sale': sale}), 200)


      
        


    def post(self):
        data = request.get_json()
        if not data:
            return make_response(jsonify({'error': 'invalid data'}), 422)
        sale_id = len(sales)+1
        sale = {'id': sale_id, 'user': data['user'], 'date_created': data['date_created'],
                   'line_items': data['line_items'],
                   }
        sales.append(sale)
        return make_response(jsonify({'message':'sale record created successfully'}), 201)
