from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('miblog.urls')),
    path('usuarios/', include('django.contrib.auth.urls')),
    path('usuarios/', include('usuarios.urls')),
]
