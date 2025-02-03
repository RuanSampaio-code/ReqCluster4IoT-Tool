from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import RegistroUsuarioForm
from .models import CustomUser

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroUsuarioForm, EditarPerfilForm
from django.contrib.auth import update_session_auth_hash


#Tela de login
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)  # Agora usa o backend customizado
        if user is not None:
            login(request, user)  # Autentica o usuário
            return redirect('home') # Redireciona para a página protegida
        else:
            return render(request, 'usuarios/login.html', {'error': 'Usuário ou senha inválidos'})

    return render(request, 'usuarios/login.html')

#pagina de novo usuario
@login_required
def novo_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            # Criação do usuário
            usuario = CustomUser(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=make_password(form.cleaned_data['senha']),
                tipo_usuario=form.cleaned_data['tipo_usuario'],
            )
            usuario.save()
        
            return redirect('gerencia_usuarios')  # Redirecionar para a página de login
    else:
        form = RegistroUsuarioForm()

    return render(request, 'usuarios/novo_usuario.html', {'form': form})





# Registrar Usuário dentro da apaplicação
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            try:
                # Criação do usuário
                usuario = CustomUser(
                    username=form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=make_password(form.cleaned_data['senha']),
                    tipo_usuario=form.cleaned_data['tipo_usuario'],
                )
                usuario.save()
                messages.success(request, 'Usuário cadastrado com sucesso! Faça login para continuar.')
                return redirect('login')  # Redirecionar para a página de login
            except Exception as e:
                messages.error(request, f'Erro ao cadastrar o usuário: {str(e)}')
        else:
            messages.error(request, 'Formulário inválido. Por favor, corrija os erros e tente novamente.')
    else:
        form = RegistroUsuarioForm()

    return render(request, 'usuarios/registrar.html', {'form': form})


# Na view de edição de perfil
@login_required
def editar_perfil(request):
    usuario = request.user
    
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            
            # Reautentica o usuário se a senha foi alterada
            if 'nova_senha' in form.cleaned_data and form.cleaned_data['nova_senha']:
                update_session_auth_hash(request, usuario)
            
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('home')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = EditarPerfilForm(instance=usuario)

    return render(request, 'usuarios/editar_perfil.html', {'form': form})







#Registrar Usuário na home
@login_required
def gerencia_usuarios(request):
    return render(request, 'usuarios/gerencia_usuarios.html')
























# View para logout
def logout_view(request):
    logout(request)  # Finaliza a sessão do usuário
    return redirect('login')  # Redireciona para a página de login


# Página protegida (apenas para usuários autenticados)
@login_required
def pagina_protegida(request):
    return render(request, 'usuarios/home.html')




@login_required
def listar_usuarios(request):
    """
    Lista todos os usuários cadastrados no sistema.
    """
    usuarios = CustomUser.objects.all()  # Busca todos os usuários do banco de dados
    return render(request, 'usuarios/listar_usuarios.html', {'usuarios': usuarios})
