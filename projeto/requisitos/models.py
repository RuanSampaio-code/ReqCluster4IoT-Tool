# requisitos/models.py
from djongo import models  # Mude de django.db para djongo
from django.conf import settings

class Requisito(models.Model):
    TIPO_CHOICES = [
        ("funcional", "Funcional"),
        ("nao_funcional", "Não Funcional"),
    ]

    # Substitua ForeignKey por IntegerField (armazena o ID do projeto)
    #projeto_id = models.IntegerField()  # ID do Projeto do SQLite
    projeto_id = models.IntegerField(default=0)  # Adicione default=0
    requisito = models.CharField(max_length=255)
    arquivo = models.FileField(upload_to="requisitos/", blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, blank=True, null=True)

    

    class Meta:
        db_table = 'requisitos'  # Nome da coleção no MongoDB

    def __str__(self):
        return f"{self.requisito} (Projeto ID: {self.projeto_id})"
    
