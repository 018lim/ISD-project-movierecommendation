from django.http import HttpResponse
from django.template import loader

def index(request):
    name = 'Welcome to the first webpage of django'
    temp = loader.get_template('hello_world.html')
    context = {
        'name' : name,
    }#dictionary
    return HttpResponse(temp.render(context, request))

def if_else(request):
    warr=False
    vara = 9
    varb = 8
    temp = loader.get_template('hello_if.html')
    context1 = {
        'warranty': warr,
        'vara': vara,
        'varb': varb,
    }
    return HttpResponse(temp.render(context1, request))

import datetime

def for_loop(request):
    weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    #today = datetime.datetime.today().weekday()
    today = datetime.datetime(2022, 3, 27)
    #today = today.weekday()
    temp = loader.get_template('hello_for.html')
    context3 = {
        'today' : today,
        'weekday' : weekday,
        }
    return HttpResponse(temp.render(context3, request))

def ifequal_func(request):
    vara = 6
    varb = 5
    temp = loader.get_template('hello_ifequal.html')
    context1 = {
        'vara': vara,
        'varb': varb,
    }
    return HttpResponse(temp.render(context1, request))

def filter_func(request):
    name = "HUFS Yongin"
    weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    temp = loader.get_template('hello_filter.html')
    context = {
        'name' : name,
        'weekday' : weekday,
        }
    return HttpResponse(temp.render(context, request))

def today_is(request):
    now = datetime.datetime.now()
    temp = loader.get_template('blog/datetime.html')
    context = {
        'now' : now,
    }
    return HttpResponse(temp.render(context, request))

from django.conf import settings

def home(request):
    now = datetime.datetime.now()
    temp = loader.get_template('blog2/home.html')
    context = {
        'now' : now,
        'base_dir': settings.BASE_DIR,
    }
    return HttpResponse(temp.render(context, request))

def blog(request):
    writer = "Bernardo"
    temp = loader.get_template('blog2/blog.html')
    context = {
        'writer' : writer,
    }
    return HttpResponse(temp.render(context, request))

def index2(request):
    name = 'HUFS'
    cities = [
    {'name': 'Mumbai', 'population': '19,000,000', 'country': 'India'},
    {'name': 'Calcutta', 'population': '15,000,000', 'country': 'India'},
    {'name': 'New York', 'population': '20,000,000', 'country': 'USA'},
    {'name': 'Chicago', 'population': '7,000,000', 'country': 'USA'},
    {'name': 'Tokyo', 'population': '33,000,000', 'country': 'Japan'},
    ]
    temp = loader.get_template('tablecss.html')
    context = {
        'name' : name,
        'cities' : cities,
        }
    return HttpResponse(temp.render(context, request))

def contact(request):
    writer = "Bernardo"
    temp = loader.get_template('contact.html')
    context = {
        'writer' : writer,
    }
    return HttpResponse(temp.render(context, request))
