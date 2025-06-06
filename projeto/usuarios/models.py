from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # Campo adicional: Tipo de usuário
    TIPOS_USUARIO = [
        ('admin', 'Administrador'),
        ('normal', 'Usuário Normal'),
    ]
    tipo_usuario = models.CharField(
        max_length=10,
        choices=TIPOS_USUARIO,
        default='normal',
        blank=True  # Isso permite que o campo seja vazio no admin, mas o formulário precisa tratar
    )

    def __str__(self):
        return self.username
