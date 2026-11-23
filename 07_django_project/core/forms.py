from django import forms
from .models import Asset


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name','price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например, Bitcoin'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Например, 50000'}),
        }