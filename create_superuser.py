import os
import django

# Configura o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Verifica se o superuser já existe
if not User.objects.filter(username='00000000000').exists():
    # Cria o superuser
    User.objects.create_superuser(
        username='00000000000',  # CPF como username
        email='erik@gmail.com',  # Email
        password='e1e2e3e4'      # Senha
    )
    print("Superuser criado com sucesso!")
else:
    print("Superuser já existe.")