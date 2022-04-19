from django.http import HttpResponse

from django.template import loader

def index(request):
    name = 'Won_Jong_Dae'
    temp = loader.get_template('hello_Jong_Dae.html')
    context = {
        'name' : name,
    }
    return HttpResponse(temp.render(context, request))


def if_else(request):
    answer = 26
    a = 25
    b = 27
    temp = loader.get_template('hello_if.html')
    context1 = {
        'answer' : answer,
        'a': a,
        'b': b,

        }
    return HttpResponse(temp.render(context1, request))

import datetime

def for_loop(request):
    weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    today = datetime.datetime.today().weekday()
    temp = loader.get_template('hello_if.html')
    context = {
        'today' : today,
        'weekday' : weekday,
        }
    return HttpResponse(temp.render(context, request))
