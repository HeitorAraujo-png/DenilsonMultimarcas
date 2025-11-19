from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Roupa

# Create your views here.


def logout_view(request):
    logout(request)
    return redirect('home')


def home_view(request):
    page_number = request.GET.get('page')
    query = request.GET.get('search', '').strip()
    objetos = Roupa.objects.filter(is_promo=False)
    if query:
        objetos = Roupa.objects.filter(
            is_promo=False,
            name__icontains=query
        )
    paginator = Paginator(objetos, 40)
    return render(request, 'core/home.html', {
                            'page_obj': paginator.get_page(page_number), 
                            'promo': Roupa.objects.filter(is_promo=True),
                            'login': True if request.user.is_authenticated else False,
                            'nivel': True if request.user.is_superuser or request.user.is_staff and request.user.is_active else False
                })

