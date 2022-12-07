from django.db import models
from django.contrib.auth.models import User

class Despesa(models.Model):
    nome_despesa = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits = 10, decimal_places = 2, blank=True, default = 0)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        db_table = 'despesas_fixas'

    def get_soma_despesas(self):
        soma = 0
        for x in self.preco:
            soma += x
        return soma