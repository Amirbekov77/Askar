from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Todo
from .forms import TodoForm

# Получение списка всех todos
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

# Получение одного todo по id
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todos/todo_detail.html', {'todo': todo})

# Создание нового todo через POST-запрос
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todos/')
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form})

# Удаление todo
def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('/todos/')

