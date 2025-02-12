from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post
from .forms import PostForm

# Получить все посты
def get_posts(request):
    posts = Post.objects.all()
    posts_data = [{"id": post.id, "title": post.title, "description": post.description, "author": post.author} for post in posts]
    return JsonResponse(posts_data, safe=False)

# Получить пост по id
def get_post(request, id):
    post = get_object_or_404(Post, id=id)
    post_data = {"id": post.id, "title": post.title, "description": post.description, "author": post.author}
    return JsonResponse(post_data)

# Добавить новый пост (POST)
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_posts')  # Перенаправить на список постов
    else:
        form = PostForm()
    return render(request, 'post/add_post.html', {'form': form})

# Удалить пост по id
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('get_posts')  # Перенаправить на список постов

