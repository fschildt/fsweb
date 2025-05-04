from django.shortcuts import render

def view_index(request):
    return render(request, 'tools/index.html')

def view_hangboard_timer(request):
    return render(request, 'tools/hangboard-timer.html')
