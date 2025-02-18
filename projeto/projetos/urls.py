from django.urls import path
from . import views

urlpatterns = [
    path('home/projetos/', views.gerencia_projetos, name='gerencia_projetos'),
    path('home/projetos/novo/', views.criar_projeto, name='criar_projeto'),
    path('projetos/<int:id>/', views.detalhes_projeto, name='detalhes_projeto'),


    path('editar/<int:id>/', views.editar_projeto, name='editar_projeto'),
    path('deletar/<int:id>/', views.deletar_projeto, name='deletar_projeto'),
]