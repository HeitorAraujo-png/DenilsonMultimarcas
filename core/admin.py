from django.contrib import admin
from .models import Roupa

# Register your models here.

class RoupaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'unit' ,'is_promo', 'price_promo', )
    search_fields = ('id', 'name', 'price', 'unit' ,'is_promo', 'price_promo', )
    list_filter = ('id', 'name', 'price', 'unit' ,'is_promo', 'price_promo', )
    ordering = ('-id', )
    
    
admin.site.register(Roupa, RoupaAdmin)