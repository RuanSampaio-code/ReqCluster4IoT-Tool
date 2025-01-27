from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import RegistroUsuarioForm
from .models import CustomUser

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


#Tela de login
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password=password)  # Agora usa o backend customizado
        if user is not None:
            login(request, user)  # Autentica o usuário
            return redirect('protegida') # Redireciona para a página protegida
        else:
            return render(request, 'usuarios/login.html', {'error': 'Usuário ou senha inválidos'})

    return render(request, 'usuarios/login.html')



#Registrar Usuário
def registrar_usuario(request):
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
            return redirect('login')  # Redirecionar para a página de login
    else:
        form = RegistroUsuarioForm()

    return render(request, 'usuarios/registrar.html', {'form': form})


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
