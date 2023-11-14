from app.models import Category, Product, User
from app import login


def load_catgories():
    return Category.query.all()


def load_products(kw):
    products = Product.query
    if kw:
        products = products.filter(Product.name.contains(kw))
    return products.all()


def get_user_by_id(user_id):
    return User.query.get(user_id)


def check_user(username=None, password=None):
    if username and password:
        import hashlib
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

        user = User.query.filter(User.username.__eq__(username.strip()),
                                 User.password.__eq__(password)).first()
        return user


