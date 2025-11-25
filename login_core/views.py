from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .utils import verify_password
import re
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('user').strip()
        senha = request.POST.get('password').strip()
        try:
            try:
                usuario = User.objects.get(email=username)
            except User.DoesNotExist:
                usuario = User.objects.get(username=username)
            user = authenticate(request, username=usuario.username, password=senha)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Senha incorreta')
        except User.DoesNotExist:
            messages.error(request, 'Usuario invalido!')
    return render(request, 'login_core/login_index.html')

def create_account_view(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        email = request.POST.get('email').strip()
        senha = request.POST.get('password').strip()
        senha_confirm = request.POST.get('password_confirm').strip()
        erro = verify_password(senha, senha_confirm, email)
        if not erro:
            user = User.objects.create_user(
                email=email,
                password=senha,
                username=username
            )
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, ', '.join(erro))
    return render(request, 'login_core/create_account.html')
