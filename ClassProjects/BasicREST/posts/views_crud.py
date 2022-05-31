from django.shortcuts import render, redirect
from .models import Post


def index(request):
    return render(request, 'crud/index.html')


def read(request):
    post = Post.objects.all()
    context = {'post': post}
    return render(request, 'crud/p_result.html', context)

def create(request):
    post = Post(title=request.POST['title'], content=request.POST['content'])
    post.save()
    return render(request, 'crud/index.html')

def edit(request, id):
    post = Post.objects.get(id=id)
    context = {'post': post}
    return render(request, 'crud/p_edit.html', context)

def update(request, id):
    post = Post.objects.get(id=id)
    post.title = request.POST['title']
    post.content = request.POST['content']
    post.save()
    return redirect('index')

def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('index')
