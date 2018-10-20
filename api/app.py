from flask import Flask, Blueprint
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager
from api.resources import ProductController, SalesController, UserController
from instance.api_config import api_config

api_blueprint = Blueprint("store-api", __name__, url_prefix='/api/v1')
jwt=JWTManager()

''' setting api config '''


def create_app(config_setting):

    app = Flask(__name__)
    app.config.from_object(api_config[config_setting])
    app.config['JWT_SECRET_KEY']="SECRET KEY"


    jwt.init_app(app)

    ''' setting api blueprint  '''
    api = Api(api_blueprint)

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

    return app
