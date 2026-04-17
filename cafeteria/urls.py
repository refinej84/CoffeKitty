from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('cardapio/', cardapio, name='cardapio'),
    path('informacoes/', informacoes, name='informacoes'),
    path('lista/', lista, name='lista'),
    path('add/<int:id>/', add_lista, name='add_lista'),
    path('logout/', sair, name='logout'),
    path('remover/<int:id>/', remover_lista, name='remover_lista'),
]