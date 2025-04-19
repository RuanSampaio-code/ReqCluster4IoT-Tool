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
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.http import require_http_methods
from .agrupamento import agrupamento

import os

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
    print(json.dumps(documento, cls=DjangoJSONEncoder))
    # Prepara os dados para o template
    contexto = {
        'projeto_id': projeto_id,
        'dados_json': json.dumps(documento, cls=DjangoJSONEncoder),
        'projeto': documento  # Opcional, se precisar de outros dados
    }

    return render(request, 'mindmap-requisitos/req-mind.html', contexto)


@login_required
def classificacao_requisitos(request, projeto_id):
    # Supondo que você tem uma conexão com o MongoDB
    from pymongo import MongoClient
    import os
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
    def extrair_textos(dicionario):
        resultado = {}
        for chave, valor in dicionario.items():
            # Assumindo que 'texto' é sempre uma chave dentro de cada valor
            resultado[chave] = valor.get('texto', '')
        return resultado

    requisitos = extrair_textos(documento["requisitos"])
    import tensorflow as tf
    from transformers import TFAutoModelForSequenceClassification, AutoTokenizer, pipeline

    # Verifica se há GPU disponível
    device = 0 if tf.config.list_physical_devices('GPU') else -1

    # Caminho do modelo
    #model_path = './modelo_classificacao'
    #model_path = 'modelo_classificacao'

    

    # Obtém o diretório atual onde o script está sendo executado
    diretorio_atual = os.getcwd()

    # Nome da pasta que está na mesma raiz
    nome_da_pasta = "requisitos\modelo_classificacao"

    # Constrói o caminho completo adicionando o nome da pasta
    model_path = os.path.join(diretorio_atual, nome_da_pasta)
    print(model_path)


    # Verifique se o caminho existe
    if os.path.exists(model_path):
        # Carregar o modelo e tokenizer a partir do diretório local
        model = TFAutoModelForSequenceClassification.from_pretrained(model_path)
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        print("Modelo e tokenizer carregados com sucesso!")
    else:
        print("O diretório do modelo não foi encontrado.")

    # Inicializa o pipeline com o dispositivo adequado
    classifier = pipeline("text-classification", model=model, tokenizer=tokenizer, device=device)
    funcionais = []
    nao_funcionais = []
    for identificador, requisito in requisitos.items():
        if classifier(requisito)[0]['label'] =="F":
            funcionais.append(identificador)
        else:
            nao_funcionais.append(identificador)
    collection.update_one(
        {"projeto_id": int(projeto_id)},  # Filtra pelo projeto_id
        {
            "$set": {
                "funcionais": funcionais,
                "nao_funcionais": nao_funcionais
            }
        }
    )

    return redirect(f'/projetos/{projeto_id}/')

@login_required
def agrupamento_requisitos(request, projeto_id):
    def extrair_textos(dicionario):
        resultado = {}
        for chave, valor in dicionario.items():
            # Assumindo que 'texto' é sempre uma chave dentro de cada valor
            resultado[chave] = valor.get('texto', '')
        return resultado
    # Supondo que você tem uma conexão com o MongoDB
    from pymongo import MongoClient
    import os
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
    def extrair_textos(dicionario):
        resultado = {}
        for chave, valor in dicionario.items():
            # Assumindo que 'texto' é sempre uma chave dentro de cada valor
            resultado[chave] = valor.get('texto', '')
        return resultado
    
    requisitos = extrair_textos(documento["requisitos"])

    # Validação para agrupar apenas os requisitos que ja foram classificados
    if not documento.get("funcionais"):
        messages.error(request, "Não é possível realizar o agrupamento: Nenhum requisito foi classificado como funcional.")
        return redirect(f'/projetos/{projeto_id}/')  # ou renderizar uma template específica
    
    # Validação: verificar se existem pelo menos 4 requisitos funcionais
    if len(documento["funcionais"]) < 4:
        messages.error(request, "Não é possível realizar o agrupamento: É necessário pelo menos 4 requisitos classificados.")
        return redirect(f'/projetos/{projeto_id}/')


    requisitos_funcionais = [requisitos[i] for i in documento["funcionais"]]

    collection.update_one(
        {"projeto_id": int(projeto_id)},  # Filtra pelo projeto_id
        {
            "$set": {
                "grupos": agrupamento(requisitos_funcionais,documento["funcionais"]),
            }
        }
    )

    return redirect(f'/projetos/{projeto_id}/')


