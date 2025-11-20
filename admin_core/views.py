from django.shortcuts import render
from core.decorators import admin_required
# Create your views here.
@admin_required
def admin_view(request):
    return render(request, 'admin_core/admin.html')

# Crud
@admin_required
def create_clothe(request):
    return render(request, 'admin_core/create/clothe.html')

@admin_required
def create_category(request):    
    return render(request, 'admin_core/create/category.html')

@admin_required
def create_img_clothe(request):    
    return render(request, 'admin_core/create/img_clothe.html')

@admin_required
def create_user(request):    
    return render(request, 'admin_core/create/user.html')

# cRud
@admin_required
def view_clothes(request):
    return render(request, 'admin_core/view_clothes.html')

@admin_required
def view_users(request):    
    return render(request, 'admin_core/view_users.html')

# crUd





# cruD
