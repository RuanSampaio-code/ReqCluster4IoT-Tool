from django import forms
from .models import Requisito, Projeto
from django.forms import inlineformset_factory

class RequisitoForm(forms.ModelForm):
    class Meta:
        model = Requisito
        fields = ['requisito', 'arquivo']  # Corrigido 'conteudo_texto' para 'requisito'
        widgets = {
            'requisito': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o requisito'}),
            'arquivo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'requisito': 'Nome do Requisito',
            'arquivo': 'Upload de Arquivo (.txt)',
        }

    def clean(self):
        cleaned_data = super().clean()
        requisito = cleaned_data.get('requisito')
        arquivo = cleaned_data.get('arquivo')

        if not requisito and not arquivo:
            raise forms.ValidationError("Você deve fornecer pelo menos um nome de requisito ou um arquivo.")

        return cleaned_data

# Criando o Formset para múltiplos requisitos dentro de um projeto
RequisitoFormSet = inlineformset_factory(
    Projeto,
    Requisito,
    form=RequisitoForm,
    fields=['requisito', 'arquivo'],  # Corrigido 'conteudo_texto' para 'nome'
    extra=1,
    
)