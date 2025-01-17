
from django.urls import path
from . import views

urlpatterns = [
    path('', views.example_view, name='example_view'),
    path('cadastro/', views.cadastro, name= 'cadastro'),
    path('login/', views.login, name= 'login'),
    path('home', views.home, name='home'),
   
]