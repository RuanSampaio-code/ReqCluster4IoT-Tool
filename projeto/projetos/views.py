from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Projeto
from .forms import ProjetoForm
from requisitos.forms import RequisitoFormSet  # Importa o formset de requisitos
from requisitos.models import Requisito




@login_required
def criar_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)
        formset = RequisitoFormSet(request.POST, request.FILES)
        
        if form.is_valid() and formset.is_valid():
            # Salva o projeto no SQLite
            projeto = form.save(commit=False)
            projeto.usuario = request.user
            projeto.save()
             # Processar arquivo separadamente
            arquivo = request.FILES.get('arquivo')

            # Salva os requisitos no MongoDB
            for requisito_form in formset:
                if requisito_form.has_changed():
                    dados = requisito_form.cleaned_data
                    if dados.get('requisito') or dados.get('arquivo'):
                        Requisito.objects.using('mongodb').create(
                            projeto_id=projeto.id,  # Armazena o ID do projeto
                            requisito=dados.get('requisito'),
                            arquivo=dados.get('arquivo'),
                            tipo=dados.get('tipo')
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






# views.py (exemplo atualizado da view gerencia_projetos)
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
    return render(request, 'projetos/detalhes_projeto.html', {'projeto': projeto})






@login_required
def editar_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id, usuario=request.user)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        formset = RequisitoFormSet(request.POST, request.FILES, instance=projeto)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, 'Projeto atualizado com sucesso!')
            return redirect('listar_projetos')
        else:
            messages.error(request, 'Erro ao atualizar o projeto. Verifique os campos.')

    else:
        form = ProjetoForm(instance=projeto)
        formset = RequisitoFormSet(instance=projeto)

    return render(request, 'projetos/editar.html', {'form': form, 'formset': formset})






@login_required
def deletar_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id, usuario=request.user)
    projeto.delete()
    messages.success(request, 'Projeto excluído com sucesso!')
    return redirect('gerencia_projetos')
