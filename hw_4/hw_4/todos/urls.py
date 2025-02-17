from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo-lists/', views.todo_list_view, name='todo_list_view'),
    path('todo-lists/create/', views.todo_list_create, name='todo_list_create'),
    path('todo-lists/<int:id>/', views.todo_list_detail, name='todo_list_detail'),
    path('todo-lists/<int:id>/delete/', views.todo_list_delete, name='todo_list_delete'),
    path('todo-lists/<int:id>/edit/', views.todo_list_edit, name='todo_list_edit'),
    path('todo-lists/<int:todo_list_id>/todo/create/', views.todo_create, name='todo_create'),
    path('todos/<int:id>/delete/', views.todo_delete, name='todo_delete'),
    path('todos/<int:id>/edit/', views.todo_edit, name='todo_edit'),
]
