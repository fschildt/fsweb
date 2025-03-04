from django.urls import path

from . import views

app_name = 'fitness-tracker'
urlpatterns = [
    path("", views.index, name="index"),
]
