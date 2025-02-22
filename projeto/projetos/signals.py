# projetos/signals.py
# projetos/signals.py
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.apps import apps  # Importe apps para evitar dependência circular

@receiver(pre_delete, sender='projetos.Projeto')  # Especifique o sender como string
def deletar_requisitos(sender, instance, **kwargs):
    Requisito = apps.get_model('requisitos', 'Requisito')  # Obtenha o modelo dinamicamente
    Requisito.objects.using('mongodb').filter(projeto_id=instance.id).delete()
