from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Projeto
from .forms import ProjetoForm
from requisitos.forms import RequisitoFormSet  # Importa o formset de requisitos

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


# views.py (ajuste na view criar_projeto)
@login_required
def criar_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.usuario = request.user
            projeto.save()  # Salva o projeto primeiro
            
            # Agora processa os requisitos associados ao projeto
            formset = RequisitoFormSet(request.POST, request.FILES, instance=projeto)
            
            if formset.is_valid():
                formset.save()  # Salva os requisitos
                messages.success(request, 'Projeto e requisitos criados com sucesso!')
                return redirect('gerencia_projetos')
            else:
                # Se houver erro nos requisitos, deleta o projeto criado (opcional)
                projeto.delete()
                messages.error(request, 'Erro nos requisitos. Verifique os campos.')
        else:
            messages.error(request, 'Erro no projeto. Verifique os campos.')
    else:
        form = ProjetoForm()
        formset = RequisitoFormSet()

    return render(request, 'projetos/criar_projeto.html', {
        'form': form,
        'formset': formset
    })











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
