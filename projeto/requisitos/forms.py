
from django import forms
from django.forms import formset_factory, BaseFormSet

class RequisitoForm(forms.Form):
    requisito = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Digite o requisito',

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