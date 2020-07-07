from rest_framework import serializers
from .models import Produtos, Usuarios

class ProdutosSerializer(serializers.ModelSerializer):

    class Meta:

        model = Produtos
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):

    class Meta:

        model = Usuarios
        fields = '__all__'