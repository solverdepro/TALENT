from django.urls import path 
from . import views

urlpatterns = [
    path('login2/', views.login_view, name='login'),
    path('register2/', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('news/', views.news, name='news')

]