from django.contrib import admin
from .models import *

# Register your models here.
class ClotheAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Name', 'Price', 'Unit' ,'Is_promo', 'Price_promo', 'Active', )
    search_fields = ('Id', 'Name', 'Price', 'Unit' ,'Is_promo', 'Price_promo', 'Active', )
    list_filter = ('Id', 'Name', 'Price', 'Unit' ,'Is_promo', 'Price_promo', 'Active', )
    ordering = ('-Id', )
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Name', 'Active', )
    search_fields = ('Id', 'Name', 'Active', )
    list_filter = ('Id', 'Name', 'Active', )
    ordering = ('-Id', )

class ClotheImageAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Fk_clothe', )
    search_fields = ('Id', 'Fk_clothe', )
    list_filter = ('Id', 'Fk_clothe', )
    ordering = ('-Id', )
    
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ('Id', 'Text', 'Size', 'Specification' ,'Mark', 'Fk_category', 'Fk_clothe', )
    search_fields = ('Id', 'Text', 'Size', 'Specification' ,'Mark', 'Fk_category', 'Fk_clothe', )
    list_filter = ('Id', 'Text', 'Size', 'Specification' ,'Mark', 'Fk_category', 'Fk_clothe', )
    ordering = ('-Id', )
    
admin.site.register(Clothe, ClotheAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ClotheImage, ClotheImageAdmin)
admin.site.register(Description, DescriptionAdmin)