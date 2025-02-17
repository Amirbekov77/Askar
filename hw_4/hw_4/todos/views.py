from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoList, Todo
from .forms import TodoListForm, TodoForm

# Главная страница с перенаправлением на /todo-lists
def home(request):
    return redirect('/todo-lists')

# Список всех TodoLists
def todo_list_view(request):
    todo_lists = TodoList.objects.all()
    return render(request, 'todos/todo_list_view.html', {'todo_lists': todo_lists})

# Детали TodoList
def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todos = Todo.objects.filter(todo_list=todo_list)
    return render(request, 'todos/todo_list_detail.html', {'todo_list': todo_list, 'todos': todos})

# Создание нового TodoList
def todo_list_create(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/todo-lists')
    else:
        form = TodoListForm()
    return render(request, 'todos/todo_list_form.html', {'form': form})

# Удаление TodoList
def todo_list_delete(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    todo_list.delete()
    return redirect('/todo-lists')

# Редактирование TodoList
def todo_list_edit(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    if request.method == 'POST':
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect('/todo-lists')
    else:
        form = TodoListForm(instance=todo_list)
    return render(request, 'todos/todo_list_form.html', {'form': form})

# Создание нового Todo
def todo_create(request, todo_list_id):
    todo_list = get_object_or_404(TodoList, id=todo_list_id)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_list = todo_list
            todo.save()
            return redirect('/todo-lists/{}/'.format(todo_list.id))
    else:
        form = TodoForm()
    return render(request, 'todos/todo_form.html', {'form': form})

# Удаление Todo
def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo_list_id = todo.todo_list.id
    todo.delete()
    return redirect('/todo-lists/{}/'.format(todo_list_id))

# Редактирование Todo
def todo_edit(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/todo-lists/{}/'.format(todo.todo_list.id))
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/todo_form.html', {'form': form})
