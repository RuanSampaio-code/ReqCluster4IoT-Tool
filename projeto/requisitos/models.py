# requisitos/models.py
'''
from djongo import models  # Mude de django.db para djongo
from django.conf import settings
from bson import ObjectId


# Adicione esta função no topo do arquivo
def status_default():
    return ["Pendente de agrupamento"]
class Requisito(models.Model):
    _id = models.ObjectIdField(primary_key=True, default=ObjectId)  # Ajustando para MongoDB
    projeto_id = models.IntegerField(unique=True)  # Único por projeto
    requisitos = models.JSONField()  # Armazenará {"1": "texto", "2": "url_arquivo", ...}
    funcionais = models.JSONField(default=list)  # Armazena arrays
    nao_funcionais = models.JSONField(default=list)
    grupos =  models.JSONField()
    caracteristica_grupo = models.JSONField()
    status = models.JSONField(default=status_default)  # Use a função nomeada

    class Meta:
        db_table = 'requisitos'

    def __str__(self):
        return f"Requisitos (Projeto ID: {self.projeto_id})"
'''
     
