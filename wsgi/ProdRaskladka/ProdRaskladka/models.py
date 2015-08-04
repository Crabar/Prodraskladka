__author__ = 'Crabar'
from mongoengine import *


class ProductWithAmount(DynamicEmbeddedDocument):
    id = StringField()
    amount = IntField()


class Dish(Document):
    name = StringField(required=True)
    products = ListField(EmbeddedDocumentField(ProductWithAmount), required=True)
    type = StringField(required=True)


class DaysPlan:
    plan = []
    summary = {}

    def __init__(self, plan, summary):
        self.plan = plan
        self.summary = summary
