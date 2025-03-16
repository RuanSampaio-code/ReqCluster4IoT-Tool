from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import Requisito
from projetos.models import Projeto
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json
from django.shortcuts import render
from pymongo import MongoClient
from django.core.serializers.json import DjangoJSONEncoder



@login_required
def visualizacao_agrupamento(request, projeto_id):
    # Supondo que você tem uma conexão com o MongoDB
    from pymongo import MongoClient
    client = MongoClient('mongodb://localhost:27017/')
    db = client['requisitos_db']
    collection = db['requisitos']

    # Busca o documento no MongoDB pelo projeto_id
    documento = collection.find_one({"projeto_id": int(projeto_id)})

    if not documento:
        return render(request, 'erro.html', {'mensagem': 'Projeto não encontrado'})

    # Converter ObjectId para string
    if '_id' in documento:
        documento['_id'] = str(documento['_id'])

    # Prepara os dados para o template
    contexto = {
        'projeto_id': projeto_id,
        'dados_json': json.dumps(documento, cls=DjangoJSONEncoder),
        'projeto': documento  # Opcional, se precisar de outros dados
    }

    return render(request, 'mindmap-requisitos/req-mind.html', contexto)




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



@login_required
def adicionar_requisito(request):
    if request.method == "POST":
        projeto_id = request.POST.get("projeto_id")
        texto = request.POST.get("requisito_texto")
        #tipo = request.POST.get("requisito_tipo", "Não especificado")
        #grupo = request.POST.get("requisito_grupo", "-")

        requisito_doc = get_object_or_404(Requisito, projeto_id=projeto_id)

        # Criando uma chave única para o novo requisito
        novo_id = str(len(requisito_doc.requisitos) + 1)

        # Adicionando ao JSON
        requisito_doc.requisitos[novo_id] = {
            "texto": texto,
            #"tipo": tipo,
            #"grupo": grupo
        }

        # Atualizando no banco
        Requisito.objects.filter(id=requisito_doc.id).update(requisitos=requisito_doc.requisitos)

        return JsonResponse({"success": True})

    return JsonResponse({"error": "Método não permitido"}, status=405)


