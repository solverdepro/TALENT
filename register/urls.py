from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homeView'),
    path('upload/', views.upload_media, name='uploadMediaView'),
    path('success/', views.upload_success, name='uploadSuccessView'),
]