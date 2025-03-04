from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ValidationError


class CustomUserManager(BaseUserManager):
    def create_user(self, cpf, email=None, password=None, **extra_fields):
        if not cpf:
            raise ValueError('O CPF é obrigatório')
        email = self.normalize_email(email)  # Normaliza o email (opcional)
        user = self.model(cpf=cpf, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cpf, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(cpf, email, password, **extra_fields)

    def authenticate(self, request, cpf_or_email=None, password=None):
        # Tenta autenticar com CPF
        user = self.filter(cpf=cpf_or_email).first()
        if user is None:
            # Se não encontrar com CPF, tenta autenticar com Email
            user = self.filter(email=cpf_or_email).first()

        if user and user.check_password(password):
            return user
        return None

class CustomUser(AbstractBaseUser, PermissionsMixin):
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)  # Opcional
    nome = models.CharField(max_length=100, null=True, blank=True)  # Opcional
    sobrenome = models.CharField(max_length=100, null=True, blank=True)  # Opcional
    altura = models.FloatField(null=True, blank=True)  # Opcional
    peso = models.FloatField(null=True, blank=True)  # Opcional
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('NB', 'Não Binário'),
        ('O', 'Outro'),
        ('PNI', 'Prefiro não informar'),
    ]
    genero = models.CharField(max_length=3, choices=GENERO_CHOICES, null=True, blank=True)  # Opcional
    data_nascimento = models.DateField(null=True, blank=True)  # Opcional
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)  # Adicione este campo

    objects = CustomUserManager()

    USERNAME_FIELD = 'cpf'  # O campo usado para login (CPF)
    REQUIRED_FIELDS = ['email']  # O campo email é obrigatório para criar um superusuário

    def __str__(self):
        return self.cpf

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser