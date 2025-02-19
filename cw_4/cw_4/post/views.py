from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Thread, Post
from .forms import ThreadForm, PostForm

# Главная страница, редирект на /threads
def index(request):
    return redirect('threads')

# Список всех threads
def thread_list(request):
    threads = Thread.objects.all()
    return render(request, 'post/threads_list.html', {'threads': threads})

# Детали конкретного thread
def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    posts = thread.posts.all()
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.thread = thread
            post.save()
            return redirect('thread_detail', thread_id=thread.id)
    else:
        post_form = PostForm()
    return render(request, 'thread_detail.html', {'thread': thread, 'posts': posts, 'post_form': post_form})

# Удаление thread
def thread_delete(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    thread.delete()
    return redirect('threads')

# Редактирование thread
def thread_edit(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', thread_id=thread.id)
    else:
        form = ThreadForm(instance=thread)
    return render(request, 'thread_edit.html', {'form': form, 'thread': thread})

# Удаление post
def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    thread_id = post.thread.id
    post.delete()
    return redirect('thread_detail', thread_id=thread_id)

# Редактирование post
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', thread_id=post.thread.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form, 'post': post})
