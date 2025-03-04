from django.urls import path
from saude_em_acao.views import index, perfil, sobre_nos, exercicio_perna, exercicio_braco, exercicio_gluteos, exercicio_abdomen

urlpatterns = [
    path('', index, name='index'),
    path('perfil/', perfil, name='perfil'),
    path('sobre-nos/', sobre_nos, name='sobre_nos'),
    path('exercicios/perna/', exercicio_perna, name='exercicio_perna'),
    path('exercicios/braco/', exercicio_braco, name='exercicio_braco'),
    path('exercicios/gluteos/', exercicio_gluteos, name='exercicio_gluteos'),
    path('exercicios/abdomen/', exercicio_abdomen, name='exercicio_abdomen')
]
    

