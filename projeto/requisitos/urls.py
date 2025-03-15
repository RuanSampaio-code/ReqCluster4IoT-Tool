from django.urls import path
from .views import remover_requisito
from .views import adicionar_requisito


urlpatterns = [
    path('home/projetos/requisito/remover-requisito/', remover_requisito, name='remover_requisito'),
    path('adicionar-requisito/', adicionar_requisito, name='adicionar_requisito'),
]