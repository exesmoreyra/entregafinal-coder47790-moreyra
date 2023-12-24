from django.urls import path
from .views import HomeView, DetailView, AddPostView, UpdatePostView, DeletePostView, LandingPageView, resultados_busqueda
from .views import crear_avatar, avatar_creado, NosotrosView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'), 
    path('home/', HomeView.as_view(), name='home'),
    path('article/<int:pk>', DetailView.as_view(), name='details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/borrar', DeletePostView.as_view(), name='delete_post'),
    path('resultados_busqueda/', resultados_busqueda, name='resultados_busqueda'), 
    path('crear-avatar/', crear_avatar, name='crear_avatar'),
    path('avatar-creado/', avatar_creado, name='avatar_creado'),
    path('nosotros/', NosotrosView.as_view(), name='nosotros'),
    # Nueva URL para la vista de Nosotros
]

# Agrega estas líneas al final del archivo para servir archivos de medios en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
