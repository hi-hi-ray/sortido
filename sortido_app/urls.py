from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('csv', views.random_csv),
    path('about', views.about),
    path('numbers', views.random_numbers),
    path('meetup', views.random_meetup, name='meetup'),
]
