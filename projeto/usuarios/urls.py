from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('about/', views.about, name='about'),  # Nome da URL em inglês
    path('registrar/', views.registrar_usuario, name='registrar'),
    path('contatos/', views.contatos, name='contatos'),
    path('home/usuario/', views.gerencia_usuarios, name='gerencia_usuarios'),
    path('home/usuario/editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('home/usuario/novo-usuario', views.novo_usuario, name='novo_usuario'),

    path('home/usuario/editar-usuario/<int:user_id>/', views.editar_usuario, name='editar_usuario'),
    path('home/usuario/deletar-usuario/<int:user_id>/', views.deletar_usuario, name='deletar_usuario'),
   
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.pagina_protegida, name='home'),
]
