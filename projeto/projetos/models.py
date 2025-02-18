from django.db import models
from django.conf import settings  # Para usar o modelo de usuário padrão do Django

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projetos')
    data_criacao = models.DateTimeField(auto_now_add=True)
    requisitos_digitados = models.TextField(blank=True)  # ← Campo necessário
    arquivo_requisitos = models.FileField(upload_to='requisitos/', blank=True, null=True)  # Campo para upload do arquivo

    def __str__(self):
        return self.nome