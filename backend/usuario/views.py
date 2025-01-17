from usuario.models import Usuario
from usuario.serializers import UsuarioSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from  django.contrib.auth import login as login_django
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response





from django.http import JsonResponse

""" Cadastro de usuarios """
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


""" Login de usuario """
def login(request):

    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = authenticate(email=email, password= senha)

        if user:
            login_django(request, user)
            return HttpResponse("Autheticado")
        else:
            return HttpResponse('email ou senha invalidos')




def home(request):
    if request.user.is_autentidatd:

        return HttpResponse('home')
    return HttpResponse('voce precisa estar logado')



class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

""" nova função de view apenas para teste """
def example_view(request):
    return JsonResponse({'message': 'Hello from Django!'})