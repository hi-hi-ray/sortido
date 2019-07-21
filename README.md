# Sortido
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors)

O sortido foi desenvolvido para facilitar os sorteios online, permitindo que você realize os seus sorteios de forma rápida e sem complicações.

## Sobre o projeto

Somos um grupo de desenvolvimento que criamos um site para lhe ajudar a sortear.
Esse site é fruto do projeto de bloco Engenharia de software Escaláveis do Instituto Infnet, cujo tivemos como mentor o professor Aquino Botelho.

## Pré-requisitos

Para rodar o Python3 você precisa de uma maquina com sistema operacional windows ou linux.

#### Instalando o Python3 no windows

##### Adicionando o python no path
Para que você consiga rodar o python pela linha de comando é necessário adiciona-lo no path do sistema que pode ser feito seguindo os passos a seguir:

1. Abra o painel de controle e navegue até as configurações de sistema

2. Selecione as configurações avançadas do sistema

3. Clique em variáveis de ambiente

4. Procure nas variáveis do sistema pela variável **Path**

5. Clique em editar

6. Verifique se os valores **C:\Python34** e **C:\Python34\Scripts** existem no campo de valor da variável, caso não exista adicione ao final dos valores separando cada valor com **;**. O **Python34** neste exemplo é referente a pasta onde o python foi instalado no seu sistema, este valor pode ser diferente caso esteja instalando outra versão do python por exemplo se for a versão 2.7 o valor será **Python27**. Verifique o destino da sua instalação e substitua por este valor.

7. Clique em OK

##### Instalando o pip

Para que você consiga instalar os pacotes do python é necessário que você tenha o pip instalado no sistema. Este procedimento funciona com python 2.7.9 ou versões superiores e python 3.x.

Clique com o botão direito no ícone do windows e selecione executar:

Digite **cmd** e clique em ok:

Na linha de comando rode **_python -m ensurepip_**:

Se o comando retornar dizendo que os requisitos já estão satisfeitos rode **_python -m ensurepip --upgrade_**:

### Instalando o Python no Linux

Verifique se já tem o Python instalado, se você usa GNU/Linux, provavelmente já possui alguma versão do Python instalada por padrão. Para conferir, digite em um terminal:
**_$ which python3_**

que deve retornar algo como **_/usr/bin/python_**. Isso significa que o Python está instalado nesse endereço.

Caso contrário, se retornar algo como **_which: no python in (/usr/local/sbin:/usr/local/bin:/usr/bin:/usr...)_** você precisa instalar pelos repositórios ou gerenciador de pacotes de sua distribuição.

##### Instalação por Gerenciadores de Pacotes

Os gerenciadores de pacotes mais comuns são apt-get (Debian, Ubuntu) e yum (RedHat, CentOS). Caso sua distribuição utilize um gerenciador de pacotes diferente, acesse a página de downloads do Python https://www.python.org/downloads/.

###### apt-get

Para instalar o Python 3.5, digite em um terminal:

**_$ sudo apt-get install python3.5_**

#### Instalando requests

Instalar requests é simples usando pip:

**_$ pip install requests_**

#### Instalando Django

Para instalar o Django digite o comando abaixo:

**_pip install Django==2.1.7_**

## Como rodar o projeto

1. Com o Python instalado abra o terminal

2. Procure pela pasta do projeto digitando no terminal **_cd sortido/_**

3. Digite no cmd o comando **_python3 manage.py runserver_**

4. pegar o http gerado, entrar no navegador e rodar a aplicação.

## Build with

* Python - Linguagem usada no projeto.

* Django - Web framework utilizado conjunto de componentes que ajuda você a desenvolver sites de forma mais rápida e fácil.

* Request - Uma biblioteca HTTP para python usada em nosso projeto

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
<table>
  <tr>
    <td align="center"><a href="https://hi-hi-ray.github.io"><img src="https://avatars3.githubusercontent.com/u/13999149?v=4" width="100px;" alt="Raysa Dutra"/><br /><sub><b>Raysa Dutra</b></sub></a><br /><a href="https://github.com/hi-hi-ray/sortido/commits?author=hi-hi-ray" title="Code">💻</a> <a href="#projectManagement-hi-hi-ray" title="Project Management">📆</a> <a href="#talk-hi-hi-ray" title="Talks">📢</a> <a href="#business-hi-hi-ray" title="Business development">💼</a> <br /> <a href="#design-hi-hi-ray" title="Design">🎨</a> <a href="#review-hi-hi-ray" title="Reviewed Pull Requests">👀</a> <a href="#maintenance-hi-hi-ray" title="Maintenance">🚧</a> <a href="#ideas-hi-hi-ray" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/yurisouza"><img src="https://avatars0.githubusercontent.com/u/10949463?v=4" width="100px;" alt="Yuri Pereira"/><br /><sub><b>Yuri Pereira</b></sub></a><br /><a href="https://github.com/hi-hi-ray/sortido/commits?author=yurisouza" title="Code">💻</a> <a href="#talk-yurisouza" title="Talks">📢</a> <a href="https://github.com/hi-hi-ray/sortido/issues?q=author%3Ayurisouza" title="Bug reports">🐛</a></td>
    <td align="center"><a href="https://github.com/heriktedesco"><img src="https://avatars2.githubusercontent.com/u/15737700?v=4" width="100px;" alt="heriktedesco"/><br /><sub><b>heriktedesco</b></sub></a><br /><a href="https://github.com/hi-hi-ray/sortido/commits?author=heriktedesco" title="Code">💻</a> <a href="#business-heriktedesco" title="Business development">💼</a></td>
    <td align="center"><a href="https://github.com/pedroppbastos"><img src="https://avatars2.githubusercontent.com/u/33101241?v=4" width="100px;" alt="Pedro Paulo P Bastos"/><br /><sub><b>Pedro Paulo P Bastos</b></sub></a><br /><a href="#business-pedroppbastos" title="Business development">💼</a> <a href="https://github.com/hi-hi-ray/sortido/commits?author=pedroppbastos" title="Documentation">📖</a></td>
</tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:END -->
This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!