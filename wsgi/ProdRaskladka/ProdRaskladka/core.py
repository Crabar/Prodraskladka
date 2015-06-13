__author__ = 'Crabar'

class DayPlan:
    def __init__(self, breakfast, lunch, dinner):
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner


from .models import *
from random import choice

def generate_day_plan(people_count):
    breakfast = choice(Dish.objects(type__contains="breakfast").all())
    lunch = {} #choice(Dish.objects(type__contains="lunch").all())
    dinner = choice(Dish.objects(type__contains="dinner").all())
    res = DayPlan(breakfast, lunch, dinner)
    return res

def generate_plan(days, people_count):
    total_plan = [generate_day_plan(people_count) for x in range(days)]
    return total_plan
