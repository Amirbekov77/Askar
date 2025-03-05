# customers/views.py
from django.shortcuts import render
from .models import Customer

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})

def customer_detail(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, 'customers/customer_detail.html', {'customer': customer})

# customers/views.py
from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm

def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем нового клиента в базе данных
            return redirect('customer_list')  # Перенаправляем на список клиентов
    else:
        form = CustomerForm()
    return render(request, 'customers/customer_list.html', {'form': form})




