from django.db import models


# Create your models here.
class MarcaCarro(models.Model):
    nome = models.CharField(max_length=24)

    def __str__(self):
        return self.nome


class Carro(models.Model):
    nome = models.CharField(max_length=24)
    marca = models.ForeignKey(MarcaCarro, on_delete=models.CASCADE)
    ano = models.IntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Item(models.Model):
    nome = models.CharField(max_length=24)
    preco = models.DecimalField(decimal_places=2, max_digits=9)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=64)
    email = models.EmailField()
    celular = models.CharField(max_length=12)
    cpf = models.CharField(max_length=12)

    def __str__(self):
        return self.nome


class OrdemServico(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    status_choices = [
        ('ATIVO', 'Ativo'),
        ('AG PGTO', 'Ag. Pgto'),
        ('CANCELADO', 'Cancelado'),
        ('FINALIZADO', 'Finalizado'),
        ('PAUSADO', 'Pausado'),
    ]
    status = models.CharField(max_length=10, choices=status_choices,
                              default='ATIVO')
    descricao = models.TextField()
    observacao = models.TextField()
    itens = models.ForeignKey(Item, on_delete=models.CASCADE)
    mao_obra = models.DecimalField(decimal_places=2, max_digits=9)
    ts_created = models.DateTimeField(auto_now_add=True)
    ts_updated = models.DateTimeField(auto_now=True)
