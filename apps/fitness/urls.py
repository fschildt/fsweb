from django.urls import path

from . import views

app_name = 'fitness'
urlpatterns = [
    path("", views.index, name="index"),
    path("hangboard-timer/", views.hangboard_timer, name="hangboard_timer")
]
