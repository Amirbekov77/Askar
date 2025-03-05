from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation_create'),
    path('<int:pk>/', views.reservation_detail, name='reservation_detail'),
    path('create/', views.create_reservation, name='create_reservation'),
    path('<int:id>/update/', views.update_reservation_status, name='update_reservation_status'),
    path('<int:id>/delete/', views.delete_reservation, name='delete_reservation'),
]
