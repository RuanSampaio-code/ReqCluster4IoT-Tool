from django.urls import path
from . import views

urlpatterns = [
    path('home/projetos/', views.gerencia_projetos, name='gerencia_projetos'),
    path('', views.listar_projetos, name='listar_projetos'),
    path('home/proejtos/novo/', views.criar_projeto, name='criar_projeto'),
    path('editar/<int:id>/', views.editar_projeto, name='editar_projeto'),
    path('deletar/<int:id>/', views.deletar_projeto, name='deletar_projeto'),
]