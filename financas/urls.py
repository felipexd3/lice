"""
urls template
"""
from django.urls import path
from core import views
from . import views

app_name = 'financas'

urlpatterns = [
    path(r'nova-receita/', views.nova_receita, name='nova_receita'),
    path(r'nova-despesa/', views.nova_despesa, name='nova_despesa'),
    path(r'home/', views.home, name='home'),
]
