from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.get_posts, name='get_posts'),
    path('posts/<int:id>/', views.get_post, name='get_post'),
    path('posts/add/', views.add_post, name='add_post'),
    path('posts/<int:id>/delete/', views.delete_post, name='delete_post'),
]
