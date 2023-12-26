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
from .forms import AvatarForm 
from django.contrib import messages

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

    return render(request, 'landing_page.html', {'form': form})

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

@login_required
def crear_avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, instance=request.user)
        if form.is_valid():
             avatar_choice = form.cleaned_data['avatar']
             print(f'Avatar Choice: {avatar_choice}') 
             request.user.avatar = f'avatars/{avatar_choice}'
             request.user.save()

             messages.success(request, 'Avatar actualizado exitosamente.')
             return redirect('landing_page')
    else:
        form = AvatarForm(instance=request.user)
    return render(request, 'crear_avatar.html', {'form': form})



def avatar_creado(request):
    avatar_url = request.GET.get('avatar_url', None)
    return render(request, 'avatar_creado.html', {'avatar_url': avatar_url})


class NosotrosView(View):
    def get(self, request):
        return render(request, 'nosotros.html')