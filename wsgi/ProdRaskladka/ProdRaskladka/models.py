__author__ = 'Crabar'
from mongoengine import *
from django.db import models



class Product(Document):
    name = StringField(required=True)

class ProductWithAmount(DynamicEmbeddedDocument):
    id = ReferenceField(Product)
    amount = IntField()

class Dish(Document):
    name = StringField(required=True)
    products = ListField(EmbeddedDocumentField(ProductWithAmount), required=True)
    type = StringField(required=True)