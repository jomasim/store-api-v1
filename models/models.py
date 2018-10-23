from werkzeug.security import generate_password_hash, check_password_hash
products = []
sales = []
users=[]
''' sample product dict '''

sample_product = {'id': '1', 'name': 'shirt', 'category': 'apparel', 'description': {
    'color': 'black',
    'size': '35',
            'gender': 'male'
}, 'price': '1200', 'quantity': '10'}

''' sample sale record '''


sample_sale = {
    'id': '1',
    'date_created': '12/7/2008',
    'user': 'attendant1',
            'line_items': {
                'products': {
                    'product_id': '1',
                    'item_count': '2',
                    'selling_price': '1200'
                }
            }
}

sample_user={
    'id':'1',
    'name':'joma simeon',
    'email':'simjoms@gmail.com',
    'phone':'+254728109567',
    'username':'joma',
    'password':generate_password_hash('123456')
}
users.append(sample_user)
class Product():
    @staticmethod
    def all():
        products.append(sample_product)
        return products

class Sales():
    @staticmethod
    def all():
        sales.append(sample_sale)
        return sales

class User():

    def __init__(self,id,username,password,is_admin=False):
      self.id=id
      self.username=username
      self.password=password

    @staticmethod
    def all():
        users.append(sample_user)
        return users
    @staticmethod
    def get_by_username(username):
        for user in users:
            if user['username'] == str(username):
                return user
        return False

