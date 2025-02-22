

# Register your models here.
# requisitos/admin.py
from django.contrib import admin
from .models import Requisito

@admin.register(Requisito)
class RequisitoAdmin(admin.ModelAdmin):
    list_display = ('projeto_id', 'requisito', 'tipo')