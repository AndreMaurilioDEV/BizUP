from rest_framework import serializers
from .models import Produto, User, Venda, MEI

class ProdutoSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Produto
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'

class MeiSerializer(serializers.ModelSerializer):
    class Meta:
        model = MEI
        fields = '__all__'
    