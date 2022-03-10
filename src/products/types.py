from graphene_sqlalchemy import SQLAlchemyObjectType
from .models import Category, Products, Inventory


class CategoryType(SQLAlchemyObjectType):
    class Meta:
        model = Category
        only_fields = ('id', 'name')


class ProductType(SQLAlchemyObjectType):
    
    class Meta:
        model = Products
        only_fields = ('name', 'description', 'total','price',)



class InventoryType(SQLAlchemyObjectType):
    class Meta:
        model = Inventory
        only_fields = ('id', 'total', 'price', 'product_id')                
        