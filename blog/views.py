from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import ComentarioForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
 #from django import ListView
# Create your views here.

@login_required
def post_list(request):
    posts = Post.objects.all().order_by('-fecha_publicacion')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post= get_object_or_404(Post, pk=pk)
    comentarios = post.comentarios.all()

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.post = post
            nuevo_comentario.save()
        else:
            form = ComentarioForm()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comentarios': comentarios, 
        'form': ComentarioForm()
        })

""" class ListaPostsView(ListView):
    model = Post
    template_name = 'blog/lista_posts_view.html'
    context_object_name = 'posts'

 """
""" VISTAS BASADAS EN CLASES"""

def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login') #redirecciona a la vista de inicio de sesión
    return render(request, 'blog/registro.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('post_list')
        else:
            return render(request, 'blog/login.html', {'error': 'Credenciales inválidas'})
    
    return render(request, 'blog/login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')