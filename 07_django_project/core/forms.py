from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Asset


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['name','price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например, Bitcoin'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Например, 50000'}),
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'