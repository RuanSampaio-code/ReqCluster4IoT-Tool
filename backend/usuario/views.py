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




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer





def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:

        username = request.POST.get('username')
        email = request.POST.get('email')
        senha =  request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('ja existe usuario com este username')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save
        

        return HttpResponse("usuario cadastrado com sucesso")



def login(request):

    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        print(email)
        print(senha)
       

        user = authenticate(email=email, password=senha)
        print(user)

        if user:
            auth_login(request, user)
            return HttpResponse('Autheticado')
        else:
            return HttpResponse('email ou senha invalidos')


@login_required
def home(request):
    if request.user.is_authenticated:

        return HttpResponse('home')
    return HttpResponse('voce precisa estar logado')

""" class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
 """
    
""" nova função de view apenas para teste """
def example_view(request):
    return JsonResponse({'message': 'Hello from Django!'})