""" 
@login_required
def remover_requisito(request):
    if request.method == "POST":
        projeto_id = request.POST.get("projeto_id")
        requisito_key = request.POST.get("requisito_key")

        # Buscar o documento correto com base no projeto_id
        requisito_doc = get_object_or_404(Requisito, projeto_id=projeto_id)
        # Verificar se o requisito existe e remover da lista "requisitos"
        if requisito_key in requisito_doc.requisitos:
            del requisito_doc.requisitos[requisito_key]

            # Remover o requisito de todos os grupos em "grupos"
            grupos_atualizados = requisito_doc.grupos.copy()
            if requisito_doc.grupos:
                
                for grupo_nome, requisitos_ids in grupos_atualizados.items():
                    if requisito_key in requisitos_ids:
                        requisitos_ids.remove(requisito_key)
                        # Opcional: Remover o grupo se ficar vazio
                        if not requisitos_ids:
                            del grupos_atualizados[grupo_nome]
            if requisito_doc.funcionais:
                funcionais_atualizados = requisito_doc.funcionais.copy()
                if requisito_key in requisito_doc.funcionais:
                    funcionais_atualizados.pop(funcionais_atualizados.index(requisito_key))

            nao_funcionais_atualizados = requisito_doc.nao_funcionais.copy()
            if requisito_doc.nao_funcionais:
                
                if requisito_key in requisito_doc.nao_funcionais:
                    nao_funcionais_atualizados.pop(nao_funcionais_atualizados.index(requisito_key))

            # Atualizar os grupos no documento
            requisito_doc.grupos = grupos_atualizados
            requisito_doc.funcionais = funcionais_atualizados
            requisito_doc.nao_funcionais = nao_funcionais_atualizados

            # Salvar as alterações no banco de dados
            print(requisito_doc.funcionais)
            requisito_doc.save()

            messages.success(request, f"Requisito {requisito_key} removido com sucesso!")

        return redirect(f'/projetos/{projeto_id}/')

    return JsonResponse({"error": "Método não permitido"}, status=405)

 """
@login_required
def remover_requisito(request):
    if request.method == "POST":
        projeto_id = request.POST.get("projeto_id")
        requisito_key = request.POST.get("requisito_key")

        # Buscar o documento correto com base no projeto_id
        requisito_doc = get_object_or_404(Requisito, projeto_id=projeto_id)

        # Verificar se o requisito existe e remover da lista "requisitos"
        if requisito_key in requisito_doc.requisitos:
            del requisito_doc.requisitos[requisito_key]

            # Remover o requisito de todos os grupos em "grupos"
            grupos_atualizados = requisito_doc.grupos.copy() if requisito_doc.grupos else {}
            
            for grupo_nome, requisitos_ids in grupos_atualizados.items():
                if requisito_key in requisitos_ids:
                    requisitos_ids.remove(requisito_key)
                    # Remover o grupo se ficar vazio
                    if not requisitos_ids:
                        del grupos_atualizados[grupo_nome]

            # Inicializar as listas antes do uso para evitar UnboundLocalError
            funcionais_atualizados = requisito_doc.funcionais.copy() if requisito_doc.funcionais else []
            nao_funcionais_atualizados = requisito_doc.nao_funcionais.copy() if requisito_doc.nao_funcionais else []

            # Remover o requisito das listas funcionais e não funcionais
            if requisito_key in funcionais_atualizados:
                funcionais_atualizados.remove(requisito_key)

            if requisito_key in nao_funcionais_atualizados:
                nao_funcionais_atualizados.remove(requisito_key)

            # Atualizar os grupos e listas no documento
            requisito_doc.grupos = grupos_atualizados
            requisito_doc.funcionais = funcionais_atualizados
            requisito_doc.nao_funcionais = nao_funcionais_atualizados

            # Salvar as alterações no banco de dados
            requisito_doc.save()

            messages.success(request, f"Requisito {requisito_key} removido com sucesso!")

        return redirect(f'/projetos/{projeto_id}/')

    return JsonResponse({"error": "Método não permitido"}, status=405)





