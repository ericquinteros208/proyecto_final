from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import CategoryForm

from .forms import PostForm 


# Create your views here.

def home(request):
    categorias = Category.objects.all() 
    context = {'categorias': categorias}
    return render(request, 'post/posts_page.html', context)   


def post_list(request, categoria_id):
    categoria = get_object_or_404(Category, id=categoria_id)
    posts = Post.objects.filter(categoria=categoria)
    context={'posts': posts, 'categoria': categoria}
    return render(request, 'post/post.html',context)


def formulario(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES )
        if form.is_valid():
            form.save()
            return redirect('home')

    context = { 'form': form}
    return render (request , 'post/form_post.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post/post_detail.html', {'post': post})


def buscar_posts(request):
    query = request.GET.get('q')
    resultados = Post.objects.filter(titulo__icontains=query) if query else Post.objects.all()
    
    return render(request, 'post/buscar_resultados.html', {'resultados': resultados, 'query': query})



def buscar_categorias(request):
    query = request.GET.get('q')  # Obtiene la consulta de búsqueda
    if query:
        categorias = Category.objects.filter(name__icontains=query)  # Filtra por nombre
    else:
        categorias = Category.objects.all()  # Devuelve todas las categorías si no hay consulta
    return render(request, 'post/posts_page.html', {'categorias': categorias})





    



