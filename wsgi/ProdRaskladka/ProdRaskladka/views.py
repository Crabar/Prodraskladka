__author__ = 'Crabar'

from .models import Product
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .core import *


def home(request):
    return render(request, 'index.html')

def generate(request):
    try:
        people_count = int(request.POST["peopleCount"])
        days_count = int(request.POST["daysCount"])
    except ValueError:
        return render(request, 'index.html', {'error_message': "You didn't provide all necessary information!"})

    plan = generate_plan(days_count, people_count)
    return render(request, "index.html", {"plan": plan})