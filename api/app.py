from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, Api
from api.resources import Product, Sales
app = Flask(__name__)
api = Api(app)

api.add_resource(Product, '/api/v1/products/',
                 strict_slashes=False, endpoint='products')
api.add_resource(Product, '/api/v1/products/<int:product_id>/',
                 strict_slashes=False, endpoint='product_by_id')
api.add_resource(Sales, '/api/v1/sales/',
                 strict_slashes=False, endpoint='sales')
api.add_resource(Sales, '/api/v1/sales/<int:sale_id>/',
                 strict_slashes=False, endpoint='sale_by_id')
