from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, BigInteger, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db_conf import Base
from storage import ProfileImage,Json


"""create product models here"""


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    products = relationship('Products', secondary='product_category', )

    def __repr__(self):
        return '<Category %r>' % self.name


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    category = relationship('Category', secondary='product_category', nullable=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    total = Column(Integer, nullable=False, default=0)
    price = Column(BigInteger, nullable=False)
    image = Column(String(250), nullable=True)


class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    total = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_active = Column(Boolean, default=True)
    price = Column(BigInteger, nullable=False)
    image = Column(String(250),nullable=True)
    product = relationship('Products', backref='inventory')


class ProductCategory(Base):
    __tablename__ = "product_category"
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id'), primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    price = Column(BigInteger, nullable=False)
