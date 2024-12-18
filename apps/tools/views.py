from django.template import loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('tools/index.html')
    return HttpResponse(template.render())

def hangboard_timer(request):
    template = loader.get_template('tools/hangboard-timer.html')
    return HttpResponse(template.render())
