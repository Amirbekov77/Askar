from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Todo
from .forms import TodoForm
from django.views.decorators.csrf import csrf_exempt
import json

# Список всех задач
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

# Получение информации о задаче по id
def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

# Создание новой задачи (через форму)
@csrf_exempt
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form})

# Удаление задачи по id
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return redirect('todo_list')

