from django.urls import path

from . import views

urlpatterns = [
    path('', views.podcastList, name = 'podcastList'),
    path('<int:podcast_id>', views.podcastView, name = 'podcastView'),
    path('delete/item/<int:podcast_id>', views.Delete, name='Delete'),
    path('delete/all', views.deleteall, name='deleteall'),
    path('restore/<int:podcast_id>', views.restore, name = 'restore'),
]