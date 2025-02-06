

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Projeto
from .forms import ProjetoForm  # Vamos criar o formulário no próximo passo
from django.contrib import messages


@login_required
def gerencia_projetos(request):
    return render(request, 'projetos/gerencia_projetos.html')



@login_required
def listar_projetos(request):
    projetos = Projeto.objects.filter(usuario=request.user)
    return render(request, 'projetos/listar.html', {'projetos': projetos})
@login_required
def criar_projeto(request):
    if request.method == 'POST':
        # Adicionar request.FILES para processar arquivos
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.usuario = request.user
            projeto.save()
            # Redirecionar para a página desejada após sucesso
            return redirect('gerencia_projetos')  # Verifique o nome correto da sua URL
        else:
            # Adicionar tratamento de erros
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = ProjetoForm()
    
    # Se houver erros, reexibir o modal com os erros
    return render(request, 'seu_template.html', {'form': form})

@login_required
def editar_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id, usuario=request.user)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('listar_projetos')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'projetos/editar.html', {'form': form})

@login_required
def deletar_projeto(request, id):
    projeto = get_object_or_404(Projeto, id=id, usuario=request.user)
    projeto.delete()
    return redirect('listar_projetos')