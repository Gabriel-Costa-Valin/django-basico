from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

# Create your views here.

def ver_produto(request):
    if request.method == 'GET':
        nome = 'Gabriel'
        return render(request, 'ver_produto.html', {'nome': nome})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('age')

        #pessoas = Pessoa.objects.all()
        #pessoas = Pessoa.objects.filter(nome=nome)
        #pessoas.exists()
        pessoa = Pessoa(nome=nome, idade=idade)
        pessoa.save()
        
        return HttpResponse('Dados enviados com sucesso!')


def inserir_produto(request):
    return HttpResponse('Estou no inserir!')