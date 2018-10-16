from flask import jsonify, make_response, request
from flask_restful import Resource
products = []


class Product(Resource):
    def get(self):
        pass

    def post(self):
        data = request.get_json()
        product_id = len(products)+1
        product = {'id': product_id, 'name': data['name'], 'category': data['category'],
                   'description': data['description'],
                   'price': data['price']
                   }
        products.append(product)
        return make_response(jsonify({'products': products}), 201)


class Sales(Resource):
    def get(self):
        pass

    def post(self):
        pass
