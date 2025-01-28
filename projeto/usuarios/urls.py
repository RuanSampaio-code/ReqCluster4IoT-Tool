from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('registrar/', views.registrar_usuario, name='registrar'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),

    path('home/registrar/', views.registrar_usuario_home, name='registrar_usuario_home'),

    path('logout/', views.logout_view, name='logout'),
    path('home/', views.pagina_protegida, name='home'),
]
