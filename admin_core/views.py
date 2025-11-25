from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from core.decorators import admin_required
from core.models import *
from django.db import transaction
from login_core.utils import verify_password
# Create your views here.
@admin_required
def admin_view(request):
    return render(request, 'admin_core/admin.html')


# Crud
sizes = ['PP', 'P', 'M', 'G', 'GG', 'XG', 'XXG']
@admin_required
def view_create_clothe(request):
    if request.method == 'POST':
        nome = request.POST.get('name')
        preco = float(request.POST.get('price'))
        img = request.FILES.get('img')
        unit = int(request.POST.get('unit'))
        marca = request.POST.get('marca')
        espec = request.POST.get('espec')
        texto = request.POST.get('text')
        categoria = request.POST.get('categoria')
        size = request.POST.get('size').upper().strip()
        try:
            categoria_obj = Category.objects.get(Name=categoria)
        except Category.DoesNotExist:
            messages.error(request, 'Categoria inválida')
            return redirect('create_clothe')
            
        if size not in sizes:
            messages.error(request, 'Tamanho de roupa invalido')
            return redirect('create_clothe')
        promo = request.POST.get('check') == 'true'
        preco_promo = int(request.POST.get('price_promo')) if promo else None
        if promo and not preco_promo:
            messages.error(request, "Preço promocional obrigatório quando a promoção está marcada.")
            return redirect('create_clothe')
        if not all([nome, preco, unit, marca, categoria, size, texto]):
            messages.error(request, 'Campos incompletos')
            return redirect('create_clothe')
        else:
            try:
                with transaction.atomic():
                    clothe_new = Clothe.objects.create(
                        Name=nome ,
                        Img=img ,
                        Unit=unit ,
                        Price=preco ,
                        Price_promo=preco_promo ,
                        Is_promo = promo
                    )
                    Description.objects.create(
                        Text= texto,
                        Size= size,
                        Specification= espec,
                        Mark= marca,
                        Fk_category= categoria_obj,
                        Fk_clothe= clothe_new,
                    )
                    messages.success(request, 'Roupa cadastrada!')
            except Exception as e:
                messages.error(request, f'Erro: {e}')
            return redirect('create_clothe')
                
    return render(request, 'admin_core/create/clothe.html', {'categorys': Category.objects.all()})

@admin_required
def view_create_category(request):
    if request.method == 'POST':
        categoria = request.POST.get('categoria')
        try:
            if not Category.objects.filter(Name=categoria).exists():
                Category.objects.create(Name=categoria)
            else:
                messages.error(request, 'Já existe uma categoria com esse nome!')
                return redirect('create_category')
        except Exception as e:
            messages.error(request, f'Erro: {e}')
            return redirect('create_category')
            
    return render(request, 'admin_core/create/category.html')

@admin_required
def view_create_img_clothe(request):    
    return render(request, 'admin_core/create/img_clothe.html')

@admin_required
def view_create_user(request):    
    if request.method == 'POST':
        nome = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        email = request.POST.get('email')
        admin = request.POST.get('check') == 'true'
        erros = verify_password(password, password_confirm, email)
        if not erros:
            try:
                User.objects.create_user(
                    username = nome,
                    password = password,
                    email = email,
                    is_staff = admin
                ).save()
                messages.success(request, 'Usuario criado!')
            except Exception as e:
                messages.error(request, f'Erro! {e}')
                
        else:
            messages.error(request, ', '.join(erros))

    return render(request, 'admin_core/create/user.html')

# cRud
# READ ESTA PRONTO
@admin_required
def view_read_clothe(request):
    page_number = request.GET.get('page')
    order = request.GET.get("order", 'Id')
    filtro = request.GET.get("filter", '1')
    asc = request.GET.get("asc", '')
    try:
        active_filter = bool(int(filtro))
    except ValueError:
        active_filter = True
    if not order:
        order = 'Id'
    orderning = asc + order
    paginator = Paginator(Clothe.objects.filter(Active=active_filter).order_by(orderning), 40)
    return render(request, 'admin_core/read/clothe.html', {'page_obj': paginator.get_page(page_number)})

