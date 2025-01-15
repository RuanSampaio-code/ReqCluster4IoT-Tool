from usuario.models import Usuario
from usuario.serializers import UsuarioSerializer
from rest_framework import viewsets

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer