# Instruções de utilização

## Pré-requisitos

* Python 3.6 ou superior instalado.
* Acesso ao terminal/linha de comando.

## Instalação

Primeiramente, clone o repositório no seu local desejado através do terminal utilizando o comando:

```
git clone https://github.com/ICEI-PUC-Minas-PMV-ADS/pmv-ads-2023-1-e1-proj-web-t10-futscore.git
```

Após clonar o repositório, navegue até o diretório do projeto:

```
cd pmv-ads-2023-1-e1-proj-web-t10-futscore
```

Recomendamos a criação de um ambiente virtual para instalar as dependências do projeto. Você pode criar um utilizando o seguinte comando:

```
python -m venv venv
```

Ative o ambiente virtual. No Windows:

```
venv\Scripts\activate
```

No Unix ou MacOS:

```
source venv/bin/activate
```

Com o ambiente virtual ativo, instale as dependências do projeto utilizando o arquivo requirements.txt:

```
pip install -r requirements.txt
```

## Executando o projeto

Com as dependências instaladas, agora você pode rodar o servidor. Execute o seguinte comando no terminal:

```
python manage.py runserver
```

Agora o site deve estar rodando em localhost:8000 ou 127.0.0.1:8000 no seu navegador.