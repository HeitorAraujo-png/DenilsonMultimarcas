from django.urls import path
from admin_core import views

urlpatterns = [
    path('', views.admin_view, name='home_adm')
]
