from datetime import datetime

from sqlalchemy import Column, String, Float, ForeignKey, Integer, DateTime
from app import db
from sqlalchemy.orm import relationship
from flask_login import UserMixin
import hashlib


class Category(db.Model):
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship("Product", backref="category", lazy=True)

    def __str__(self):
        return self.name


class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    full_name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(500), default='https://ceacopiniones.es/wp-content/uploads/2019/03/user-3-1024x1024.png')

    def __str__(self):
        return self.full_name


class Product(db.Model):
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)


if __name__ == '__main__':
    from app import app

    with app.app_context():
        u2 = User(full_name='Tran Thi B',
                  username='TranB',
                  password=str(hashlib.md5("12345".encode('utf-8')).hexdigest()))
        db.session.add(u2)
        db.session.commit()

        # c1=Category(name="Mobile")
        # c2=Category(name="Tablet")
        # db.session.add_all([c1,c2])
        # p1 = Product(name="Iphone 15", price=250000,
        #              image="https://mobilepriceall.com/wp-content/uploads/2022/09/Apple-iPhone-14-1024x1024.jpg",
        #              category_id=1)
        # p2 = Product(name="Tablet 14", price=230000,
        #              image="https://mobilepriceall.com/wp-content/uploads/2022/09/Apple-iPhone-14-1024x1024.jpg",
        #              category_id=2)
        # p3 = Product(name="IPad 13", price=253000,
        #              image="https://mobilepriceall.com/wp-content/uploads/2022/09/Apple-iPhone-14-1024x1024.jpg",
        #              category_id=2)
        # p4 = Product(name="Iphone 12", price=250000,
        #              image="https://mobilepriceall.com/wp-content/uploads/2022/09/Apple-iPhone-14-1024x1024.jpg",
        #              category_id=1)
        # p5 = Product(name="Iphone 11", price=250000,
        #              image="https://mobilepriceall.com/wp-content/uploads/2022/09/Apple-iPhone-14-1024x1024.jpg",
        #              category_id=1)
        # db.session.add_all([p1, p2, p3, p4, p5])
        # db.session.commit()
        # db.create_all()
