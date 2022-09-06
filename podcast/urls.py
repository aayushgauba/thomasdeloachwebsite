from django.urls import path

from . import views

urlpatterns = [
    path('', views.podcastList, name = 'podcastList'),
]