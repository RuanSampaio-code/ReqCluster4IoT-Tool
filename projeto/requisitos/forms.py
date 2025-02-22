# requisitos/forms.py
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
RequisitoFormSet = formset_factory(RequisitoForm, extra=1)