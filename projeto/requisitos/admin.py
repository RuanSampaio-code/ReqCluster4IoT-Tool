

# Register your models here.
# requisitos/admin.py
from django.contrib import admin
from .models import Requisito

class RequisitoAdmin(admin.ModelAdmin):
    list_display = ['projeto_id', 'requisitos_count']  # Campos personalizados
    search_fields = ['projeto_id']
    
    def requisitos_count(self, obj):
        return len(obj.requisitos) if obj.requisitos else 0
    requisitos_count.short_description = "Qtd. Requisitos"

admin.site.register(Requisito, RequisitoAdmin)