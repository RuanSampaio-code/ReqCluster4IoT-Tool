from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'arquivo_requisitos', 'requisitos_digitados']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 3}),
            'requisitos_digitados': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        }
        labels = {
            'arquivo_requisitos': 'Arquivo de Requisitos (opcional)',
            'requisitos_digitados': 'Requisitos Digitados (opcional)'
        }