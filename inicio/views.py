from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from rest_framework import viewsets
from .serializer import *
from .models import *
import requests


def buscar_cep(request):
    if request.method == 'POST':
        cep_model = Cep()
        cep_model.cep = request.POST['cep']

        if not len(str(cep_model.cep)) == 8 and (cep_model.cep.isnumeric()):
            return HttpResponse('Digite um CEP válido')

        requisicao = requests.get(f'https://brasilapi.com.br/api/cep/v1/{cep_model.cep}')

        if requisicao.status_code == 404:
            messages.error(request, 'CEP não encontrado')
            return redirect('/')

        if Cep.objects.filter(cep=cep_model.cep):
            return render(request, 'index.html', {'resultado': Cep.objects.filter(cep=cep_model.cep)})

        queryset = requisicao.json()
        cep_model.state = queryset['state']
        cep_model.city = queryset['city']
        cep_model.neighborhood = queryset['neighborhood']
        cep_model.street = queryset['street']
        cep_model.service = queryset['service']
        cep_model.save()

        return render(request, 'index.html', {'resultado': Cep.objects.filter(cep=cep_model.cep)})

    return render(request, 'index.html')


def historico(request):
    if request.method == 'GET':
        return render(request, 'historico.html', {'historico_cep': Cep.objects.all()})

    return render(request, 'historico.html')


class CepViewSet(viewsets.ModelViewSet):
    queryset = Cep.objects.all()
    serializer_class = CepSerializer
