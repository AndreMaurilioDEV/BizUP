from django.db import models

class Endereco_User(models.Model):
  id_endereco_user = models.AutoField(primary_key=True)
  cep = models.CharField(max_length=10)
  uf = models.CharField(max_length=2)
  cidade = models.CharField(max_length=45)
  rua = models.CharField(max_length=45)
  numero = models.CharField(max_length=10)
  referencia = models.CharField(
    max_length=255, 
    null=True, 
    blank=True
  )

class User(models.Model):
  id_user = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=45, blank=False)
  email = models.EmailField(max_length=45, unique=True, blank=False)
  cpf = models.CharField(max_length=11, unique=True, blank=False)
  telefone = models.CharField(max_length=15, blank=False)
  id_endereco_user = models.ForeignKey(
    Endereco_User,
    on_delete=models.CASCADE,
    related_name='usuarios'
  )

class Endereco_MEI(models.Model):
  id_endereco_mei = models.AutoField(primary_key=True)
  cep = models.CharField(max_length=10)
  uf = models.CharField(max_length=2)
  cidade = models.CharField(max_length=45)
  rua = models.CharField(max_length=45)
  numero = models.CharField(max_length=10)
  referencia = models.CharField(
    max_length=255, 
    null=True, 
    blank=True
  )

class MEI(models.Model):
  id_mei = models.AutoField(primary_key=True)
  email = models.EmailField(max_length=45, unique=True)
  nome = models.CharField(max_length=45)
  cnpj = models.CharField(unique=True, max_length=14)
  telefone= models.CharField(max_length=15)  
  id_endereco_mei = models.ForeignKey(
    Endereco_MEI,
    on_delete=models.CASCADE,
    related_name='meis'
  )

class Fidelidade(models.Model):
  id_fidelidade = models.AutoField(primary_key=True)
  qtd = models.IntegerField()
  descontos = models.FloatField()
  id_mei = models.ForeignKey(
    MEI,
    on_delete=models.CASCADE,
    related_name='fidelidades'
  )
  id_user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='fidelidades'
  )

class Venda(models.Model):
  id_venda = models.AutoField(primary_key=True)
  valor_final = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
  cupom_fiscal = models.CharField(max_length=45, blank=False)
  entrega = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
  desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, blank=True)

class Agendamento(models.Model):
  id_venda = models.ForeignKey(
    Venda,
    on_delete=models.CASCADE,
    related_name='agendamentos'
  )
  id_user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='agendamentos'
  )
  id_mei = models.ForeignKey(
    MEI,
    on_delete=models.CASCADE,
    related_name='agendamentos'
  )
  data_encomenda = models.DateTimeField(auto_now_add=True)
  data_entrega = models.DateTimeField()
  qtd = models.IntegerField()
  valor_total = models.DecimalField(max_digits=10, decimal_places=2)


class Entregador(models.Model):
  cpf_entregador = models.CharField(
    max_length=11, 
    unique=True, 
    primary_key=True
  )
  nome = models.CharField(max_length=45)
  telefone = models.CharField(max_length=15)
  tipo_entrega = models.CharField(max_length=45)

class Venda_Realizada(models.Model):
  entregador = models.ForeignKey(
    Entregador,
    on_delete=models.CASCADE,
    related_name='vendas_realizadas'
  )
  id_venda = models.ForeignKey(
    Venda,
    on_delete=models.CASCADE,
    related_name='vendas_realizadas'
  )
  id_endereco_user = models.ForeignKey(
    Endereco_User,
    on_delete=models.CASCADE,
    related_name='vendas_realizadas'
  )

class Produto(models.Model):
  id_produto = models.AutoField(primary_key=True)
  tipo = models.CharField(max_length=45, blank=False)
  desconto = models.BooleanField(default=False, blank=True)
  valor = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
  nome = models.CharField(max_length=45, blank=False)
  desconto_produto = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, blank=True)

class Item_Produto_Venda(models.Model):
  id_mei = models.ForeignKey(
    MEI,
    on_delete=models.CASCADE,
    related_name='itens_produtos_vendas'
)
  id_produto = models.ForeignKey(
    Produto,
    on_delete=models.CASCADE,
    related_name='itens_produtos_vendas'    
)
  id_venda = models.ForeignKey(
    Venda,
    on_delete=models.CASCADE,
    related_name='itens_produtos_vendas'    
)
  qtd = models.IntegerField()
  valor = models.DecimalField(max_digits=10, decimal_places=2)
  
    




