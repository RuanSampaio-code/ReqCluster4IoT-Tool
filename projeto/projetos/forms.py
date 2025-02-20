from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao']  # Removidos os campos de requisitos
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'nome': 'Nome do Projeto',
            'descricao': 'Descrição Detalhada'
        }