from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('threads/', views.thread_list, name='threads'),
    path('threads/<int:thread_id>/', views.thread_detail, name='thread_detail'),
    path('threads/<int:thread_id>/delete/', views.thread_delete, name='thread_delete'),
    path('threads/<int:thread_id>/edit/', views.thread_edit, name='thread_edit'),
    path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
]
