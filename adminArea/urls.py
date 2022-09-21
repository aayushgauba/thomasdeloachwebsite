from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name = 'dashboard'),
    path('upload', views.upload, name = 'upload'),
    path('signin', views.signin, name = 'signin'),
    path('signup', views.signup, name = 'signup'),
    path('signout', views.signout, name = 'signout'),
    path('recycle', views.recycle, name = 'recycle'),
    path('edit/text/<int:podcast_id>', views.editText, name = 'editText'),
    path('edit/file/<int:podcast_id>', views.fileupdate, name = 'fileupdate'),
]