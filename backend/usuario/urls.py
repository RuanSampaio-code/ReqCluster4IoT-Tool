
from django.urls import path
from . import views
from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'register', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('cadastro/', views.cadastro, name= 'cadastro'),
    path('login/', views.login, name= 'login'),
    path('home', views.home, name='home'),
    path('example/', views.example_view, name='example'),
   
]