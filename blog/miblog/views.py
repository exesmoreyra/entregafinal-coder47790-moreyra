from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.decorators import login_required
from .forms import PostForm
import json 

#def home(request):
#   return render(request, 'home.html' , {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
   

class DetailView(DetailView):
    model = Post
    template_name = 'details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'   
    

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    
    
class LandingPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'landing_page.html')
    
def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            nueva_publicacion = form.save(commit=False)
            nueva_publicacion.usuario = request.user
            nueva_publicacion.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'nombre_de_tu_template_para_creacion_de_post.html', {'form': form})

def resultados_busqueda(request):
    query = request.GET.get('q', '')
    resultados_str = request.GET.get('resultados', '[]')

    # Decodifica los resultados JSON
    resultados = json.loads(resultados_str)

    context = {
        'query': query,
        'resultados': resultados,
    }

    return render(request, 'resultados_busqueda.html', context)