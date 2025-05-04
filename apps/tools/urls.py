from django.urls import path

from . import views

app_name = 'tools'
urlpatterns = [
    path("", views.view_index, name="index"),
    path("hangboard-timer/", views.view_hangboard_timer, name="hangboard_timer")
]
