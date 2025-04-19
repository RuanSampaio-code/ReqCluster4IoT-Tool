from django import template

register = template.Library()

@register.filter
def determinar_tipo(key, requisito_doc):
    key_str = str(key)
    
    if key_str in requisito_doc.funcionais:
        return "funcional"
    elif key_str in requisito_doc.nao_funcionais:
        return "não funcional"
    return "não classificado"