from rest_framework.exceptions import APIException

class ProdutoNotFound(APIException):
    status_code = 404
    default_detail = "Produto não encontrado."
    default_code = "produto_not_found"