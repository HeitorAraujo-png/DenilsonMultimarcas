from django.urls import path
from admin_core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.admin_view, name='home_adm'),
    path('view-clothes/', views.view_clothes, name='home_adm'),
    path('view-users/', views.view_users, name='home_adm'),
    path('create-clothe/', views.create_clothe, name='home_adm'),
    path('create-category/', views.create_category, name='home_adm'),
    path('create-img-clothe/', views.create_img_clothe, name='home_adm'),
    path('create-user/', views.create_user, name='home_adm'),
]






















if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)