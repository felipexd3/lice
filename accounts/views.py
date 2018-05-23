from django.shortcuts import render, redirect
from .forms import UserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            u = form.save()
            u.set_password(u.password)
            u.save()
            return HttpResponse('Usuario Cadastrado!')
    else:
        form = UserForm()
    return render(request, 'auth/registro.html', {'form': form})
    