from django.shortcuts import redirect, render
from app.models import Despesa

def lista_despesas(request):
    despesa = Despesa.objects.all()
    response = {'despesas': despesa}
    return render(request, 'despesas.html', response)

def nova_despesa(request):
    id_despesa = request.GET.get('id')
    dados = {}
    if id_despesa:
        dados['despesa'] = Despesa.objects.get(id=id_despesa)
    return render(request, 'nova_despesa.html', dados)

def submit_despesa(request):
    if request.POST:
        nome_despesa = request.POST.get('nome_despesa')
        preco = request.POST.get('preco')
        usuario = request.user
        id_despesa = request.POST.get('id_despesa')
        if id_despesa:
            Despesa.objects.filter(id = id_despesa).update(nome_despesa = nome_despesa,
                                                       preco = preco)
        else: 
            Despesa.objects.create(nome_despesa = nome_despesa,
                                   preco = preco,
                                   usuario = usuario)
    return redirect('/')

def delete_despesa(request, id_despesa):
    usuario = request.user
    despesa = Despesa.objects.get(id = id_despesa)
    if usuario == despesa.usuario:
        despesa.delete()
    return redirect('/')