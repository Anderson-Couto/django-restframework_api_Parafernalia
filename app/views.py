from rest_framework.views import APIView
from .models import Produtos, Usuarios
from .serializers import ProdutosSerializer, UsuariosSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
import json
from datetime import date
import requests
from collections import OrderedDict


##--------------- Usuários ---------------##

class UsuariosList(APIView):  
    serializer_class = UsuariosSerializer

    def get(self, request, format=None):
        users = Usuarios.objects.all()
        serializer = UsuariosSerializer(users, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
class UsuariosC(APIView):
    serializer_class = UsuariosSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"messagem": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class UsuariosRUD(APIView):
    serializer_class = UsuariosSerializer
    
    def get(self, request, pk):
        users = Usuarios.objects.get(pk=pk)
        serializer = self.serializer_class(users)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        users = Usuarios.objects.get(pk=pk)
        serializer = self.serializer_class(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            users = Usuarios.objects.get(pk=pk)
            users.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as message:
            return Response(status=status.HTTP_404_NOT_FOUND)

##--------------- Produtos ---------------##

class ProdutosList(APIView):
    serializer_class = ProdutosSerializer

    def get(self, request, format=None):
        produtos = Produtos.objects.all()
        serializer = ProdutosSerializer(produtos, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class ProdutosC(APIView):
    serializer_class = ProdutosSerializer
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"messagem": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ProdutosRUD(APIView):
    serializer_class = ProdutosSerializer
    
    def get(self, request, pk):
        produtos = Produtos.objects.get(pk=pk)
        serializer = self.serializer_class(produtos)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        produtos = Produtos.objects.get(pk=pk)
        serializer = self.serializer_class(produtos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        try:
            produtos = Produtos.objects.get(pk=pk)
            produtos.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as message:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ProdutosDisc(APIView):
    serializer_class = ProdutosSerializer

    def get(self, request, pk, format=None):
        produtos = Produtos.objects.all()
        serializer = ProdutosSerializer(produtos, many=True)

        pkP_list = [i['id'] for i in serializer.data]

        r_list = []
        for pkP in pkP_list: 
            r = requests.get(f'http://localhost:3000/api/discounts/{pkP}/{pk}').json()
            produto = list(produtos.filter(pk=pkP).values())
            produto.append(r)
            produto_final = OrderedDict(produto[0], **produto[1])
            r_list.append(produto_final)

        return Response(data=r_list, status=status.HTTP_200_OK)
"""
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
"""


"""
##--------------- Descontos ---------------##
class DescontoCalc(APIView):

    def get(self, request, pkP, pkU):
        user = Usuarios.objects.get(pk=pkU)
        produto = Produtos.objects.get(pk=pkP)
        
        dt = desconto_total(pkP, pkU)

        data = {
            'total_discount': dt,
            'final_price': preco_descontado(pkP,dt)
        }

        return Response(data=data, status=status.HTTP_200_OK)

def desconto_birthday(pkU):
    user = Usuarios.objects.get(pk=pkU)
    hoje = date.today()
    
    desconto = 0.0
    if (hoje.day == user.birthdate.day) and (hoje.month == user.birthdate.month): desconto = 5.0

    return desconto

def desconto_BF():
    BLACK_FRIDAY = date(date.today().year, 7, 7)
    hoje = date.today()

    desconto = 0.0
    if (hoje.day == BLACK_FRIDAY.day) and (hoje.month == BLACK_FRIDAY.month): desconto = 10.0

    return desconto

def desconto_total(pkP, pkU):
    produto = Produtos.objects.get(pk=pkP)
    user = Usuarios.objects.get(pk=pkU)

    total = produto.base_discount_percent + desconto_birthday(pkU) + desconto_BF()
    if total > 25.0 : total = 25.0

    return total

def preco_descontado(pkP, discount):
    produto = Produtos.objects.get(pk=pkP)
    preco_total = produto.price

    return preco_total*(100 - discount)/100
"""