from django.db import models
from django.contrib.auth.models import User

class Despesa(models.Model):
    nome_despesa = models.CharField(max_length=100)
    preco = models.FloatField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'despesas_fixas'