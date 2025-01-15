from django.contrib import admin
from .models import Usuario  # Substitua `.models` pelo nome correto do seu arquivo/modelo

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'is_admin')  # Campos que deseja exibir
    list_display_links = ('id', 'nome')  # Campos linkáveis
    list_per_page = 20  # Número de registros por página
    search_fields = ('nome', 'email')  # Campos pesquisáveis

admin.site.register(Usuario, UsuarioAdmin)
