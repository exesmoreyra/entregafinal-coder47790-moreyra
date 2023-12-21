from django.urls import path
from .views import HomeView, DetailView, AddPostView, UpdatePostView, DeletePostView, LandingPageView, resultados_busqueda

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'), 
    path('home/', HomeView.as_view(), name='home'),
    path('article/<int:pk>', DetailView.as_view(), name='details'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/borrar', DeletePostView.as_view(), name='delete_post'),
    path('resultados_busqueda/', resultados_busqueda, name='resultados_busqueda'),  # Corregimos la importación
]
