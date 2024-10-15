from django.urls import path
from api.views import ProdutoList

urlpatterns = [
    path('produtos/', ProdutoList.as_view(), name='produto-list'),
]