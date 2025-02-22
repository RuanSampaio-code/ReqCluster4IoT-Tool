# projetos/apps.py
from django.apps import AppConfig  # Adicione esta linha

class ProjetosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'projetos'

    def ready(self):
        import projetos.signals  # Importe os sinais aqui