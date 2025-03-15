from django.urls import path
from .views import remover_requisito

urlpatterns = [
    path('home/projetos/requisito/remover-requisito/', remover_requisito, name='remover_requisito'),
]