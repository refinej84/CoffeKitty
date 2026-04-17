from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect

def sair(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    categorias = Categoria.objects.all()
    return render(request, 'home.html', {'categorias': categorias})

@login_required
def cardapio(request):
    produtos = Produto.objects.all()
    categorias = Categoria.objects.all()

    categoria_id = request.GET.get('categoria')

    if categoria_id:
        produtos = produtos.filter(categoria_id=categoria_id)

    return render(request, 'cardapio.html', {
        'produtos': produtos,
        'categorias': categorias
    })

@login_required
def informacoes(request):
    return render(request, 'informacoes.html')


@login_required
def lista(request):
    itens = ListaDesejos.objects.filter(usuario=request.user)
    return render(request, 'lista.html', {'itens': itens})


@login_required
def add_lista(request, id):
    produto = Produto.objects.get(id=id)
    ListaDesejos.objects.create(usuario=request.user, produto=produto)
    return redirect('lista')

@login_required
def remover_lista(request, id):
    item = ListaDesejos.objects.get(id=id, usuario=request.user)
    item.delete()
    return redirect('lista')