import requests
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def serieA(request):
    token = "81P4bUPg7JOqgRWpxyfqxELvW19jORE05eEx18FKm6BFcugyppGjqGdq68Gc"
    endpoint = 'https://api.sportmonks.com/v3/football/standings/live/leagues/648?include=participant;details'

    headers = {
        'Authorization': token,
    }

    response1 = requests.get(endpoint, headers=headers).json()

    data = response1['data']

    return render(request, 'tabelaSerieA.html', {'data': data})

def serieB(request):
    token = "81P4bUPg7JOqgRWpxyfqxELvW19jORE05eEx18FKm6BFcugyppGjqGdq68Gc"
    endpoint = 'https://api.sportmonks.com/v3/football/standings/live/leagues/651?include=participant;details'

    headers = {
        'Authorization': token,
    }

    response1 = requests.get(endpoint, headers=headers).json()

    data = response1['data']

    return render(request, 'tabelaSerieB.html', {'data': data})

def CDB(request, fase):
    fases = [
        ('0', '0'),
        ('primeira-fase', 'https://api.api-futebol.com.br/v1/campeonatos/2/fases/310'),
        ('segunda-fase', 'https://api.api-futebol.com.br/v1/campeonatos/2/fases/311'),
        ('terceira-fase', 'https://api.api-futebol.com.br/v1/campeonatos/2/fases/312'),
        ('oitavas', 'https://api.api-futebol.com.br/v1/campeonatos/2/fases/313'),
        ('semi', 'https://api.api-futebol.com.br/v1/campeonatos/2/fases/314'),
        ('quartas', 'https://api.api-futebol.com.br/v1/campeonatos/2/fases/315'),
        ('final', 'https://api.api-futebol.com.br/v1/campeonatos/2/fases/316'),
    ]

    # Determine which stage we're at
    fase_atual = fases[fase]

    # Fetch data from API
    headers = {'Authorization': 'Bearer live_f90ee7baae2db53750a917df263bf7'}
    response = requests.get(fase_atual[1], headers=headers)
    data = response.json()

    # Pass data to template
    context = {
        'partidas': data['chaves'],
        'fase': fase_atual[0],
        'faseAtual': fase,
        'faseAnterior': fase - 1,
        'fasePosterior': fase + 1,
        'fasesTotais': len(fases),
        'fase_nome': data['nome'],
    }
    return render(request, 'tabelaCDB.html', context)