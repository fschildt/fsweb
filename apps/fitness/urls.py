from django.urls import path

from . import views

app_name = 'fitness'
urlpatterns = [
    path("", views.view_index, name="index"),
    path("strength/", views.view_strength, name="strength"),
    path("cardio/", views.view_cardio, name="cardio"),
    path("flexibility/", views.view_flexibility, name="flexibility"),
    path("brain/", views.view_brain, name="brain")
]
