from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hangboard-timer", views.hangboard_timer, name="hangboard-timer")
]
