# requisitos/templatetags/grupo_tags.py
from django import template

register = template.Library()

@register.filter
def encontrar_grupo(req_id, grupos):
    for grupo, requisitos in grupos.items():
        # Remove o prefixo "requisito-" se existir
        clean_id = str(req_id).replace('requisito-', '')
        if clean_id in [str(r).replace('requisito-', '') for r in requisitos]:
            return grupo
    return "-"