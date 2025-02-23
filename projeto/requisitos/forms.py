""" # requisitos/forms.py
from django import forms
from .models import Requisito
from django.forms import formset_factory  # Troque inlineformset_factory por formset_factory


class RequisitoForm(forms.Form):  # Troque ModelForm por Form
    requisito = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o requisito'})
    )
    arquivo = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
    tipo = forms.ChoiceField(
        choices=Requisito.TIPO_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        requisito = cleaned_data.get('requisito')
        arquivo = cleaned_data.get('arquivo')

        if not requisito and not arquivo:
            raise forms.ValidationError("Forneça um requisito ou um arquivo.")

        return cleaned_data

# Troque o inlineformset_factory por um formset_factory comum
RequisitoFormSet = formset_factory(RequisitoForm, extra=1) """


# forms.py
""" from django import forms
from django.forms import BaseFormSet, formset_factory
from .models import Requisito

class RequisitoForm(forms.ModelForm):  
    class Meta:
        model = Requisito
        fields = ['requisito', 'tipo', 'arquivo']
        widgets = {
            'requisito': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Descrição detalhada do requisito'
            }),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'arquivo': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

class BaseRequisitoFormSet(BaseFormSet):
    def clean(self):
       
        if any(self.errors):
            return
            
        if not any(form.has_changed() for form in self.forms):
            raise forms.ValidationError("Pelo menos um requisito deve ser informado.")

RequisitoFormSet = formset_factory(
    RequisitoForm,
    formset=BaseRequisitoFormSet,
    extra=1,
    can_delete=True  
) """

# requisitos/forms.py
from django import forms
from django.forms import formset_factory, BaseFormSet

class RequisitoForm(forms.Form):
    requisito = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Digite o requisito'
        })
    )
    arquivo = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': '.txt'  # Aceitar apenas .txt
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        requisito = cleaned_data.get('requisito')
        arquivo = cleaned_data.get('arquivo')

        if not requisito and not arquivo:
            raise forms.ValidationError("Forneça um requisito ou um arquivo.")

        return cleaned_data

RequisitoFormSet = formset_factory(RequisitoForm, extra=1)