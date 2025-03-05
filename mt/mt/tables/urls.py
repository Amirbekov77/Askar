from django.urls import path
from . import views

urlpatterns = [
    path('', views.table_list, name='table_list'),
    path('available/', views.available_tables, name='available_tables'),
    path('<int:id>/', views.table_detail, name='table_details'),
    path('create/', views.create_table, name='create_table'),
]

