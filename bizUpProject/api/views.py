from .models import Produto, User, Venda, MEI
from .serializers import ProdutoSerializer, UserSerializer, MeiSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .exceptions import ProdutoNotFound, UserNotFound
from rest_framework import status
from .validators import validate_data

class ProdutoList(APIView):
    def get(self, request, pk=None):
        if pk:
            produto = Produto.objects.filter(pk=pk).first()
            serializer = ProdutoSerializer(produto, partial = True)
            if not produto.exists():
                return Response({"error": "Produto não encontrado."}, status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            produtos = Produto.objects.all()
            serializer = ProdutoSerializer(produtos, many=True)
            if not produtos.exists():
                return Response({"error": "Nenhum produto encontrado."}, status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ProdutoSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def patch(self, request, pk):
        produto = Produto.objects.filter(pk=pk).first()
        if produto is None:
            return Response({"error": "Produto não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProdutoSerializer(produto, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Produto atualizado com sucesso!!', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        produto = Produto.objects.filter(pk=pk).first()
        if produto is None:
            return Response({"error": "Produto não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        produto.delete()
        return Response({'msg': 'Produto removido com sucesso!!'}, status=status.HTTP_204_NO_CONTENT)

class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        if not users.exists():
            return Response({'msg': 'Produto não encontrado!!'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        errors = validate_data(request.data)
        if errors:
            return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        usuario = User.objects.filter(pk=pk).first()
        if usuario is None:
            return Response({"error": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(usuario, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Usuário atualizado com sucesso!!', 'data': serializer.data}, status=status.HTTP_200_OK)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class MEIView(APIView):
    def get(self, request, pk=None):
        if pk:
            mei = MEI.objects.filter(pk=pk).first()
            serializer = MeiSerializer(mei, partial = True)
            if not mei.exists():
                return Response({"error": "MEI não encontrado."}, status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            mei = MEI.objects.all()
            serializer = MeiSerializer(mei, many=True)
            if not mei.exists():
                return Response({"error": "Nenhum MEI encontrado."}, status=status.HTTP_404_NOT_FOUND)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        errors = validate_data(request.data)
        if errors:
            return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)
        serializer = MeiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        mei = MEI.objects.filter(pk=pk).first()
        if mei is None:
            return Response({"error": "MEI não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        serializer = MeiSerializer(mei, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'MEI atualizado com sucesso!!', 'data': serializer.data}, status=status.HTTP_200_OK)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
