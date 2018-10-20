from flask import jsonify, make_response, request
from flask_restful import Resource
from models.models import Product, Sales, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

products = Product.all()
sales = Sales.all()
users = User.all()


class ProductController(Resource):
    def get(self, product_id=None):
        if not product_id:
            return make_response(jsonify({'products': products}), 200)
        else:

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


class SalesController(Resource):
    def get(self, sale_id=None):

        if not sale_id:
            return make_response(jsonify({'sales': sales}), 200)
        else:
            ''' search sale by sale id '''
            sale = [sale for sale in sales if sale['id'] == str(sale_id)]
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
        return make_response(jsonify({'message': 'sale record created successfully'}), 201)


class UserController(Resource):
    def post(self):
        user_id = len(users)+1
        data = request.get_json()
        if not data:
            return make_response(jsonify({'error': 'invalid data'}), 422)
        user = {'id': user_id, 'name': data['name'], 'email': data['email'],
                'username': data['username'], 'phone': data['phone']
                }

        ''' check if user already exists '''
        existing = [user for user in users if user['email'] == data['email']]
        if not existing:
            users.append(user)
            return make_response(jsonify({'message': 'user created successfully'}), 201)
        else:
            return make_response(jsonify({'message': 'user exists'}), 409)

    def get(self):
        pass


class AuthController(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']

        user = User.get_by_username(username)

        if user:
            if check_password_hash(user.password, password):
                token = create_access_token(identity=user)
                return make_response(jsonify({"message": "login successful",
                                              "access_token": token}), 200)
        return make_response(jsonify({"message": "invalid login"}), 401)
