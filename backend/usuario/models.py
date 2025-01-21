""" from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
 """
from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):

    email = models.EmailField(unique=True)  # E-mail único
    is_admin = models.BooleanField(default=False)

    # Adicione related_name para os campos de relacionamento
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_user_permissions',
    )