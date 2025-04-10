from django.shortcuts import render


def index(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

    context = {}

    user = request.user
    if user.is_authenticated:
        context['username'] = user.username
    else:
        context['username'] = None

    return render(request, 'index.html', context)

