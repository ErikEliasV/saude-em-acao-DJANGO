from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('pergunta/', views.tela_pergunta, name='tela_pergunta'),
    path('login/', views.tela_login, name='tela_login'), 
    path('logout/', views.custom_logout, name='logout'),
]