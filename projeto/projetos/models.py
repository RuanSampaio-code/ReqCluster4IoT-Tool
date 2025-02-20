

from django.db import models
from django.conf import settings

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projetos')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome