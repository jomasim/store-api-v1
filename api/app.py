from flask import Flask,Blueprint
from flask_restful import Resource, Api
from api.resources import ProductController, SalesController,UserController

api_blueprint=Blueprint("store-api",__name__,url_prefix='/api/v1')
app = Flask(__name__)
api=Api(api_blueprint)

api.add_resource(UserController, '/user/',
                 strict_slashes=False, endpoint='post_user')
api.add_resource(ProductController, '/products/',
                 strict_slashes=False, endpoint='products')
api.add_resource(ProductController, '/products/<int:product_id>/',
                 strict_slashes=False, endpoint='product_by_id')
api.add_resource(SalesController, '/sales/',
                 strict_slashes=False, endpoint='sales')
api.add_resource(SalesController, '/sales/<int:sale_id>/',
                 strict_slashes=False, endpoint='sale_by_id')

app.register_blueprint(api_blueprint)                 
