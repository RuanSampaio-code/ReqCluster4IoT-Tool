from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_usuario, name='registrar'),
    path('listar_usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.pagina_protegida, name='protegida'),
]
