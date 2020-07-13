import json
import requests
from requests import Request, Session


def inserindo_users():
    with open('tools/users.json', 'r') as users_file:
        dados = json.load(users_file)

    for i in dados:
        requests.post('http://127.0.0.1:8000/users/crud', data=i)

    print ('Dados de usuários inseridos com sucesso')

def inserindo_products():
    with open('tools/products.json', 'r') as products_file:
        dados = json.load(products_file)

    for i in dados:
        requests.post('http://127.0.0.1:8000/products/crud', data=i).json()

    print ('Dados de produtos inseridos com sucesso')
    
if __name__ == "__main__":
    inserindo_users()
    inserindo_products()