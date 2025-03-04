from .models import CustomUser

class CustomUserBackend:
    def authenticate(self, request, cpf_or_email=None, password=None):
        # Tenta autenticar com CPF
        user = CustomUser.objects.filter(cpf=cpf_or_email).first()
        if user is None:
            # Se não encontrar com CPF, tenta autenticar com Email
            user = CustomUser.objects.filter(email=cpf_or_email).first()

        if user and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None