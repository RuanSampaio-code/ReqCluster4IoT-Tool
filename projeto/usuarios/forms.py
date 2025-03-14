from django import forms
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser

class RegistroUsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, label="Senha")
    confirmar_senha = forms.CharField(widget=forms.PasswordInput, label="Confirmar Senha")


    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'tipo_usuario']  # Removi 'senha' daqui

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_usuario'].required = False  # Torna o campo opcional no formulário

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        if senha and confirmar_senha and senha != confirmar_senha:
            raise forms.ValidationError("As senhas não coincidem.")
        
        # Define 'normal' como padrão se o campo estiver vazio
        if not cleaned_data.get('tipo_usuario'):
            cleaned_data['tipo_usuario'] = 'normal'
        
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["senha"])  # Correção importante aqui
        if commit:
            user.save()
        return user


class EditarPerfilForm(forms.ModelForm):
    nova_senha = forms.CharField(
        label="Nova Senha",
        required=False,
        widget=forms.PasswordInput,
        help_text="Deixe em branco para manter a senha atual"
    )
    confirmar_senha = forms.CharField(
        label="Confirmar Nova Senha",
        required=False,
        widget=forms.PasswordInput
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'tipo_usuario']  # ADICIONE O CAMPO AQUI]

    def clean(self):
        cleaned_data = super().clean()
        nova_senha = cleaned_data.get("nova_senha")
        confirmar_senha = cleaned_data.get("confirmar_senha")

        if nova_senha or confirmar_senha:
            if nova_senha != confirmar_senha:
                self.add_error('confirmar_senha', "As senhas não coincidem")
            
            # Valida a força da senha
            try:
                validate_password(nova_senha, self.instance)
            except forms.ValidationError as error:
                self.add_error('nova_senha', error)

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data['email']
        if CustomUser.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError("Este e-mail já está em uso!")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        nova_senha = self.cleaned_data.get('nova_senha')
        
        if nova_senha:
            user.set_password(nova_senha)
        
        if commit:
            user.save()
        return user