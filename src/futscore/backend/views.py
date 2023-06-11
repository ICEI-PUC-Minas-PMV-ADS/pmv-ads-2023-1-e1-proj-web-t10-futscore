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

def calendario(request):
    return render(request, 'calendario.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def recover(request):
    return render(request, 'recover.html')

def status(request):
    return render(request, 'status.html')

def profile(request):
    return render(request, 'profile.html')

def estatisticas(request, jogo):
    jogos = [
        ('Cruzeiro', '3 x 0', 'América-MG', 'Ao Vivo 88', 'Mineirão'),
        ('Corinthians', '2 x 1', 'Atlético-MG', 'Ao Vivo 88', 'Neo Química Arena'),
        ('Palmeiras', '1 x 1', 'Flamengo', 'Ao Vivo 23', 'Allianz Parque'),
        ('Fluminense', '1 x 0', 'Santos', 'Ao Vivo 23', 'Maracanã'),
    ]

    jogo_atual = jogos[jogo]

    context = {
        'time1': jogo_atual[0],
        'time2': jogo_atual[2],
        'placar': jogo_atual[1],
        'status': jogo_atual[3],
        'estadio': jogo_atual[4],
    }
    
    return render(request, 'estatisticas.html', context)

