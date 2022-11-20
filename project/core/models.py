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
