from django.urls import path
from admin_core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.admin_view, name='home_adm'),
    path('create/clothe/', views.view_create_clothe, name='create_clothe'),
    path('create/category/', views.view_create_category, name='create_category'),
    path('create/img-clothe/', views.view_create_img_clothe, name='create_img_clothe'),
    path('create/user/', views.view_create_user, name='create_user'),
    path('read/clothe/', views.view_read_clothe, name='read_clothe'),
    path('read/category/', views.view_read_category, name='read_category'),
    path('read/img-clothe/', views.view_read_img_clothe, name='read_img_clothe'),
    path('read/user/', views.view_read_user, name='read_user'),
    path('update/clothe/<id>/', views.view_update_clothe, name='update_clothe'),
    path('update/category/<id>/', views.view_update_category, name='update_category'),
    path('update/img-clothe/<id>/', views.view_update_img_clothe, name='update_img_clothe'),
    path('update/user/<id>/', views.view_update_user, name='update_user'),
    path('delete/clothe/<id>/', views.view_delete_clothe, name='delete_clothe'),
    path('delete/category/<id>/', views.view_delete_category, name='delete_category'),
    path('delete/img-clothe/<id>/', views.view_delete_img_clothe, name='delete_img_clothe'),
    path('delete/user/<id>/', views.view_delete_user, name='delete_user'),
]






















if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)