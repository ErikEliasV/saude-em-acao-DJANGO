from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['cpf', 'email', 'password1', 'password2', 'nome', 'sobrenome', 'altura', 'peso', 'genero', 'data_nascimento']