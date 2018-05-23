"""
módulos necessários para criação dos forms, receitas e depesas
"""
from django import forms
from .models import Receitas, Despesas

class ReceitasForm(forms.ModelForm):
    """
    classe que irá materializar o formulário de adição de receitas
    """
    class Meta:
        model = Receitas
        fields = '__all__'

class DespesasForm(forms.ModelForm):
    """
    classe que irá materializar o formulário de adição de despesas
    """
    class Meta:
        model = Despesas
        fields = '__all__'
