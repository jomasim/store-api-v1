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
    'username':'joma'
}

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
    @staticmethod
    def all():
        users.append(sample_user)
        return users


