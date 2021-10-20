from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean, Enum
from sqlalchemy.orm import relationship
from data import db
from datetime import datetime
from flask_login import UserMixin
import enum
class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    created_date = Column(DateTime, default=datetime.now())
    category_id = Column(Integer, ForeignKey(Category.id))
    creator_id = Column(Integer, ForeignKey('user.id'))
    receipt_details = relationship('ReceiptDetail', backref='product', lazy=True)
class UserRole(enum.Enum):
    ADMIN = 1
    MANAGER = 2
    STAFF = 3
    USER = 4



class User(db.Model,UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    use_role = Column(Enum(UserRole), default=UserRole.USER)
    products = relationship(Product, backref='user', lazy=True)
class Receipt(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, default=datetime.now())
    updated_date = Column(DateTime, default=datetime.now())
    details = relationship('ReceiptDetail', backref='receipt', lazy=True)

class ReceiptDetail(db.Model):
    product_id = Column(Integer, ForeignKey(Product.id), primary_key=True)
    receipt_id = Column(Integer, ForeignKey(Receipt.id), primary_key=True)
    quantity = Column(Integer, default=0)
    unit_price = Column(Float, default=0)
if __name__ == '__main__':
    db.create_all()