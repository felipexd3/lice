"""
modulo models para herança das classes do modelo
"""
from django.db import models
class Receitas(models.Model):
    """
    Classe para registro receitas
    """
    RECEITAS_CHOICES = (
        ('H', 'Salário'),
        ('I', 'Investimentos'),
        ('J', 'Reajuste'),
        ('K', 'Outros')
    )

    descricao = models.CharField(u'Descrição', max_length=255)
    valor = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    categoria = models.CharField(u'Categoria', max_length=1, choices=RECEITAS_CHOICES)


class Despesas(models.Model):
    """
    Classe para registro despesas
    """
    DESPESAS_CHOICES = (
        ('A', 'Mercado'),
        ('B', 'Farmácia'),
        ('C', 'Alimentação'),
        ('D', 'Lazer'),
        ('E', 'Saúde'),
        ('F', 'Casa'),
        ('G', 'Educação'),
        ('L', 'Outros')
    )

    descricao = models.CharField(u'Descrição', max_length=255)
    valor = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    categoria = models.CharField(u'Categoria', max_length=1, choices=DESPESAS_CHOICES)
