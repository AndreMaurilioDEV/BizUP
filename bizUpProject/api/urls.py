from django.urls import path
from api.views import ProdutoList, UserView, MEIView

urlpatterns = [
    path('produtos/', ProdutoList.as_view(), name='produto-list'),
    path('produtos/<int:pk>/', ProdutoList.as_view(), name='produto-detail'),
    path('users/', UserView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserView.as_view(), name='user-detail'),
    path('meis/', MEIView.as_view(), name='meis-list'),
    path('meis/', MEIView.as_view(), name='meis-detail'),
]