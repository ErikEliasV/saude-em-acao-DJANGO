from django.urls import path
from saude_em_acao.views import index, tela_login, perfil, sobre_nos, exercicio_perna, exercicio_braco, exercicio_gluteos, exercicio_abdomen, tela_registro, tela_pergunta

urlpatterns = [
    path('', index, name='index'),
    path('login/', tela_login, name='tela_login'),
    path('registro/', tela_registro, name='tela_registro'),
    path('pergunta/', tela_pergunta, name='tela_pergunta'),
    path('perfil/', perfil, name='perfil'),
    path('sobre-nos/', sobre_nos, name='sobre_nos'),
    path('exercicios/perna/', exercicio_perna, name='exercicio_perna'),
    path('exercicios/braco/', exercicio_braco, name='exercicio_braco'),
    path('exercicios/gluteos/', exercicio_gluteos, name='exercicio_gluteos'),
    path('exercicios/abdomen/', exercicio_abdomen, name='exercicio_abdomen')
]
    

