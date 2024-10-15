from .models import Produto
from .serializers import ProdutoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .exceptions import ProdutoNotFound
from rest_framework import status

class ProdutoList(APIView):
    def get(self, request):
        produtos = Produto.objects.all()
        if not produtos.exists():
            raise ProdutoNotFound() 
        
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
