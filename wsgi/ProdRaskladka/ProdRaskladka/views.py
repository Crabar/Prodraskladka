__author__ = 'Crabar'

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .core import *
from octopus.views import OctopusTemplateView
from .models import *


def generate(request):
    try:
        people_count = int(request.POST["peopleCount"])
        days_count = int(request.POST["daysCount"])
    except ValueError:
        return render(request, "food_item.html", {'error_message': "You didn't provide all necessary information!"})

    result = generate_plan(days_count, people_count)
    request.session["days_plan"] = result
    return render(request, "food_item.html", {"days_plan": result})

def delete(request):
    days_plan = request.session["days_plan"]
    removed_day = request.POST["deletedElement"]
    days_plan = remove_day(days_plan, removed_day)
    return render(request, "food_item.html", {"days_plan": days_plan})


class IndexView(OctopusTemplateView):
    template_name = 'index.html'


