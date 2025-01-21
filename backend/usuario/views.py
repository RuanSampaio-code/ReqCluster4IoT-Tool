""" from usuario.models import CustomUser
from usuario.serializers import UserSerializer
from rest_framework import viewsets """
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .serializers import UserSerializer
from django.http import JsonResponse
from rest_framework import viewsets

#Autenticação
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib import messages
from django.shortcuts import render, redirect



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Tentando autenticar o usuário com base no e-mail e senha
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            # Sucesso no login
            return JsonResponse({'message': 'Login successful', 'user': user.username})
        else:
            # Falha no login
            return JsonResponse({'error': 'Invalid username or password'}, status=400)
        


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmarSenha')

        # Verificar se as senhas coincidem
        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('cadastro')

        # Verificar se o username já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Já existe um usuário com este username.')
            return redirect('cadastro')

        # Verificar se o email já existe
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Já existe um usuário com este e-mail.')
            return redirect('cadastro')

        # Criar novo usuário e salva
        User.objects.create_user(username=username, email=email, password=senha)
        messages.success(request, 'Usuário cadastrado com sucesso! Faça login.')
        return redirect('login')


#Login


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(request, email=email, password=senha)

        if user:
            auth_login(request, user)  # Faz login do usuário
            messages.success(request, 'Login realizado com sucesso!')
            #return HttpResponse('Autheticado')
            return redirect('autenticando')  # Redirecione para a página inicial
        else:
            messages.error(request, 'E-mail ou senha inválidos.')
            return HttpResponse('email ou senha invalidos')
            #return redirect('login')


def autenticando(request):
    if request.user.is_authenticated:

        return render(request, 'home.html')
    return HttpResponse('voce precisa estar logado')

""" class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
 """
    
""" nova função de view apenas para teste """
def example_view(request):
    return JsonResponse({'message': 'Hello from Django!'})