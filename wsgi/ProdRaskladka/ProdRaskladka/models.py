__author__ = 'Crabar'
from mongoengine import *
from django.db import models

class Product(Document):
    name = StringField(required=True)

class Dish(Document):
    name = StringField(required=True)
    products = ListField(ReferenceField(Product), required=True)
    type = StringField(required=True)