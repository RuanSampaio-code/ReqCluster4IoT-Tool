import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Projeto
from .forms import ProjetoForm
from requisitos.forms import RequisitoFormSet  # Importa o formset de requisitos

from pymongo import MongoClient
from django.http import Http404

# Criar cliente MongoDB (pode deixar aqui se preferir, ou usar função/factory)
client = MongoClient('mongodb://mongodb:27017/')
db = client['requisitos_db']
collection = db['requisitos']

def criar_requisito(projeto_id, requisitos, funcionais, nao_funcionais, grupos, caracteristica_grupo, status):
    documento = {
        'projeto_id': projeto_id,
        'requisitos': requisitos,
        'funcionais': funcionais,
        'nao_funcionais': nao_funcionais,
        'grupos': grupos,
        'caracteristica_grupo': caracteristica_grupo,
        'status': status
    }
    try:
        collection.insert_one(documento)
        print("Requisito inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir requisito: {e}")

@login_required
def criar_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)
        formset = RequisitoFormSet(request.POST, request.FILES)
        arquivo_txt = request.FILES.get('arquivo_txt')
        
        if form.is_valid() and formset.is_valid():
            projeto = form.save(commit=False)
            projeto.usuario = request.user
            projeto.save()

            requisitos_data = {}
            counter = 1

            for req_form in formset:
                dados = req_form.cleaned_data
                req_text = dados.get('requisito')
                if req_text:
                    key = str(counter)
                    requisitos_data[key] = {'texto': req_text}
                    counter += 1

            if arquivo_txt:
                requisitos_txt = arquivo_txt.read().decode('utf-8').splitlines()
                for linha in requisitos_txt:
                    linha = linha.strip()
                    if linha:
                        key = str(counter)
                        requisitos_data[key] = {'texto': linha}
                        counter += 1

            criar_requisito(
                projeto_id=projeto.id,
                requisitos=requisitos_data,
                funcionais=[],
                nao_funcionais=[],
                grupos={},
                caracteristica_grupo={},
                status=['Pendente de agrupamento']
            )

            messages.success(request, 'Projeto e requisitos criados!')
            return redirect('gerencia_projetos')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = ProjetoForm()
        formset = RequisitoFormSet()

    return render(request, 'projetos/criar_projeto.html', {
        'form': form,
        'formset': formset
    })

@login_required
def gerencia_projetos(request):
    projetos = Projeto.objects.filter(usuario=request.user)
    form = ProjetoForm()
    formset = RequisitoFormSet()
    return render(request, 'projetos/gerencia_projetos.html', {
        'projetos': projetos,
        'form': form,
        'formset': formset
    })

@login_required
def listar_projetos(request):
    projetos = Projeto.objects.filter(usuario=request.user)
    return render(request, 'projetos/listar.html', {'projetos': projetos})

@login_required
def detalhes_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id, usuario=request.user)
    
    documento = collection.find_one({"projeto_id": projeto.id})
    if not documento:
        raise Http404("Documento de requisitos não encontrado")
    print(documento)
    # Agora você passa para o template o documento inteiro com requisitos, grupos, etc
    return render(request, 'projetos/detalhes_projeto.html', {
        'projeto': projeto,
        'requisito_doc': documento
    })

@login_required
def editar_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id, usuario=request.user)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        formset = RequisitoFormSet(request.POST, request.FILES)  # Sem instance pois requisitos não é Django ORM
        
        if form.is_valid() and formset.is_valid():
            form.save()
            # Você teria que atualizar requisitos no MongoDB manualmente aqui,
            # pois não é possível usar formset.save() com pymongo
            # Ou adapte para salvar os requisitos com pymongo

            messages.success(request, 'Projeto atualizado com sucesso!')
            return redirect('listar_projetos')
        else:
            messages.error(request, 'Erro ao atualizar o projeto. Verifique os campos.')
    else:
        form = ProjetoForm(instance=projeto)
        formset = RequisitoFormSet()

    return render(request, 'projetos/editar.html', {'form': form, 'formset': formset})

@login_required
def deletar_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id, usuario=request.user)
    projeto.delete()

    # Se quiser deletar requisitos relacionados no MongoDB:
    collection.delete_many({"projeto_id": projeto.id})

    messages.success(request, 'Projeto excluído com sucesso!')
    return redirect('gerencia_projetos')
