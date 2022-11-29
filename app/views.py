from django.shortcuts import render

def lista_despesas(request):
    return render(request, 'despesas.html')
