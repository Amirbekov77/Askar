# mt/urls.py
from django.urls import path, include
from reservations import views as reservations_views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),  # Подключаем URL-ы приложения customers
    path('tables/', include('tables.urls')),        # Подключаем URL-ы приложения tables
    path('reservations/', include('reservations.urls')),  # Подключаем URL-ы приложения reservations
]
