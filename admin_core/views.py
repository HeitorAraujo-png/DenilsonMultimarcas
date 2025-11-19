from django.shortcuts import render
from core.decorators import admin_required
# Create your views here.
@admin_required
def admin_view(request):
    return render(request, 'admin_core/admin.html')