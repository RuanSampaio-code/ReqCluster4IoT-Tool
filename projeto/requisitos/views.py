from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import Requisito
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def remover_requisito(request):
    if request.method == "POST":
        projeto_id = request.POST.get("projeto_id")
        requisito_key = request.POST.get("requisito_key")

        # Buscar o documento correto
        requisito_doc = get_object_or_404(Requisito, projeto_id=projeto_id)

        # Remover o requisito do JSON
        if requisito_key in requisito_doc.requisitos:
            del requisito_doc.requisitos[requisito_key]

            # Atualizar o documento existente no MongoDB sem criar um novo
            Requisito.objects.filter(id=requisito_doc.id).update(requisitos=requisito_doc.requisitos)

            # Mensagem de sucesso
            messages.success(request, f"O requisito {requisito_key} foi removido com sucesso!")

        return redirect(f'/projetos/{projeto_id}/')

    return JsonResponse({"error": "Método não permitido"}, status=405)
