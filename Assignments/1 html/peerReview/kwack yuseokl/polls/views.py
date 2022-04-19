from django.http import HttpResponse

from django.template import loader

def index(request):
    name = 'HUFS'
    temp = loader.get_template('메인 화면.html')
    context = {
        'name' : name,
    }
    return HttpResponse(temp.render(context, request))
