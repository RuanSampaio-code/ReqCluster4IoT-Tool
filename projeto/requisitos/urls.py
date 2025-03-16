from django.urls import path
from .views import remover_requisito,adicionar_requisito, visualizacao_agrupamento, visualizacao_agrupamento



urlpatterns = [
    path('home/projetos/requisito/remover-requisito/', remover_requisito, name='remover_requisito'),
    path('adicionar-requisito/', adicionar_requisito, name='adicionar_requisito'),
    path('manipula-requisito/<int:projeto_id>/', visualizacao_agrupamento, name='visualizacao_agrupamento' ), 
    #path('atualizar-agrupamento/<int:projeto_id>/', views.atualizar_agrupamento, name='atualizar_agrupamento'),
]