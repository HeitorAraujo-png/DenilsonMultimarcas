from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name='home'),
    path('admin/', include('admin_core.urls'), name='adm'),
    path('login/', include('login_core.urls'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('adm/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)