from django.urls import path
from .views import remover_requisito
from .views import adicionar_requisito
from .views import visualizacao_agrupamento
from .views import atualizar_agrupamento
from .views import get_mindmap_data
from .views import save_mindmap_data
from .views import editar_requisito
from .views import classificacao_requisitos
from .views import agrupamento_requisitos
from .views import processar_agrupamento

urlpatterns = [
    path('home/projetos/requisito/remover-requisito/', remover_requisito, name='remover_requisito'),
    path('adicionar-requisito/', adicionar_requisito, name='adicionar_requisito'),
    path('manipula-requisito/<int:projeto_id>/', visualizacao_agrupamento, name='visualizacao_agrupamento' ), 
    path('atualizar-agrupamento/<int:projeto_id>/',atualizar_agrupamento,name='atualizar_agrupamento'),
    path('api/mindmap/<int:projeto_id>/', get_mindmap_data, name='get_mindmap_data'),
    path('api/mindmap/save/<int:projeto_id>/', save_mindmap_data, name='save_mindmap_data'),
    path('classificacao-requisitos/<int:projeto_id>/', classificacao_requisitos, name='classificacao_requisitos' ), 
    path('agrupamento-requisitos/<int:projeto_id>/', agrupamento_requisitos, name='agrupamento_requisitos' ), 
    path('home/projetos/requisito/editar/<int:projeto_id>/<str:requisito_id>/', 
         editar_requisito, 
         name='editar_requisito'),
    path('processar-agrupamento/<int:projeto_id>/', processar_agrupamento, name='processar_agrupamento'),
         
   
]