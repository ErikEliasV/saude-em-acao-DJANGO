from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('cpf', 'email', 'nome', 'sobrenome', 'is_staff', 'is_superuser')
    search_fields = ('cpf', 'email', 'nome', 'sobrenome')
    ordering = ('cpf',)

    fieldsets = (
        (None, {'fields': ('cpf', 'email', 'password')}),
        ('Informações Pessoais', {'fields': ('nome', 'sobrenome', 'altura', 'peso', 'genero', 'data_nascimento')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('cpf', 'email', 'password1', 'password2'),
        }),
    )

    filter_horizontal = ('groups', 'user_permissions')