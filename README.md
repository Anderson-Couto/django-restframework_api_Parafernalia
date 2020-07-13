# API de Cadastro e Consultas
Projeto desenvolvido para a empresa Parafernália, com o intuito de construir um sistema Varejista que calcula descontos sobre produtos para usuários específicos.

## Requisitos
- [Python 3.8](https://www.python.org/ "Python 3.8")
- IDE ou Editor de Texto à sua escolha ([VS Code](https://code.visualstudio.com/ "VS Code"), [PyCharm](https://www.jetbrains.com/pt-br/pycharm/download/#section=windows "PyCharm"), entre outros)
- [Postman](https://www.postman.com/ "Postman") ou o próprio Navegador Web
- [Git](https://git-scm.com/ "Git")
- [PostgreSQL](https://www.postgresql.org/ "PostgreSQL")

## Instalação
Com os requisitos já disponíveis em sua máquinha, selecione uma pasta para receber os arquivos deste repositório. Então, realize o comando:

`git clone https://github.com/Anderson-Couto/django-restframework_api_Parafernalia.git`

Após esta etapa, crie um [ambiente virtual](https://www.treinaweb.com.br/blog/criando-ambientes-virtuais-para-projetos-python-com-o-virtualenv/ "ambiente virtual") para receber os pacotes. Com a sua virtualenv acessada, realize o comando no terminal:

`pip install -r requeriments.txt`

## Execução

### Banco de Dados

Em [settings.py](https://github.com/Anderson-Couto/django-restframework_api_Parafernalia/blob/master/varejo_api/settings.py "settings.py"), na pasta varejo_api, é necessário alterar as configurações DATABASES (linha 78) de acordo com a sua máquina.

### Iniciando o Servidor
Com a virtualenv ativa e os pacotes instalados, digite:

`python manage.py runserver`

**Obs**: Se necessário, execute os comandos:

`python manage.py makemigrations`

`python manage.py migrate`

