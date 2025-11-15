from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Roupa
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
    return render(request, 'core/login_index.html')

def create_account_view(request):
    
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        email = request.POST.get('email').strip()
        senha = request.POST.get('password').strip()
        senha_confirm = request.POST.get('password_confirm').strip()
        erro = []
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) and senha == senha_confirm:
            if not re.search(r'[a-z]', senha): erro.append('deve conter ao menos uma letra minúscula')
            if not re.search(r'[A-Z]', senha): erro.append('deve conter ao menos um letra maiúscula')
            if not re.search(r'\d', senha): erro.append('deve conter ao menos um dígito')
            if len(senha) < 8: erro.append('deve conter no minimo 8 caracteres')
            if User.objects.filter(email=email).exists():
               erro.append('Já tem um user com esse email') 
            if not erro:
                user = User.objects.create_user(
                    email=email,
                    password=senha,
                    username=username
                ).save()
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, ', '.join(erro))
        elif senha != senha_confirm:
            messages.error(request, 'As senhas estão diferentes')
        else:
            messages.error(request, 'Email invalido')
    return render(request, 'core/create_account.html')

def home_view(request):
    return render(request, 'core/home.html', {'roupas': Roupa.objects.filter(is_promo=False), 'promo': Roupa.objects.filter(is_promo=True)})