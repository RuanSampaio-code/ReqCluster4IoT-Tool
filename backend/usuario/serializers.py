
from rest_framework import serializers
from usuario.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Habilita o campo de senha somente para escrita

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_admin', 'password']  # Mantém o campo de senha para cadastro

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('password', None)  # Remove o campo 'password' da resposta
        return data