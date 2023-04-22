# Arquitetura da Solução

O software do FutScore será estruturado em três componentes principais: HTML, CSS e JavaScript. Para fornecer os dados dos jogos, vamos utilizar uma API de futebol. A aplicação será hospedada no Heroku e os dados do usuário serão armazenados em Local Storage. Essa arquitetura permitirá que o site seja rápido, escalável e fácil de manter.

## Diagrama de componentes

Os componentes que fazem parte da solução são apresentados na imagem abaixo.

![Diagrama de Componentes](img/diagrama_de_componentes.png)
### Arquitetura da Solução

A solução implementada conta com os seguintes módulos:
- **Navegador** - Interface básica do sistema  
  - **Páginas Web** - Conjunto de arquivos HTML, CSS, JavaScript e imagens que implementam as funcionalidades do sistema.
   - **Local Storage** - armazenamento mantido no Navegador, onde são implementados bancos de dados baseados em JSON. São eles: 
     - **Credenciais** - Dados do usuário, como login e senha
     - **Time do coração** - Time que o usuário torce
 - **API de futebol** - API que será usada para ter acesso a todas as informações sobre os times e campeonatos.
 - **Hospedagem** - local na Internet onde as páginas são mantidas e acessadas pelo navegador. 

## Tecnologias Utilizadas

**Linguagens**: HTML, CSS, JavaScript.
**IDEs de desenvolvimento**: Visual Studio Code.
Hospedagem**: Heroku.
**Repositório**: GitHub.
**Versionamento**: Git.
**Logo e imagens**: Canva.
**Templates**: MarvelApp e Figma.

## Hospedagem

A hospedagem e o lançamento da plataforma vão ser realizadas utilizando o Heroku, um serviço em nuvem que facilita a implantação e gerenciamento de aplicações web.
