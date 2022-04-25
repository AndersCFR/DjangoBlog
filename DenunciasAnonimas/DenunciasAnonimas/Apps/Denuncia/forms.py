from django import forms
from .models import Denuncia
from django.contrib.auth.hashers import (PBKDF2PasswordHasher, SHA1PasswordHasher,)


class FormDenuncia(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ('titulo', 'tema', 'codigo', 'acusado', 'mensaje')
    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        print(hash(codigo))
        if len(codigo) != 9:
            raise forms.ValidationError('El código único debe ser de 9 dígitos')
        else:
            codigo = '145689785' # hash
        return codigo

    def clean_acusado(self):
        pass


