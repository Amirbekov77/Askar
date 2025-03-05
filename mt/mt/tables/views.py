# tables/views.py
from django.shortcuts import render, get_object_or_404
from .models import Table

def table_list(request):
    # Получаем все столы
    tables = Table.objects.all()
    return render(request, 'tables/table_list.html', {'tables': tables})

def table_detail(request, id):
    # Получаем конкретный стол по его ID
    table = get_object_or_404(Table, id=id)
    return render(request, 'tables/table_detail.html', {'table': table})

def available_tables(request):
    # Извлекаем все столы, которые доступны
    available_tables = Table.objects.filter(is_available=True)
    return render(request, 'tables/table_available.html', {'available_tables': available_tables})

# tables/views.py
from django.shortcuts import render, redirect
from .models import Table
from .forms import TableForm

def create_table(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем новый столик в базе данных
            return redirect('table_list')  # Перенаправляем на список столов
    else:
        form = TableForm()
    return render(request, 'tables/table_form.html', {'form': form})
