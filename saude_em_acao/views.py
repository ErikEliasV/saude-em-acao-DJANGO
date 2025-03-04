from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'saude_em_acao/index.html')

def perfil(request):
    return render(request, 'saude_em_acao/perfil.html')

def sobre_nos(request):
    return render(request, 'saude_em_acao/tela-sobre-nós.html')

def exercicio_perna(request):
    return render(request, 'saude_em_acao/telas_exercicios/tela_exercicio_perna.html')

def exercicio_braco(request):
    return render(request, 'saude_em_acao/telas_exercicios/tela_exercicio_braço.html')

def exercicio_gluteos(request):
    return render(request, 'saude_em_acao/telas_exercicios/tela_exercicio_gluteos.html')

def exercicio_abdomen(request):
    return render(request, 'saude_em_acao/telas_exercicios/tela_exercicio_abdomen.html')