@admin_required
def view_read_category(request):
    page_number = request.GET.get('page')
    
    order = request.GET.get("order", 'Id')
    filtro = request.GET.get("filter", '1')
    asc = request.GET.get("asc", '')
    try:
        active_filter = bool(int(filtro))
    except ValueError:
        active_filter = True
    if not order:
        order = 'Id'
    orderning = asc + order
    paginator = Paginator(Category.objects.filter(Active=active_filter).order_by(orderning), 40)
    
    return render(request, 'admin_core/read/category.html', {'page_obj': paginator.get_page(page_number)})

@admin_required
def view_read_img_clothe(request):    
    return render(request, 'admin_core/read/img_clothe.html')

@admin_required
def view_read_user(request):
    page_number = request.GET.get('page')
    order = request.GET.get("order", 'id')
    filtro = request.GET.get("filter", '1')
    asc = request.GET.get("asc", '')
    try:
        active_filter = bool(int(filtro))
    except ValueError:
        active_filter = True
    if not order:
        order = 'id'
    orderning = asc + order
    paginator = Paginator(User.objects.filter(is_active=active_filter).order_by(orderning), 40)
    return render(request, 'admin_core/read/user.html', {'page_obj': paginator.get_page(page_number)})

# crUd

@admin_required
def view_update_clothe(request, id):
    clothe_obj = get_object_or_404(Clothe, Id=id)
    if request.method == 'POST':
        clothe_obj.Active = True
        clothe_obj.save()
        return redirect('home_adm')
    return render(request, 'admin_core/update/clothe.html', {'clothe': clothe_obj, 'description': Description.objects.get(Fk_clothe=clothe_obj)})

@admin_required
def view_update_category(request, id):
    category_obj = get_object_or_404(Category, Id=id)
    if request.method == 'POST':
        category_obj.Active = True
        category_obj.save()
        return redirect('home_adm')
    return render(request, 'admin_core/update/category.html', {'category': category_obj})

@admin_required
def view_update_img_clothe(request, id):    
    img_clothe = get_object_or_404(ClotheImage, Id=id)
    if request.method == 'POST':
        img_clothe.Active = True
        img_clothe.save()
        return redirect('home_adm')
    return render(request, 'admin_core/update/img_clothe.html', {'img_clothe': img_clothe})

@admin_required
def view_update_user(request, id):  
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.is_active = True
        user.save()
        return redirect('home_adm')
    return render(request, 'admin_core/update/user.html', {'user': user})


# cruD

@admin_required
def view_delete_clothe(request, id):
    clothe_obj = get_object_or_404(Clothe, Id=id)
    if request.method == 'POST':
        clothe_obj.Active = False
        clothe_obj.save()
        return redirect('home_adm')
    return render(request, 'admin_core/delete/clothe.html', {'clothe': clothe_obj, 'description': Description.objects.get(Fk_clothe=clothe_obj)})

@admin_required
def view_delete_category(request, id):
    category_obj = get_object_or_404(Category, Id=id)
    if request.method == 'POST':
        category_obj.Active = False
        category_obj.save()
        return redirect('home_adm')
    return render(request, 'admin_core/delete/category.html', {'category': category_obj})

@admin_required
def view_delete_img_clothe(request, id):    
    img_clothe = get_object_or_404(ClotheImage, Id=id)
    if request.method == 'POST':
        img_clothe.Active = False
        img_clothe.save()
        return redirect('home_adm')
    return render(request, 'admin_core/delete/img_clothe.html', {'img_clothe': img_clothe})

@admin_required
def view_delete_user(request, id):  
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return redirect('home_adm')
    return render(request, 'admin_core/delete/user.html', {'user': user})
