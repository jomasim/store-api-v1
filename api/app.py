from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

if __name__ == '__main__':
    app.run(debug=True)

api.add_resource('/api/v1/products')
api.add_resource('/api/v1/products/<product_id>')
api.add_resource('/api/v1/sales')
api.add_resource('/api/v1/sales/<sales_id>')