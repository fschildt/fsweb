from django.template import loader
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

    template = loader.get_template('index.html')
    return HttpResponse(template.render())