@login_required
def adicionar_requisito(request):
    if request.method == "POST":
        projeto_id = request.POST.get("projeto_id")
        texto = request.POST.get("requisito_texto")

        client = MongoClient('mongodb://localhost:27017/')
        db = client['requisitos_db']
        collection = db['requisitos']
        projeto_mongo = collection.find_one({"projeto_id": int(projeto_id)})

        if not projeto_mongo:
            return JsonResponse({"error": "Projeto não encontrado"}, status=404)

        requisitos = projeto_mongo.get("requisitos", {})

        # Encontrar o próximo ID sequencial
        numeros_existentes = []
        for key in requisitos.keys():
            try:
                num = int(key)
                numeros_existentes.append(num)
            except ValueError:
                pass
        proximo_id = max(numeros_existentes) + 1 if numeros_existentes else 1
        novo_id = str(proximo_id)

        # Adicionar o novo requisito
        collection.update_one(
            {"projeto_id": int(projeto_id)},
            {"$set": {f"requisitos.{novo_id}": {"texto": texto}}}
        )
        messages.success(request, f"Requisito {novo_id} adicionado com sucesso!")

        return JsonResponse({"success": True, "novo_id": novo_id})

    return JsonResponse({"error": "Método não permitido"}, status=405)




@login_required
def atualizar_agrupamento(request, projeto_id):
    if request.method == 'POST':
        try:
            projeto_mongo = Requisito.objects.get(projeto_id=int(projeto_id))
            raw_data = json.loads(request.body)

            # Validar grupos e requisitos
            valid_grupos = {}
            for grupo, req_ids in raw_data.get('grupos', {}).items():
                valid_reqs = []
                for req_id in req_ids:
                    if str(req_id) in projeto_mongo.requisitos:
                        valid_reqs.append(str(req_id))
                valid_grupos[grupo] = valid_reqs

            projeto_mongo.grupos = valid_grupos
            projeto_mongo.save()

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
        






""" 

""" 

@login_required
def get_mindmap_data(request, projeto_id):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['requisitos_db']
    collection = db['requisitos']

    documento = collection.find_one({"projeto_id": int(projeto_id)})
    print(documento["grupos"])
    if not documento:
        return JsonResponse({'error': 'Projeto não encontrado'}, status=404)

    mind_data = {
        "nodeData": {
            "id": str(documento["_id"]),
            "topic": f"Projeto {projeto_id}",
            "children": []
        }
    }

    for grupo, requisitos in documento.get("grupos", {}).items():
        grupo_node = {
            "id": grupo,
            "topic": grupo,
            "children": []
        }
        for req_id in requisitos:
            req_texto = documento["requisitos"].get(req_id, {}).get("texto", "Sem texto")
            grupo_node["children"].append({
                "id": f"requisito-{req_id}",
                "topic": req_texto
            })

        mind_data["nodeData"]["children"].append(grupo_node)

    return JsonResponse(mind_data) 


""" 
@csrf_exempt
def save_mindmap_data(request, projeto_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método não permitido'}, status=405)

    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client['requisitos_db']
        collection = db['requisitos']

        # Buscar documento do projeto no MongoDB
        projeto_mongo = collection.find_one({"projeto_id": int(projeto_id)})
        if not projeto_mongo:
            return JsonResponse({'error': 'Projeto não encontrado'}, status=404)

        raw_data = json.loads(request.body)

        # Inicializar requisitos e grupos se não existirem
        if "requisitos" not in projeto_mongo:
            projeto_mongo["requisitos"] = {}
        if "grupos" not in projeto_mongo:
            projeto_mongo["grupos"] = {}

        novos_grupos = {}
        novos_requisitos = projeto_mongo.get("requisitos", {})

        for grupo in raw_data.get("nodeData", {}).get("children", []):
            grupo_id = grupo["id"]
            novos_grupos[grupo_id] = []

            for req in grupo.get("children", []):
                req_id = req["id"].replace("requisito-", "")
                req_texto = req["topic"]

                # Se for um novo requisito, adicionar ao dicionário de requisitos
                if req_id not in novos_requisitos:
                    novos_requisitos[req_id] = {"texto": req_texto}

                novos_grupos[grupo_id].append(req_id)

        # Atualizando os dados no MongoDB
        collection.update_one(
            {"projeto_id": int(projeto_id)},
            {"$set": {"grupos": novos_grupos, "requisitos": novos_requisitos}}
        )

        return JsonResponse({'status': 'success'})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
 """

