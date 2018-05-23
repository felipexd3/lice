from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path(r'registro/', views.add_user, name='add_user'),
]