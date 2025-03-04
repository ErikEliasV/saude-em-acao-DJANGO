from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login  
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages

User = get_user_model()

def custom_logout(request):
    logout(request)
    return redirect('index')

def registro(request):
    if request.method == 'POST':
        cpf = request.POST.get('cpf', '').replace('.', '').replace('-', '')  
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(cpf=cpf).exists():
            return render(request, 'usuario/tela-registro.html', {'error': 'Este CPF já está em uso.'})

        if User.objects.filter(email=email).exists():
            return render(request, 'usuario/tela-registro.html', {'error': 'Este email já está em uso.'})

        if not cpf.isdigit() or len(cpf) != 11:
            return render(request, 'usuario/tela-registro.html', {'error': 'CPF inválido. Deve conter 11 dígitos numéricos.'})

        if password1 != password2:
            return render(request, 'usuario/tela-registro.html', {'error': 'As senhas não coincidem.'})


        user = User.objects.create(
            cpf=cpf,  
            email=email,
            password=make_password(password1)
        )


        user = authenticate(request, cpf=cpf, password=password1)
        if user is not None:
            login(request, user) 
            return redirect('usuario:tela_pergunta')
        else:
            return render(request, 'usuario/tela-registro.html', {'error': 'Falha ao autenticar o usuário.'})
    
    return render(request, 'usuario/tela-registro.html')

def tela_pergunta(request):
    if request.method == 'POST':
        user = request.user 
        user.nome = request.POST.get('nome').title()
        user.sobrenome = request.POST.get('sobrenome').title()
        user.altura = request.POST.get('altura')
        user.peso = request.POST.get('peso')
        user.genero = request.POST.get('genero')
        user.data_nascimento = request.POST.get('data_nascimento')
        user.save()
        return redirect('index')  
    return render(request, 'usuario/tela-pergunta.html')

def tela_login(request):
    if request.method == 'POST':
        cpf_or_email = request.POST.get('cpf_or_email')
        password = request.POST.get('password')

        print(f"Tentando autenticar com CPF/Email: {cpf_or_email}")  # Depuração
        user = authenticate(request, cpf_or_email=cpf_or_email, password=password)

        if user is not None:
            print(f"Usuário autenticado: {user.cpf}")  # Depuração
            login(request, user)
            return redirect('index')
        else:
            print("Falha na autenticação")  # Depuração
            messages.error(request, 'CPF/Email ou senha incorretos.')
            return redirect('usuario:tela_login')

    return render(request, 'usuario/tela-login.html')

