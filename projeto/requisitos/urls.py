from django.urls import path
from .views import remover_requisito

urlpatterns = [
    path('remover-requisito/', remover_requisito, name='remover_requisito'),
]