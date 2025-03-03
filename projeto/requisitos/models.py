# requisitos/models.py
from djongo import models  # Mude de django.db para djongo
from django.conf import settings


# Adicione esta função no topo do arquivo
def status_default():
    return ["Pendente de agrupamento", "agrupamento automático", "agrupamento personalizado"]
class Requisito(models.Model):
    projeto_id = models.IntegerField(unique=True)  # Único por projeto
    requisitos = models.JSONField()  # Armazenará {"1": "texto", "2": "url_arquivo", ...}
    funcionais = models.JSONField()
    nao_funcionais = models.JSONField()
    grupos =  models.JSONField()
    caracteristica_grupo = models.JSONField()
    status = models.JSONField(default=status_default)  # Use a função nomeada

    class Meta:
        db_table = 'requisitos'

    def __str__(self):
        return f"Requisitos (Projeto ID: {self.projeto_id})"

""" class Requisito(models.Model):
    TIPO_CHOICES = [
        ("funcional", "Funcional"),
        ("nao_funcional", "Não Funcional"),
    ]


    projeto_id = models.IntegerField(default=0)  # Adicione default=0
    requisito = models.CharField(max_length=255)
    arquivo = models.FileField(upload_to="requisitos/", blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, blank=True, null=True)


    class Meta:
        db_table = 'requisitos'  # Nome da coleção no MongoDB

    def __str__(self):
        return f"{self.requisito} (Projeto ID: {self.projeto_id})"
     """
