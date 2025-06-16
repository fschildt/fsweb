from django.urls import path

from . import views

app_name = 'fitness'
urlpatterns = [
    path('', views.view_index, name="index"),
    path('strength/', views.view_strength, name='strength'),
    path('strength/add', views.view_strength_add, name='strength_add'),
    path('strength/edit/<int:id>/', views.view_strength_edit, name='strength_edit'),
    path('strength/delete/<int:id>/', views.view_strength_delete, name='strength_delete'),
    path('cardio/', views.view_cardio, name='cardio'),
    path('flexibility/', views.view_flexibility, name='flexibility'),
    path('brain/', views.view_brain, name='brain')
]
