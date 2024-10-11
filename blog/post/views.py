from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm 


# Create your views here.

def home(request):
    posts = Post.objects.all() 
    context = {'posts':posts}
    return render(request, 'post/posts_page.html', context)   



def post(request, pk):
    post = Post.objects.get(id=pk)
    context={'post':post}
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

    



