from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .forms import RegistroUsuarioForm
from .models import CustomUser

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistroUsuarioForm, EditarPerfilForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_POST


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


#tela sobr
def about(request):
    return render(request, 'usuarios/about.html')  # Nome do template em inglês

# Registrar novo Usuário 
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




#pagina de novo usuario na dentro da home
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
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('gerencia_usuarios')  # Redirecionar para a página de login
        else:
            messages.error(request, 'Formulário inválido. Por favor, corrija os erros e tente novamente.')
           
    else:
        form = RegistroUsuarioForm()

    return render(request, 'usuarios/novo_usuario.html', {'form': form})





#edição de perfil
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





#Lista usuarios na pagina de gerneciasr usuarios
@login_required
def gerencia_usuarios(request):
    usuarios = CustomUser.objects.all()
    return render(request, 'usuarios/gerencia_usuarios.html',{'usuarios':usuarios} )


#Editar usuario
@login_required
def editar_usuario(request, user_id):
    
    # Obtém o usuário a ser editado
    usuario = get_object_or_404(CustomUser, pk=user_id)
    
    # Verifica se o usuário atual é admin
    is_admin = request.user.tipo_usuario == 'admin'
    
    # --- Controle de Permissões ---
    # 1. Apenas admin pode editar outros usuários
    if not is_admin and usuario != request.user:
        raise PermissionDenied("Você não tem permissão para editar outros usuários")
    
    # 2. Impedir que não-admins editem admins
    if usuario.tipo_usuario == 'admin' and not is_admin:
        raise PermissionDenied("Apenas administradores podem editar outros administradores")
    
    # 3. Se for auto-edicao, permitir apenas campos específicos
    if usuario == request.user and not is_admin:
        form = EditarPerfilForm(instance=usuario, is_self_edit=True)
    else:
        form = EditarPerfilForm(request.POST or None, instance=usuario)
    
    # --- Lógica do Formulário ---
    if request.method == 'POST' and form.is_valid():
        # Validação extra para tipo de usuário
        if form.cleaned_data['tipo_usuario'] == 'admin' and not is_admin:
            raise PermissionDenied("Apenas administradores podem definir este perfil")
        
        form.save()
        messages.success(request, 'Alterações salvas com sucesso!')
        return redirect('gerencia_usuarios')
    
    # --- Ajuste de Campos ---
    if not is_admin:
        # Remove o campo tipo_usuario para não-admins
        form.fields.pop('tipo_usuario', None)
        
        # Se for auto-edicao, remove campos sensíveis
        if usuario == request.user:
            form.fields.pop('nova_senha', None)
            form.fields.pop('confirmar_senha', None)
    
    return render(request, 'usuarios/editar_usuario.html', {
        'form': form,
        'usuario': usuario,
        'is_admin': is_admin
    })


@require_POST
@login_required
def deletar_usuario(request, user_id):
    usuario = get_object_or_404(CustomUser, pk=user_id)
    
    # Verifica se o usuário atual é admin
    is_admin = request.user.tipo_usuario == 'admin'
    
    # --- Controle de Permissões ---
    # 1. Apenas admin pode deletar outros usuários
    if not is_admin and usuario != request.user:
        raise PermissionDenied("Você não tem permissão para deletar outros usuários")
    
    # 2. Impedir que não-admins deletem admins
    if usuario.tipo_usuario == 'admin' and not is_admin:
        raise PermissionDenied("Apenas administradores podem deletar outros administradores")
    
    # 3. Se for auto-deleção, permitir apenas para não-admins
    if usuario == request.user and not is_admin:
        raise PermissionDenied("Você não pode deletar sua própria conta")
    
    # --- Lógica da Deleção ---
    try:
        usuario.delete()
        messages.success(request, "Usuário excluído com sucesso!")
        if usuario == request.user:
            logout(request)
            return redirect('login')
    except Exception as e:
        messages.error(request, f"Erro ao excluir usuário: {str(e)}")
    
    return redirect('gerencia_usuarios')


# View para logout
def logout_view(request):
    logout(request)  # Finaliza a sessão do usuário
    return redirect('login')  # Redireciona para a página de login


# Página protegida (apenas para usuários autenticados)
@login_required
def pagina_protegida(request):
    return render(request, 'usuarios/home.html')

