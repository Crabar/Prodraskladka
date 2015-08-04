__author__ = 'Crabar'


class DayPlan:
    def __init__(self, breakfast, lunch, dinner):
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner


from .models import *
from random import choice
import functools


def generate_day_plan(people_count):
    breakfast = choice(Dish.objects(type__contains="breakfast").all())
    lunch = choice(Dish.objects(type__contains="lunch").all())
    dinner = choice(Dish.objects(type__contains="dinner").all())
    res = DayPlan(breakfast, lunch, dinner)
    return res


def generate_plan(days, people_count):
    total_plan = [generate_day_plan(people_count) for x in range(days)]
    all_products = list(functools.reduce(lambda x, y: x + y,
                                         map(lambda dish:
                                             dish.breakfast.products + dish.lunch.products
                                             + dish.dinner.products, total_plan),
                                         []))
    summary = {}
    for product in all_products:
        if product.id in summary:
            summary[product.id] += product.amount * people_count
        else:
            summary[product.id] = product.amount * people_count

    return DaysPlan(total_plan, summary)

def remove_day(days_plan, removed_day):
    if removed_day in days_plan:
        days_plan.remove(removed_day)

    return days_plan
