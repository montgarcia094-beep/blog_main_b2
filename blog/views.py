from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Post, Category

# Vista para la página principal del blog
def home(request):
    # Filtramos solo los posts activos y los ordenamos del más reciente al más antiguo
    posts = Post.objects.filter(status=Post.ACTIVATE).order_by('-created_at')
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

# Vista para ver el detalle de un post específico
def detail(request, id):
    # Buscamos el post por su ID; si no existe o no está activo, lanza un error 404
    post = get_object_or_404(Post, id=id, status=Post.ACTIVATE)

    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)