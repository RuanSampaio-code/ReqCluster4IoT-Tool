from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('registrar/', views.registrar_usuario, name='registrar'),
    path('home/usuario/listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),

    path('home/usuario/', views.gerencia_usuarios, name='gerencia_usuarios'),
    path('home/usuario/novo-usuario', views.novo_usuario, name='novo_usuario'),

    path('logout/', views.logout_view, name='logout'),
    path('home/', views.pagina_protegida, name='home'),
]
