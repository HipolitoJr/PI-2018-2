from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import re

from django.shortcuts import render

from buscas.forms import RegistrarBusca
from buscas.models import Resultado
from django.shortcuts import redirect
from django.views.generic.base import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime


def index(request):
    resultados = Resultado.objects.all().order_by('-id')

    return render(request, "index.html",
                  {"resultados": resultados, })


def search(request, keyword, url, deth, links_visitados):

    #Download da página e armazenamento dos links
    try:
        #print('\naguarde...')
        response = requests.get(url)
        links_visitados.append(url)
        html = BeautifulSoup(response.text, 'html.parser')
        links = html.find_all('a')
    except:
        #print("Link inválido: ", url)
        resultado = Resultado(url=url, resultado="Link inválido")
        resultado.save()
        return redirect('index')
        links = []

    #busca de ocorrencias da keyword na pagina
    if html.text.__contains__(keyword):
        pattern = re.compile('.{0,100} %s .{0,100}' % keyword.upper())
        result_ini = [m.start() for m in re.finditer(pattern, html.text.upper())]
        result_fim = [m.end() for m in re.finditer(pattern, html.text.upper())]
        for i in range(len(result_ini)):
            resultado = Resultado(url=url, resultado=html.text[result_ini[i] : result_fim[i]])
            resultado.save()

    #verificacao para recursividade
    if deth > 0:
        for link in links:
            try:
                if link['href'].startswith('http') and link['href'] not in links_visitados:
                    search(request, keyword, link['href'], deth - 1, links_visitados)
            except:
                pass

    return redirect('index')


def buscar(request, keyword, url, deth):

    links_visitados = []

    search(request, keyword, str(url), deth, links_visitados)

    resultados = Resultado.objects.all().order_by('-id')

    return render(request, "base.html",)


class RegistrarBuscaView(View):

    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        # perfil_logado = get_perfil_logado(request)
        # usuario_logado = User.objects.get(id=perfil_logado.id)

        resultados = Resultado.objects.all()
        for resultado in resultados:
            resultado.delete()

        form = RegistrarBusca(request.POST)

        dados = form.data

        buscar(request, dados['keyword'], dados['url'], int(dados['profundidade']))

        resultados = Resultado.objects.all().order_by('-id')

        return render(request, "base.html")