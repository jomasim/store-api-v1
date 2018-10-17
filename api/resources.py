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
    def get(self):
        pass

    def post(self):
        data = request.get_json()
        if not data:
            return make_response(jsonify({'error': 'invalid data'}), 422)
        sale_id = len(sales)+1
        sale = {'id': sale_id, 'user': data['user'], 'date_created': data['date_created'],
                   'line_items': data['line_items'],
                   }
        sales.append(sale)
        return make_response(jsonify({'sales': sales}), 201)