@csrf_exempt
def save_mindmap_data(request, projeto_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método não permitido'}, status=405)

    try:
        client = MongoClient('mongodb://localhost:27017/')
        db = client['requisitos_db']
        collection = db['requisitos']

        # Buscar documento do projeto no MongoDB
        projeto_mongo = collection.find_one({"projeto_id": int(projeto_id)})
        
        if not projeto_mongo:
            return JsonResponse({'error': 'Projeto não encontrado'}, status=404)

        raw_data = json.loads(request.body)

        novos_grupos = {}
        import copy
        novos_requisitos = copy.deepcopy(projeto_mongo.get("requisitos", {}))  # Mantém requisitos existentes
        requisitos_originais = projeto_mongo["requisitos"]
        novos_funcionais=set()
        # Processar grupos do MindElixir
        for grupo_node in raw_data.get("nodeData", {}).get("children", []):
            # Usar o 'topic' como nome do grupo (chave no dicionário)
            grupo_nome = grupo_node.get("topic", "Novo Grupo").strip()  # Nome digitado pelo usuário
            
            # Coletar IDs dos requisitos neste grupo
            requisitos_ids = []
            for req_node in grupo_node.get("children", []):
                req_id = req_node["id"].replace("requisito-", "")
                req_texto = req_node["topic"]
                if req_id not in requisitos_originais.keys():
                    req_id = max(map(int, requisitos_originais.keys()))+1
                    req_id = str(req_id)
                    novos_funcionais.add(req_id)
                   
                # Atualizar/Criar requisito se necessário
                if req_id not in novos_requisitos:
                    novos_requisitos[req_id] = {"texto": req_texto}
                else:
                    # Atualiza texto se alterado
                    novos_requisitos[req_id]["texto"] = req_texto
                
                requisitos_ids.append(req_id)

            # Adicionar ao dicionário de grupos
            novos_grupos[grupo_nome] = requisitos_ids
       
        projeto_mongo["funcionais"].extend(novos_funcionais)
        funcionais = projeto_mongo["funcionais"]
       
       
        # Atualizar o documento no MongoDB

        collection.update_one(
            {"projeto_id": int(projeto_id)},
            {
                "$set": {
                    "grupos": novos_grupos,
                    "requisitos": novos_requisitos,
                    "funcionais": funcionais
                }
            }
        )

        return JsonResponse({'status': 'success'})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    


@login_required    
@require_http_methods(["GET", "POST"])
def editar_requisito(request, projeto_id, requisito_id):
    try:
        # Busca exata por projeto_id
        requisito_doc = Requisito.objects.get(projeto_id=projeto_id)

        # Se for um POST, atualizar os dados
        if request.method == 'POST':
            novo_texto = request.POST.get('texto', '')
            novo_tipo = request.POST.get('tipo', '')

            # Atualiza o requisito
            requisito_doc.requisitos.setdefault(requisito_id, {})['texto'] = novo_texto

            # Atualiza listas de funcionais/não funcionais
            if novo_tipo == 'funcional':
                if requisito_id not in requisito_doc.funcionais:
                    requisito_doc.funcionais.append(requisito_id)
                if requisito_id in requisito_doc.nao_funcionais:
                    requisito_doc.nao_funcionais.remove(requisito_id)
            elif novo_tipo == 'nao_funcional':
                if requisito_id not in requisito_doc.nao_funcionais:
                    requisito_doc.nao_funcionais.append(requisito_id)
                if requisito_id in requisito_doc.funcionais:
                    requisito_doc.funcionais.remove(requisito_id)

            # Atualiza o documento no MongoDB
            requisito_doc.save()  # Djongo pode falhar com update_fields, então removemos

            messages.success(request, f"Requisito {requisito_id} alterado com sucesso!")

            return JsonResponse({'status': 'success'})

        # Retorno para GET
        return JsonResponse({
            'texto': requisito_doc.requisitos.get(requisito_id, {}).get('texto', ''),
            'tipo': 'funcional' if requisito_id in requisito_doc.funcionais else 
                   'nao_funcional' if requisito_id in requisito_doc.nao_funcionais else ''
        })

    except Requisito.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Projeto não encontrado'}, status=404)

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
