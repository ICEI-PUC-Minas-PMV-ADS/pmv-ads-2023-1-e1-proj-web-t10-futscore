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

def CDB(request, stage):
    stages = [
        ('Primeira Fase', 'https://api.api-futebol.com.br/v1/campeonatos/2/fases/310'),
        # ... other stages ...
    ]
    primeiraFase = 77461971
    segundaFase = 77461970
    terceiraFase = 77461969
    oitavas = 77461968
    quartas = 77461967
    semi = 77461966
    final = 77461965


    # Determine which stage we're at
    current_stage = stages[stage]

    # Fetch data from API
    headers = {'Authorization': 'Bearer live_f90ee7baae2db53750a917df263bf7'}
    response = requests.get(current_stage[1], headers=headers)
    data = response.json()

    # Pass data to template
    context = {
        'matches': data['chaves'],
        'stage_name': current_stage[0],
        'stage_index': stage,
        'total_stages': len(stages),
    }
    return render(request, 'games.html', context)