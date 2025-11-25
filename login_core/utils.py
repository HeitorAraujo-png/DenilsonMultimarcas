from django.contrib.auth.models import User
import re
def verify_password(psw1: str , psw2: str, email: str) -> bool | list:
    erro = []            
    if User.objects.filter(email=email).exists(): erro.append('Já tem um user com esse email') 
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email): erro.append('Email invalido')
    if psw1 != psw2: erro.append('As senhas devem ser iguais')
    if not re.search(r'[a-z]', psw1): erro.append('deve conter ao menos uma letra minúscula')
    if not re.search(r'[A-Z]', psw1): erro.append('deve conter ao menos um letra maiúscula')
    if not re.search(r'\d', psw1): erro.append('deve conter ao menos um dígito')
    if len(psw1) < 8: erro.append('deve conter no minimo 8 caracteres')
    return True if not erro else erro
