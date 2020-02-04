# Projeto Atems

## Requisitos:
 * Python 3.8.x
 * Django 3.0.2

## Configurando o projeto:
### Crie um ambiente virtual na raiz do projeto:
#### Windows:
    python -m venv env
#### Distribuições Linux:
    python3.8 -m venv env

### Ative o ambiente virtual:
#### Windows:
    env\Scripts\activate
#### Distribuições Linux:
    source env/bin/activate

### Instale os requisitos do projeto:
    pip install -r requirements.txt

### Realize a migração dos scripts para o banco de dados:
#### Windows:
    python manage.py migrate
#### Distribuições Linux:
    python3.8 manage.py migrate

### Execute o projeto:
#### Windows:
    python manage.py runserver
#### Distribuições Linux:
    python3.8 manage.py runserver