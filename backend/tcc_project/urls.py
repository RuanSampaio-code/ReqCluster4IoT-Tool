
from django.contrib import admin
from django.urls import path, include
from usuario.views import UsuarioViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('usuarios', UsuarioViewSet, basename= 'Usuarios')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuario.urls')),
    path('', include(router.urls)),
   
    #path('usuarios', include('usuario.urls')),
]
