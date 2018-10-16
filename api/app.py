from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, Api
from api.resources import Product, Sales
app = Flask(__name__)
api = Api(app)

if __name__ == '__main__':
    app.run(debug=True)

api.add_resource(Product, '/api/v1/products/')
api.add_resource(Product, '/api/v1/products/<int:product_id>/')
api.add_resource(Sales, '/api/v1/sales/')
api.add_resource(Sales, '/api/v1/sales/<int:sales_id>/')
