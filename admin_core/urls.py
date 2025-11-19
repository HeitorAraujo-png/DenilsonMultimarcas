from django.urls import path
from admin_core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.admin_view, name='home_adm')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)