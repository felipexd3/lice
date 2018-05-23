"""
views core
"""
from django.shortcuts import render

def home(request):
    """
    renderizacao index
    """
    return render(request, 'base.html')
