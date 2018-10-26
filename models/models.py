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
    def __init__(self):
        self.entry={}
        products.append(sample_product)
    
    def create(self,data):
        self.entry['id']=len(products)+1
        self.entry['name']=data['name']
        self.entry['category']=data['category']
        self.entry['description']=data['description']
        self.entry['price']=data['price']
        self.entry['quantity']=data['quantity']
        products.append(self.entry)

    @staticmethod
    def all():
        products.append(sample_product)
        return products
    
    @staticmethod
    def get_by_id(product_id):
        for product in products:
            if product['id'] == str(product_id):
                return product
        return False
    
    @staticmethod
    def exists(product_id):
        existing=None
        if product_id !=None:
             existing = [product for product in products if product['id'] == str(product_id)]
        return existing


class Sales():
    @staticmethod
    def all():
        sales.append(sample_sale)
        return sales

class User(object):
    def __init__(self):
        users.append(sample_user)
        self.entry={}

    def create(self,data):
        self.entry['id']=len(users)+1
        self.entry['name']=data['name']
        self.entry['username']=data['username']
        self.entry['email']=data['email']
        self.entry['password']=generate_password_hash(data['password'])
        self.entry['phone']=data['phone']
        users.append(self.entry)

    @staticmethod
    def exists(email):
        existing=None
        if email !=None:
             existing = [user for user in users if user['email'] == email]
        return existing

    ''' return all users in data structure '''
    @staticmethod
    def all():
        return users

    ''' get user by username '''
    @staticmethod
    def get_by_username(username):
        for user in users:
            if user['username'] == str(username):
                return user
        return False

