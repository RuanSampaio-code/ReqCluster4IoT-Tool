from django.db import models
from projetos.models import Projeto

class Requisito(models.Model):
    TIPO_CHOICES = [
        ("funcional", "Funcional"),
        ("nao_funcional", "Não Funcional"),
    ]

    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name="requisitos")
    requisito = models.CharField(max_length=255)
    arquivo = models.FileField(upload_to="requisitos/", blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.requisito} ({self.projeto})"

